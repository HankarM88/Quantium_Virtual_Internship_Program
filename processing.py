import pandas as pd 
import sys 
# read csv files 
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_1.csv")
# combine the dataframes 
df = pd.concat([df1,df2,df3])
print(df['product'].value_counts())
# filter out for pink morsel products only 
df = df[df['product']=='pink morsel']
# convert prices to numeric values 
df.price = df.price.str.replace('$','', regex=False)
df.price = df.price.astype('float')
# create sales feature from the product of quantity and price 
df['sales'] = df.price * df.quantity 
df = df.drop(['quantity', 'price', 'product'], axis=1)
#rename columns 
df.columns = ['Date', 'Region', 'Sales']
# convert to datetime  
df['Date'] = pd.to_datetime(df['Date'])
# sort by Date 
df = df.sort_values("Date", ascending=True)
# save the dataframe to csv file 
df.to_csv('data/sales.csv', index = False)