import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    
    import re
    users['cek1'] = users['mail'].apply(lambda x: 'ok' if x[-13:]=='@leetcode.com' else 'no')
    users['cek2'] = users['mail'].apply(lambda x: 'ok' if re.match((r'^[a-zA-Z]'), x[:len(x)-13]) else 'no')
    users['cek3'] = users['mail'].apply(lambda x: 'ok' if re.match((r'^[a-zA-Z0-9_.-]+$'), x[:len(x)-13]) else 'no')
    return users[(users['cek1']=='ok') & (users['cek2']=='ok') & (users['cek3']=='ok')][['user_id', 'name', 'mail']]
