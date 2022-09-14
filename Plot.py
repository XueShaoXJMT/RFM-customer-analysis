import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def plot0(df):
    sns.pairplot(df,hue='Customer_Type', x_vars=["Recency", "Frequency", "Monetary"],
        y_vars=["Recency", "Frequency", "Monetary"], markers=["o", "s", "P","p","D"])

def plot1(df):
    f1 = plt.figure(1,figsize=(16,9),dpi=100)
    ax1 = f1.add_subplot(111)
    sns.countplot(y='Customer_Type',order=df['Customer_Type'].value_counts(ascending=False).index,data=df,palette='Blues') # y轴是客户类型，x轴
    ax1.tick_params(labelsize=15)
    ax1.set_title('Number of each customer type',fontsize=20)
    ax1.set_xlabel('')
    ax1.set_ylabel('')
    num_by_type=list(df.groupby('Customer_Type').size())
    num_by_type=sorted(num_by_type,reverse=True)
    for x,y in enumerate(num_by_type):
        ax1.text(y+0.2,x,'%s' %y,va='center',size=12)

def plot2(df):

    f2 = plt.figure(2,figsize=(16,9),dpi=100)

    ax_1 = f2.add_subplot(131)
    labels=df.groupby('Customer_Type').Customer_Type.size().index
    customer_num=df.groupby('Customer_Type').Customer_Type.size()
    explode=[0.05,0,0,0,0]
    ax_1.pie(customer_num,explode=explode,labels=labels,textprops={'fontsize':12},shadow=False,autopct='%.2f%%')
    ax_1.axis('equal')
    ax_1.set_title('Proportion of each customer type',fontsize=20)

    ax_2 = f2.add_subplot(132)
    Monetary_sum=df.groupby('Customer_Type').Monetary.sum()
    explode=[0,0.05,0,0,0]
    ax_2.pie(Monetary_sum,explode=explode,labels=labels,textprops={'fontsize':12},shadow=False,autopct='%.2f%%')
    ax_2.axis('equal')
    ax_2.set_title('Sales of each customer type',fontsize=20)

    ax_3 = f2.add_subplot(133)
    Porfit_sum=df.groupby('Customer_Type').Profit.sum()
    explode=[0,0.05,0,0,0]
    ax_3.pie(Porfit_sum,explode=explode,labels=labels,textprops={'fontsize':12},shadow=False,autopct='%.2f%%')
    ax_3.axis('equal')
    ax_3.set_title('Profit of each customer type',fontsize=20)