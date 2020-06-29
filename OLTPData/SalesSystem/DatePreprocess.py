#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df_sale=pd.read_excel('Sale.xlsx')


# In[3]:


import datetime
now=datetime.datetime.now()
for i in range(len(df_sale['Date'])):
    if type(df_sale['Date'][i]) is datetime.datetime:
        stamp=df_sale['Date'][i]
        stamp=stamp.strftime('%m-%d-%Y')
        stamp=datetime.datetime.strptime(stamp,'%d-%m-%Y')
        df_sale['Date'][i]=stamp.strftime('%d-%m-%Y')
    else:
        try:
            stamp=datetime.datetime.strptime(df_sale['Date'][i],'%d/%m/%Y')
            df_sale['Date'][i]=stamp.strftime('%d-%m-%Y')
        except:
            wrong_date_time_correct=df_sale['Date'][i].replace(df_sale['Date'][i][:2],str(int(df_sale['Date'][i][:2])-1))
            stamp=datetime.datetime.strptime(wrong_date_time_correct,'%d/%m/%Y')
            df_sale['Date'][i]=stamp.strftime('%d-%m-%Y')


# In[4]:


df_sale.to_excel('Sale_fix.xlsx',index=None)


# In[ ]:




