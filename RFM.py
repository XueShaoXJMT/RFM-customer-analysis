import pandas as pd

def RFM_fetch(df):

    # Total frequency
    df_f = df.groupby('CustomerID',as_index=False).OrderID.count().rename(columns={'OrderID':'Frequency'})
    df_f.set_index('CustomerID',drop=True,inplace=True)

    # Monetary and Recency
    df_g = df.groupby('CustomerID')
    # lambda df : df.max() - df.min()
    df_rm = df_g.agg({'Sales': 'sum', 'OrderDate': 'max', 'Profit': 'sum'}).rename(
        columns={'Sales': 'Monetary'})
    df_rm['Recency'] = (pd.to_datetime('2019-01-01') - df_rm['OrderDate']).dt.days
    df_rm = df_rm.drop('OrderDate', axis=1)

    # Yearly frequency
    DiffYears = df_g.agg({'OrderDate': (lambda df: df.dt.year.max() - df.dt.year.min() + 1)}).rename(
        columns={'OrderDate': 'DiffYears'}).DiffYears
    df_f.Frequency = df_f.Frequency / DiffYears

    # merge
    df_rfm = df_rm.merge(df_f, on='CustomerID')

    rmid = df_rfm['Recency'].median()
    fmid = df_rfm['Frequency'].median()
    mmid = df_rfm['Monetary'].median()

    # 划分客户类型的函数
    def customer_type_func(df):
        customer_type_list = []
        for i in range(len(df)):
            if df.iloc[i, 2] <= rmid and df.iloc[i, 3] >= fmid and df.iloc[i, 0] >= mmid:
                customer_type_list.append('Best Customers')
            elif df.iloc[i, 2] <= rmid and df.iloc[i, 3] < fmid and df.iloc[i, 0] >= mmid:
                customer_type_list.append('High-spending New Customers')
            elif df.iloc[i, 2] > rmid and df.iloc[i, 3] >= fmid and df.iloc[i, 0] >= mmid:
                customer_type_list.append('Lowest-Spending Active Loyal Customers')
            elif df.iloc[i, 2] > rmid and df.iloc[i, 3] < fmid and df.iloc[i, 0] >= mmid:
                customer_type_list.append('Churned Best Customers')
            else:
                customer_type_list.append('Average Customers')
        df['Customer_Type'] = customer_type_list

    customer_type_func(df_rfm)

    return df_rfm

