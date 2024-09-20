import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(ascending=False, method='dense')
    return scores.sort_values('score', ascending=False)[['score', 'rank']]