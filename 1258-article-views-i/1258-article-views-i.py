import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views['cek'] = views['author_id'] == views['viewer_id']
    return views[views['cek'] == True][['author_id']].drop_duplicates().rename(columns={'author_id':'id'}).sort_values('id')