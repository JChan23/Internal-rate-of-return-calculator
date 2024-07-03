#libraries
import pandas as pd
import numpy as np

#lists to store data from excel sheet
years = []
deposits = []
withdrawals = []
net_cashflow = []

#import excel sheet
#excel = input('Input excel sheet location: ') # C:\Users\User\Wealth_Status.xlsx
data = pd.read_excel(r'C:\Users\User\Wealth_Status.xlsx')
data = data.fillna(0)
print(data)

count_row = data.shape[0] #Number of rows
count_col = data.shape[1] #Number of columns

#transfer data from dataframe into arrays
for i in range(count_row):
    years.append(data.iloc[i, 0])
    deposits.append(data.iloc[i, 1])
    withdrawals.append(data.iloc[i, 2])
    net_cashflow.append(deposits[i] - withdrawals[i])

#calculate IRR via fixed point iteration
IRR1 = 0.2
IRR2 = 0
count = 0
total = 0
first_constant = -(net_cashflow[0]+net_cashflow[1])/(net_cashflow[0])
while round(IRR1, 4) != round(IRR2, 4):
    IRR2 = IRR1
    total = first_constant
    for i in range(count_row-2):
        total = total + net_cashflow[i+2]/(-net_cashflow[0]*(1+IRR1)**(i+1))
    IRR1 = total
print('')
print(f'IRR for this portfolio = {round(IRR1, 4)*100}%')
