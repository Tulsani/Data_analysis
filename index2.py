import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/avocado.csv')
# here we reassign Date coloum back to Date using pandas function
df['Date']= pd.to_datetime(df["Date"])
albany_df=df[df["region"]=="Albany"]
albany_df=albany_df.set_index("Date")

#unable to plot using .plot() function
albany_df["AveragePrice"].plot()
plt.show()
#sothing the graph using moving average
albany_df['AveragePrice'].rolling(25).mean().plot()
plt.show()
#still not good
#we need to maitain index in proper order
albany_df.sort_index(inplace=True)
print(albany_df)
print(albany_df['AveragePrice'].rolling(25).mean().plot())

#plot() function allows plot the graph

#we can using the rolling mean as a coloum if we want
#custome coloum added to our data frame which is 'price25ma'
albany_df['price25ma']=albany_df['AveragePrice'].rolling(25).mean()
#for first intial values we see NaN beacuse we need atleast 25 values to
#calculate rolling mean , first 25 values would be NaN
print(albany_df.head())
#to see the effective of rolling mean
print(albany_df.tail())
#we can remove the removes the value NaN values containing rows
#helps drop missing data , u can update it as new data frame as dropna(inplace=True)
print(albany_df.dropna().head(3))
#to generarete a copy dataframe. we use
albany_df=df.copy()[df["region"]=="Albany"]
#converting two an array
print(df.values)
print(df['region'].values.tolist())
#to get uniquw values we convert it to a set
unique_list=set(df["region"].values.tolist())
#to iterative to it over like a list
print(list(set(df["region"].values.tolist())))
#simpler way availabe in pandas is , helps print all unique regions in the csv
print(df['region'].unique())
print(df['year'].unique())

#using matplotlib to print every
graph_df=pd.DataFrame()

for region in df['region'].unique()[:16]:
    print(region)
    region_df = df.copy()[df['region']==region]
    region_df.set_index("Date",inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f'{region}_price25ma'] = region_df['AveragePrice'].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f'{region}_price25ma']]
    else:
        #join is used to join multiple dataframes that have the same index
        #here we had a problem that for all region we had a the same  name
        #to solve this we use f string and append the region name to all the
        #different region for which we calculate the rolling mean of 25
        graph_df=graph_df.join(region_df[[f'{region}_price25ma']])

print(graph_df.tail())
graph_df.plot()
plt.show()
