import datetime
import pandas as pd
import numpy as np
import matplotlib


def pie(purposes):
    df = pd.DataFrame(purposes)
    df['deadline'] = pd.to_datetime(df['deadline'], format='%d.%m.%Y', errors='ignore')
    print(df.head())
    df['count_nocomplete'] = df.apply(lambda x: x.isnull().sum(), axis='columns')
    df['count_complete'] = df.apply(lambda x: x.isnull().mean(), axis='columns')
