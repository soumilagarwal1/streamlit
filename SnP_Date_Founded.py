import yfinance as yf
import pandas as pd
import re
import streamlit as st

st.write("""
# S&P 500 Companies' founding date
""")

df_final = pd.DataFrame(columns = ['Date_Founded'])

df_2 = pd.read_csv("Book2.csv")
a = df_2["Symbol"].to_list()
df_final['Date_Founded'] = df_2["Founded"].to_list()
for index, row in df_final.iterrows():
    date = row['Date_Founded']
    r = re.findall('[0-9]+', date)
    if len(r) > 1:
       r = [int(i) for i in r]
       row['Date_Founded'] = min(r)
    
df_final.index = a

st.dataframe(df_final)
# count = 0

# for at in a:  
#     print("Working on", at)
#     ata = yf.Ticker(at)
    
    
#     df = ata.financials
    
#     try:
#         op_inc = df.loc['Operating Income'].iat[1]
#         df_final.loc[at, 'Operating_Income'] = op_inc
#     except:
#         print("Operating Income not found")
#         count += 1  
 
    
#     dff = ata.balance_sheet
    
#     try:
#         net_ppe = dff.loc['Property Plant Equipment'].iat[1]
#         df_final.loc[at, 'Net_PPE'] = net_ppe
#     except:
#         print("Net PPE not found")
#         count += 1
    
#     try:
#         tot_ass = dff.loc['Total Assets'].iat[1]
#         df_final.loc[at, 'Total_Assets'] = tot_ass
#     except:
#         print("Total Assets not found")
#         count+= 1
        
#     try:    
#         lt_debt = dff.loc['Long Term Debt'].iat[1]
#         df_final.loc[at, 'Long_Term_Debt'] = lt_debt
#     except:
#         print('Long Term Debt not found')
#         count += 1
# # net ppe, total assets, operating income, total debt, date founded

# print(count)
df_final.to_csv('S&P_500_Data.csv')
