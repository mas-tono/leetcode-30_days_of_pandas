import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    tf = actor_director.groupby(['actor_id', 'director_id']).count().reset_index()
    return tf[tf['timestamp'] >= 3] [['actor_id', 'director_id']]