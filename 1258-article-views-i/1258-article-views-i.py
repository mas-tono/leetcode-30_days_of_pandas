import pandas as pd

# create a check column where author_id = viewer_id
# return only unique author_id from check column, rename the column, sort it by id

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views['check'] = views['author_id'] == views['viewer_id']
    return views[views['check'] == True][['author_id']].drop_duplicates().rename(columns={'author_id':'id'}).sort_values('id')