# Changed the 'name' by using the function 'str.capitalize()' and return the resulting df in ascending
# user_id.

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values(by=['user_id'])