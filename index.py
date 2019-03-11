import pandas as pd
import matplotlib.pyplot as plt

#convention to call dataframe df
df=pd.read_csv("dataset/avocado.csv")
print(df)
#finding head n tail of dataset
print(df.head(4))
print(df.tail(3))
#refering specific coloums
print(df["AveragePrice"])
print(df["AveragePrice"].head())
#we can also metion coloum name as df.AveragePrice.head()

#creating new dataframe for where region is specific
#below we find just Albany region prices for Avocado
albany_df=df[df['region']=="Albany"]
print(albany_df.head())

albany_df.index

#to have meaninful index
albany_df.set_index("Date")
# set_index() returns a new dataframe so we need to resign it so make it  work
print(albany_df.head())
albany_df=albany_df.set_index("Date")
print(albany_df.head())
#another way to make it work is  make inplace True
# albany_df.set_index("Date",inplace=True)
# print(albany_df.head())

albany_df.plot()
plt.show()
albany_df['AveragePrice'].plot()
plt.show()
