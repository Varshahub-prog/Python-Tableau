# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:50:37 2024

@author: Varsha
"""

import pandas as pd
# filename = pd.read_csv('file.csv')
data = pd.read_csv('transaction2.csv')
data = pd.read_csv('transaction2.csv',sep = ';')
data.info()
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem
SalesPerTransaction = NumberofItemsPurchased*SellingPricePerItem

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem*NumberofItemsPurchased
SellingPricePerItem = data['SellingPricePerItem']

# adding a new column to a data frame
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#sales per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitPerTransaction'] = data ['SalesPerTransaction'] - data['CostPerTransaction']

# markup calculation

data['Markup'] = (data ['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']
data['Markup'] = (data['ProfitPerTransaction'])/data['CostPerTransaction']
roundmarkup = round(data['Markup'],2)
data['Markup'] = round(data['Markup'],2)
# Combining date fields
my_name = 'varsha'+'Ala'
my_date = 'Day'+'-'+'Month'+'-' +'Year'
#print(d.type(data['Day']))
# mydate = 'Day'+'-'+data['Month']+'-'+'Year'
#my_date = data['Day']+'-'

# Checking columns type
print(data['Day'].dtype)

# Change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day +'-'+data['Month']+'-'+year

data['date'] = my_date


# data['mydate'] = (data['Day'].astype(str)+'-'+ data['Month']+'-' + data['Year'].astype(str))
data.iloc[0] # views the rows with index = 0
data.iloc[0:3] # first 3 rows
data.iloc[-5:] # last 5 rows
data.head(5) # brings in first 5 rows
data.iloc[:,2] # brings in all rows on the 2nd column
data.iloc[4,2] # brings in 4th row, 2nd column
split_col = data['ClientKeywords'].str.split(',',expand = True)
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['Length of contract'] = split_col[2]
#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[',' ')
data['Length of contract'] = data['Length of contract'].str.replace(']',' ')

# data.drop('Lengthof contract',axis =1, inplace = True)

# using lower function
data['ItemDescription'] = data['ItemDescription'].str.lower()
# how to merge the files
# bringing a new data set
seasons = pd.read_csv('value_inc_seasons.csv',sep = ';')

data = pd.merge(data,seasons, on  = 'Month') 

data.drop('ClientKeywords', axis = 1, inplace = True)
data = data.drop('Day',axis = 1)
data = data.drop(['Month','Year'],axis = 1)
# to export csv file
data.to_csv('ValueInc_Cleaned.csv',index = False)
