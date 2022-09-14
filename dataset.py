import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

from warnings import filterwarnings
filterwarnings('ignore')

csv_path = 'North_American_Superstore.csv'
df = pd.read_csv(csv_path, encoding="gbk")

def preprocess(df):

    df.rename(columns = lambda x : x.replace(' ',''),inplace = True)

    # drop duplicates
    df = df.drop_duplicates()

    # Outliers
    df.loc[df['Sales'] < 0].Sales.count()  # sales<0
    df = df.loc[(df['Sales'] > 0) & (df['Quantity'] > 0)]  # remain which sales>0

    # Null value
    df.isnull().sum()
    # df = df.loc[~df.PostalCode.isnull()]  # In this example, only 'PostalCode' has null value

    # 'OrderDate' to datetime format
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    df.info()

    print('The latest order date：', df['OrderDate'].max())
    print('The earliest order data：', df['OrderDate'].min())

    return df