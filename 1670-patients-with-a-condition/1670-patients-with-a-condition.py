import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients['cek'] = (patients['conditions'].str.startswith('DIAB1')) | (patients['conditions'].str.contains(' DIAB1')) 

    return patients[patients['cek']==True][['patient_id', 'patient_name', 'conditions']]