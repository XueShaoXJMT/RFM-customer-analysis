import pandas as pd
from warnings import filterwarnings
from dataset import *
from RFM import *
from Profit import *
from Plot import *
from Cohort_Analysis import *

filterwarnings('ignore')

df = pd.read_csv('North_American_Superstore.csv', encoding="gbk")

df = preprocess(df)

df1 = df.copy()
df1.drop_duplicates(subset=['OrderID'], keep='first', inplace=True)

df_rfm = RFM_fetch(df1)

profit_analyze(df_rfm)

plot0(df_rfm)
plot1(df_rfm)
plot2(df_rfm)

Cohort(df1)










