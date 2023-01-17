import datetime
import pandas as pd
import numpy as np
import matplotlib


def pie(purposes):
    df = pd.DataFrame(purposes)
    return df.plot.pie(subplots=True)
