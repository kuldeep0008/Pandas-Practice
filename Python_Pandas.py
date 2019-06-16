#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question number One: Open, High, Low and Close and Volumes aggregated at a monthly level. 
import pandas as pd
import numpy as np
df=pd.read_csv("C:/Users/kpanwar/Desktop/Machine Learning A-Z Template Folder/codetest_pricevol_5yr.csv")


def month_base_seggregation(date_column_name):
    df['month']=pd.to_datetime(df[date_column_name]).dt.month
    df['year']= pd.to_datetime(df[date_column_name]).dt.year
    
    final_table=pd.pivot_table(df, index=['month','year'], values=['open','high','low','close','volume'],
              aggfunc=np.sum)
    final_table.columns=['open','high','low','close','volume']
    return final_table


# In[ ]:


#Question number Two:  Calculate 18-day, 50-day and 100-day exponential moving averages
df1=final_table.rolling(18, min_periods=1)['open','close','high','low','volume'].mean()
df2= final_table.rolling(50, min_periods=1)['open','close','high','low','volume'].mean()
df3= final_table.rolling(100, min_periods=1)['open', 'close','high','low','volume'].mean()


# In[1]:


from ipywidgets import interact
from scipy.stats import spearmanr
def takeinput(c1,c2):
    print(c1,c2)
    cnd="Name=='"+c1+"'"
    print(cnd)
    cl1=df.query(cnd)['close']
    cnd="Name=='"+c2+"'"
    print(cnd)
    cl2=df.query(cnd)['close']
    print(spearmanr(cl1,cl2))
    print(np.corrcoef)

