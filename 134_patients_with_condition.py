# Since there are multiple conditions, we need to look for two things, conditions that startswith 'DIAB1'
# and conditions that contain ' DIAB1'. Note the "contain" has a blank space at the start for the spaces
# between words.

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[(patients['conditions'].str.startswith('DIAB1')) | \
        (patients['conditions'].str.contains(' DIAB1'))]
    return df