-- AI General III Tactical Controller (WH3 maintenance fork starter)
-- Purpose: add strategic unitcontroller layer without replacing existing UI/config flow.

---@class aigeneral_tactical_controller
---@field owner any
---@field is_debug boolean
---@field last_tick number
---@field tick_ms number
---@field mode string
---@field target_cache table<string, string>
local M = {
    mode = "balanced",
    last_tick = 0,
    tick_ms = 1200,
    target_cache = {}
}

local function _out(msg)
    out("[AI_GEN_TAC] " .. tostring(msg))
end

local function _safe_uc(su)
    if not su or not su.uc then return nil end
    return su.uc
end

local function _can_act(su)
    if not su then return false end
    local u = su.unit
    if not u or u:is_shattered() or u:is_routing() or u:is_dead() then return false end
    return true
end

function M:new(owner, is_debug)
    local o = {}
    setmetatable(o, self)
    self.__index = self
    o.owner = owner
    o.is_debug = is_debug == true
    o.mode = "balanced"
    o.last_tick = 0
    o.tick_ms = 1200
    o.target_cache = {}
    return o
end

function M:log(msg)
    if self.is_debug then _out(msg) end
end

function M:evaluate_battle_state(friendly_sus, enemy_sus)
    local state = {
        friendly_alive = 0,
        enemy_alive = 0,
        local_ratio = 1.0,
        should_commit_reserve = false
    }

    for i = 1, #friendly_sus do
        if _can_act(friendly_sus[i]) then state.friendly_alive = state.friendly_alive + 1 end
    end
    for i = 1, #enemy_sus do
        if _can_act(enemy_sus[i]) then state.enemy_alive = state.enemy_alive + 1 end
    end

    if state.enemy_alive > 0 then
        state.local_ratio = state.friendly_alive / state.enemy_alive
    end
    state.should_commit_reserve = state.local_ratio < 0.85

    if state.local_ratio > 1.25 then
        self.mode = "aggressive"
    elseif state.local_ratio < 0.85 then
        self.mode = "defensive"
    else
        self.mode = "balanced"
    end

    return state
end

function M:score_target_for_unit(friend_su, enemy_su)
    if not _can_act(friend_su) or not _can_act(enemy_su) then return -9999 end
    local score = 0
    local e = enemy_su.unit
    if e:is_artillery() then score = score + 40 end
    if e:is_missile_infantry() then score = score + 25 end
    if e:is_cavalry() then score = score + 10 end
    if e:is_flying() then score = score + 10 end
    if e:is_wavering() or e:is_routing() then score = score - 35 end
    if e:is_in_melee() then score = score + 5 end
    return score
end

function M:pick_best_target(friend_su, enemy_sus)
    local best, best_score = nil, -9999
    for i = 1, #enemy_sus do
        local s = self:score_target_for_unit(friend_su, enemy_sus[i])
        if s > best_score then
            best_score = s
            best = enemy_sus[i]
        end
    end
    return best, best_score
end

function M:issue_attack(friend_su, target_su, ranged_mode)
    local uc = _safe_uc(friend_su)
    if not uc or not target_su or not target_su.unit then return false end
    if ranged_mode then uc:melee(false) else uc:melee(true) end
    uc:attack_unit(target_su.unit, true, true)
    uc:release_control()
    return true
end

function M:tick(now_ms, friendly_sus, enemy_sus)
    if now_ms - self.last_tick < self.tick_ms then return end
    self.last_tick = now_ms

    local state = self:evaluate_battle_state(friendly_sus, enemy_sus)
    self:log("mode=" .. self.mode .. " ratio=" .. tostring(state.local_ratio))

    for i = 1, #friendly_sus do
        local fsu = friendly_sus[i]
        if _can_act(fsu) then
            local target = self:pick_best_target(fsu, enemy_sus)
            if target then
                local use_range = fsu.unit:is_missile_infantry() and not fsu.unit:is_in_melee()
                self:issue_attack(fsu, target, use_range)
            end
        end
    end
end

return M
