def profit_analyze(df):

    # profit value > 0
    df['Profit_Type'] = (df.Profit > 0)
    df_Profit_num = df.groupby(['Customer_Type', 'Profit_Type']).size().reset_index(name='Customer_Num')
    df_Profit_num = df_Profit_num[df_Profit_num.Profit_Type == True]

    # Customer number
    df_Cus_Num = df.groupby(['Customer_Type']).size().reset_index(name='Customer_Num')
    # Profit per customer
    df_Cus_Num['Customer_Rate'] = df_Profit_num.Customer_Num.values / df_Cus_Num.Customer_Num
    print(df_Cus_Num)

    # Total profit by customer type
    df_Profit = df.groupby(['Customer_Type']).Profit.sum().reset_index(name='Profit')
    print(df_Profit)

    # Monetary-vise
    df_Monetary = df.groupby('Customer_Type').Monetary.sum().reset_index(name='Monetary')
    df_Monetary['Profit_Rate'] = df_Profit.Profit / df_Monetary.Monetary
    df_Monetary['Profit'] = df_Profit.Profit
    df_Monetary['Monetary_Per_Cust'] = df_Monetary.Monetary / df_Cus_Num.Customer_Num
    df_Monetary['Profit_Per_Cust'] = df_Monetary.Profit / df_Cus_Num.Customer_Num
    print(df_Monetary)




