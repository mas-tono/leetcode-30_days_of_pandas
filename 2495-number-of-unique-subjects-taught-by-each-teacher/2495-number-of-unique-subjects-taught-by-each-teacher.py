import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher_cnt = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    teacher_cnt.rename(columns={'teacher_id':'teacher_id', 'subject_id':'cnt'}, inplace=True)
    return teacher_cnt