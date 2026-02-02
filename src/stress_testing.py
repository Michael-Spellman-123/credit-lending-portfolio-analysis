def apply_stress(pd, lgd, macro_factor=1.2):
    stressed_pd = pd * macro_factor
    stressed_lgd = lgd * macro_factor
    return stressed_pd, stressed_lgd
