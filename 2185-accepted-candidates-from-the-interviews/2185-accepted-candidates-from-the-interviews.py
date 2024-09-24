import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    p = rounds.groupby('interview_id')['score'].sum()
    t = pd.merge(candidates, p, left_on='interview_id', right_on='interview_id')
    return t[(t['score'] > 15) & (t['years_of_exp'] >= 2)]['candidate_id'].to_frame()