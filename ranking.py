def rank_top_hitters(df, top_n=3):
    df = df.sort_values('avg_prob', ascending=False).head(top_n)
    return df
