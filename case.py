import pandas as pd

df_cus = pd.read_excel('/Users/ice/Desktop/CASE/TCT- Data Analyst Test.xlsx', sheet_name='Customer')
df_sell = pd.read_excel('/Users/ice/Desktop/CASE/TCT- Data Analyst Test.xlsx', sheet_name='Seller')
df_raw = pd.read_excel('/Users/ice/Desktop/CASE/TCT- Data Analyst Test.xlsx', sheet_name='Raw tracking of seller')

df_cus.drop(df_cus.columns[6:39], axis=1, inplace=True)
print(df_cus.info())
print(df_sell.info())
print(df_raw.info())


# raw data

df_raw['diff_c_s'] = df_raw['Case Solved Date'] - df_raw['Case Created Date']
df_raw['diff_s_sb'] = df_raw['CSAT Submission date'] - df_raw['Case Solved Date']

print(df_raw.head())