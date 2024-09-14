import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['rank'] = activity.groupby('player_id')['event_date'].rank('min')
    return activity[activity['rank'] == 1][['player_id', 'event_date']].rename(columns={'event_date':'first_login'})