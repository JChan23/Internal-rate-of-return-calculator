#libraries
import pandas as pd

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

#calculate IRR via newton raphson
IRR1 = 0.1
IRR2 = 0
total = 0
f_x = 0
f_prime_x = 0
first_constant = -(net_cashflow[0]+net_cashflow[1])/(net_cashflow[0])
while round(IRR1, 4) != round(IRR2, 4):
    IRR2 = IRR1
    #calculate f(x)
    total = first_constant
    for i in range(count_row - 2):
        total = total + net_cashflow[i + 2] / (-net_cashflow[0] * (1 + IRR1) ** (i + 1))
    f_x = total - IRR1

    total = 0
    multiplier = -1
    for i in range(count_row - 2):
        total = total + multiplier*(net_cashflow[i+2])/(-net_cashflow[0])*((1+IRR1)**(-2-i))
    f_prime_x = total - 1
    IRR1 = IRR1 - (f_x/f_prime_x)
print('')
print(f'IRR for this portfolio = {round(IRR1, 4)*100}%')
