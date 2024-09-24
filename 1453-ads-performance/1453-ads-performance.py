import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads['check'] = ads['action'].apply(lambda x:1 if x=='Clicked' else 1 if x=='Viewed' else 0)
    ads['click'] = ads['action'].apply(lambda x:1 if x=='Clicked' else 0)
    p = ads.groupby('ad_id')[['check', 'click']].sum()
    p.reset_index(inplace=True)
    p['ctr'] = round((p['click']/p['check'])*100, 2)
    return p.fillna(0)[['ad_id', 'ctr']].sort_values(['ctr', 'ad_id'], ascending=[False, True])