formula_list = {
    "hp" : "hp = (lvl/100 * ((stat_base*2) + iv)) + lvl",
    "stat" : "stat = (5 + (lvl/100 * ((stat_base*2) + iv))) * nature",
    "catch" : "catch = (hp_max*3 - hp_now*2) * catch_ratio * ball_ratio/hp_max*3 * status ",
    "damage": "damage = 1/100 * stab * eff * v * ((2/10 * lvl + 1) * atq * power/25 * def + 2)",
}

catch_rate_dict = {
    "fast": "exp = 4 * lvl**3 / 5",
    "normal": "exp = lvl**3",
    "slow": "exp = 5 * lvl**3 / 4",
    "parabolic": "6 * lvl**3 / 5 - 15 * lvl**2 + 100 * lvl -140"
}