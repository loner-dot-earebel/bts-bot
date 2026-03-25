import pandas as pd

def get_bm_nn_rank(player): 
    # Replace with actual scraping logic
    return 1

def get_bm_log5_rank(player):
    return 1

def get_xwoba_rank(player):
    return 1

def get_streaksmarter_rank(player):
    return 1

def resolve_ties(df):
    df['tie_score'] = df['player'].apply(lambda x: (
        get_bm_nn_rank(x)*1 +
        get_bm_log5_rank(x)*2 +
        get_xwoba_rank(x)*3 +
        get_streaksmarter_rank(x)*4
    ))
    df = df.sort_values(['avg_prob','tie_score'], ascending=[False, True])
    return df
