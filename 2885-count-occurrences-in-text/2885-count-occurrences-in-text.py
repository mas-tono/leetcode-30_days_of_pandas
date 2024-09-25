#1. clean all leading and trailing whitespaces -> trim
#2. the requirement stated 'standalone word' -> bull/bear at beginning and end doesn't count -> so we use find, rfind to use string after first space and before last space (excluding first word and last word)
#3. use r'\bbear\b' r'\bbull\b' to do the main task

import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    files['trim'] = files['content'].str.strip()
    files['content_2'] = files['trim'].apply(lambda x: x[x.find(' '):x.rfind(' ')])
    files['bear'] = files['content_2'].apply(lambda x: 1 if re.search(r'\bbear\b', x) else 0)
    files['bull'] = files['content_2'].apply(lambda x: 1 if re.search(r'\bbull\b', x) else 0)
    c = pd.DataFrame({'word':['bull', 'bear'], 'count':[files['bull'].sum(), files['bear'].sum()]})
    return c