import pandas as pd

def lambda_handler(event, context):
    df = pd.DataFrame()
    print(df)

    list = ['one', 'two', 'three', 'four', 'five']

    df = pd.DataFrame(list)
    
    print(df)
    print(df.index())