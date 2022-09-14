import pandas as pd

def Cohort(df):

    df1 =df.copy()
    # time stampes
    times = pd.to_datetime(
        ['2014-12-31', '2015-06-30', '2015-12-31', '2016-06-30', '2016-12-31', '2017-06-30', '2017-12-31', '2018-06-30',
         '2018-12-31'])
    label = ['2015H1', '2015H2', '2016H1', '2016H2', '2017H1', '2017H2', '2018H1', '2018H2']
    customer = []
    u_customer = []

    for i in range(8):
        customer_half_year = df1.loc[(df1.OrderDate > times[i]) & (df1.OrderDate <= times[i + 1]),
                             :].CustomerID
        u_customer_half_year = list(set(customer_half_year))
        print(label[i] + 'Placed Customer', len(customer_half_year))
        print(label[i] + 'Placed Customer without duplicates', len(u_customer_half_year))
        customer.extend(customer_half_year)
        u_customer.append(u_customer_half_year)

    for i, customer_list_half_year in enumerate(u_customer):
        if i > 0 and i < 7:
            last_list = []  # All previous customer IDs
            retain_list = []  # Retained customer per half year
            for j in range(0, i):
                last_list.extend(u_customer[j])
            last_list = list(set(last_list))
            new_list = [cust for cust in customer_list_half_year if cust not in last_list]  # 保存当前周期新增客户ID
            for k in range(i + 1, 8):
                retain_list.append(len([cust for cust in u_customer[k] if cust in new_list]))
            print(label[i] + 'Number of new users', len(new_list), 'Retention rate', [round(i / len(new_list), 3) for i in retain_list])