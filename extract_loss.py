# -*- coding: utf-8 -*-
#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_rows = None

'''
Question 1: Data Extraction

Instructions:
1. Extract "loss circulation" value from the activity memo of the given dataset
2. Name the column containing the extracted values "LOSS_CIRCULATION"
3. Concatenate the new column to the dataset and save to a csv file named "loss-circulation-transformed.csv"

Extraction Logics:
- Locate the keyword "loss" in "DM_ACTIVITY.activity_memo" column.
- The numeric in (m3) unit that follows are the value to be extracted.
- In case of absence, loss circulation value should defalut to zero.
'''
print('=========== Question 1: Data Extraction ===========')

# Read File loss-circulation.csv
FILE_NAME = 'loss-circulation.csv'

df = pd.read_csv(FILE_NAME)
df.dropna(inplace=True)
df_new = df.copy()

# Resize Text Lower all
df['DM_ACTIVITY.activity_memo'] = df['DM_ACTIVITY.activity_memo'].str.lower()

# - Locate the keyword "loss" in "DM_ACTIVITY.activity_memo" column.
df_new['LOSS_CIRCULATION'] = df[df['DM_ACTIVITY.activity_memo'].str.contains('loss.+?m3', na=False)]['DM_ACTIVITY.activity_memo']
print('- Locate the keyword "loss" in "DM_ACTIVITY.activity_memo" column.')
print(df_new['LOSS_CIRCULATION'].head(3))
print('-----------------------------------------------------------------------------------------')

# - In case of absence, loss circulation value should defalut to zero.
df_new.fillna(0,inplace=True)
print('- In case of absence, loss circulation value should defalut to zero.')
print(df_new.head(3))
print('-----------------------------------------------------------------------------------------')

# Not selected word 'no loss' and 'no losses'
df_new['LOSS_CIRCULATION'] = df_new['LOSS_CIRCULATION'].str.extract('[^o].loss(es)? (.+?) m3[^/]')[1]

# LOSS_CIRCULATION to list 
df_new['LOSS_CIRCULATION'] = df_new['LOSS_CIRCULATION'].str.split()

# - In case of absence, loss circulation value should defalut to zero.
df_new['LOSS_CIRCULATION'].fillna('0',inplace=True)

# - The numeric in (m3) unit that follows are the value to be extracted.
df_new['LOSS_CIRCULATION'] = df_new['LOSS_CIRCULATION'].apply(lambda x: x[-1])
print('- The numeric in (m3) unit that follows are the value to be extracted.')
print(df_new['LOSS_CIRCULATION'].head(3))
print('-----------------------------------------------------------------------------------------')

# Replace column LOSS_CIRCULATION Text '(' to ''
df_new['LOSS_CIRCULATION'] = df_new['LOSS_CIRCULATION'].str.replace('(','')

# Override df_new['LOSS_CIRCULATION'] to df['LOSS_CIRCULATION']
df['LOSS_CIRCULATION'] = df_new['LOSS_CIRCULATION']

# df.to_csv('loss-circulation-transformed.csv')
print('Status Created file loss-circulation-transformed.csv :D: Success!')
print('-----------------------------------------------------------------------------------------')

# '''
# Question 2: Data Profiling

# Answer the following questions
# - What are the some basic statistics (avg, var, max, min, %missing) of loss circulation?
# - Using visualization tools of choice, plot the distribution of loss circulation.
# - What are the top 3 activity codes from which loss circulation occurs the most?

# '''
print('=========== Question 2: Data Profiling ===========')

FILE_NAME = 'loss-circulation-transformed.csv'

df = pd.read_csv(FILE_NAME, encoding='cp1252', index_col=0)
df.dropna(inplace=True)

df.drop('DM_EVENT.date_ops_start', axis=1, inplace=True)
df.drop('DM_ACTIVITY.activity_memo', axis=1, inplace=True)

df.set_index('DM_ACTIVITY.activity_code', inplace=True)
df_new = df.loc[(df!=0).any(1)]

# - What are the some basic statistics (avg, var, max, min, %missing) of loss circulation?
statistics = df_new.describe()
print('- What are the some basic statistics (avg, var, max, min, %missing) of loss circulation?')
print(statistics)
print('-----------------------------------------------------------------------------------------')

# - Using visualization tools of choice, plot the distribution of loss circulation.
count_activity_code = df_new.pivot_table(index=['DM_ACTIVITY.activity_code'], values=['LOSS_CIRCULATION'], aggfunc='size').reset_index().rename(columns={0: 'LOSS_CIRCULATION'})
count_activity_code.plot(kind='bar', x='DM_ACTIVITY.activity_code', y='LOSS_CIRCULATION', title='COUNT LOSS CIRCULATION')
print('- Using visualization tools of choice, plot the distribution of loss circulation.')
print(count_activity_code)
print('-----------------------------------------------------------------------------------------')

# - What are the top 3 activity codes from which loss circulation occurs the most?
count_activity_code.set_index('DM_ACTIVITY.activity_code', inplace=True)
top_3 = (count_activity_code.nlargest(3, ['LOSS_CIRCULATION'])).to_dict()
print('- What are the top 3 activity codes from which loss circulation occurs the most?')
for k, v in top_3['LOSS_CIRCULATION'].items():
	print(str(k) + ": "+ str(v))
plt.show()
print('======== END ========')
