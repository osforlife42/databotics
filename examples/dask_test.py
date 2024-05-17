import dask
import dask.dataframe as dd
import pandas as pd
import time

# Create a dummy data source that generates a sequence of numbers
class DataSource:
    def __init__(self):
        self.i = 0

    def generate_data(self):
        while True:
            self.i += 1
            time.sleep(1)
            return {'value': [self.i]}

# Create a Dask dataframe from the data source
def create_dask_df(data_source):
    df = dd.from_pandas(pd.DataFrame(data_source()), npartitions=1)
    df = df.set_index('value')
    return df

# Create the data source and Dask dataframe
data_source = DataSource()
df = create_dask_df(data_source.generate_data)

print('------')

# Print the data every second
while True:
    print(df.compute())
    time.sleep(1)
    print('------')
