import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    ss = pd.merge(students, subjects, how='cross')
    dd = pd.merge(ss, examinations, how='left', on=['student_id', 'subject_name'], indicator=True)
    dd['_merge'] = dd['_merge'].cat.rename_categories ({'both':1, 'left_only':0})
    dd['_merge'] = pd.to_numeric(dd['_merge'],errors='coerce')
    return dd.groupby(['student_id', 'student_name', 'subject_name'], dropna=False)['_merge'].agg([('attended_exams', 'sum')]).reset_index()

    