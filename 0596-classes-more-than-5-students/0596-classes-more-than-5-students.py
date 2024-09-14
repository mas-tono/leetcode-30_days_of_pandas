import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    cnt_class = courses.groupby('class')['student'].count().reset_index()
    return cnt_class[cnt_class['student'] >= 5][['class']]