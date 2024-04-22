#!/usr/bin/env python
# coding: utf-8

# # US Accidents Exploratory Data Analysis
# 
# TODO - talk about EDA
# 
# TODO - talk about the dataset (source, what it contains, how it will be useful)
# 
# - Kaggle
# 
# - informaiton about accidents
# 
# - can use useful to prevent accidents
# 
# - mention that this does not contain data about New York
# 
# 

# In[2]:


import opendatasets as od

download_url = 'https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents'

od.download(download_url)


# In[3]:


data_filename = './us-accidents/US_Accidents_March23.csv'


# # Data Preparation and Cleaning
# 
# 1.Load the file using Pandas
# 
# 2.Look at some information about the data & the columns
# 
# 3.Fix any missing or incorrect values

# In[4]:


import pandas as pd


# In[5]:


df = pd.read_csv(data_filename)


# In[6]:


df


# In[8]:


df.columns


# In[9]:


df.info()


# In[10]:


df.describe()


# In[11]:


df.describe(include ='object')


# In[12]:


df.shape


# In[13]:


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

numeric_df = df.select_dtypes(include=numerics)
len(numeric_df.columns)


# In[14]:


missing_percentage = df.isna().sum().sort_values(ascending= False)/len(df)
missing_percentage


# In[15]:


missing_percentage[missing_percentage != 0]


# In[16]:


type(missing_percentage)


# In[15]:


missing_percentage[missing_percentage != 0].plot(kind='barh')


# - Remove columns that you don't want to use

# ## Exploratory Data Analysis and Visulization
# 
# Columns we'll analyze
# 
# - City
# - State
# - Start Time
# - Start Lat
# - Start Lag
# - Temprature
# - Weather Condition
# 

# In[16]:


df.columns


# ###  Analysis for City

# In[17]:


df.City


# In[18]:


df.City.unique()


# In[19]:


Unique_cities = df.City.unique()
len(Unique_cities)


# In[20]:


cities_by_accident = df.City.value_counts()
cities_by_accident


# In[21]:


'New York' in df.City


# In[22]:


cities_by_accident[:20]


# In[23]:


type(cities_by_accident)


# In[24]:


cities_by_accident[:20].plot(kind = 'barh')


# In[25]:


import seaborn as sns
sns.set_style("darkgrid")


# In[26]:


sns.distplot(cities_by_accident)


# In[27]:


# log_scale = True plot is more clear visible no of accident in cities
sns.histplot(cities_by_accident, log_scale = True)


# In[28]:


cities_by_accident[cities_by_accident == 1]


# In[29]:


high_accident_cities = cities_by_accident[cities_by_accident>=1000]
low_accident_cities  = cities_by_accident[cities_by_accident<1000]


# In[78]:


len(high_accident_cities)/ len(cities_by_accident)


# - 8.9% cities high accidents

# In[31]:


len(low_accident_cities)/len(cities_by_accident)


# - 91% cities low accidents

# In[32]:


sns.distplot(high_accident_cities)


# In[33]:


sns.distplot(low_accident_cities)


# ###  Analysis for Start Time

# In[34]:


df.Start_Time


# In[35]:


df.Start_Time[0]


# In[36]:


df['Start_Time'] = pd.to_datetime(df['Start_Time'])


# In[37]:


df.dtypes


# In[38]:


df.Start_Time[0]


# In[43]:


#(norm_hist = True use to convert into percentage)
sns.distplot(df.Start_Time.dt.hour, bins = 24, kde = False,norm_hist = True , color = 'red')
            


# What time of the day are accidents most frequent in?
# 
# - A high percentage of accidents occur between 7 am to 8 am (probably people in a hurry to get to work)
# - Next higest percentage is 3 pm to 5 pm.

# In[50]:


sns.distplot(df.Start_Time.dt.dayofweek, bins = 7, kde = False,norm_hist = True, color = 'blue')


#  IS distribution of accidents by hour the same on weekends as on weekdays

# In[53]:


# dayofweek == 6 means sunday
sundays_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 6]
sns.distplot(sundays_start_time.dt.hour, bins = 24, kde = False, norm_hist = True)


# In[54]:


mondays_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 0]
sns.distplot(mondays_start_time.dt.hour, bins = 24, kde = False, norm_hist = True)


# - **On workings i.e. monday, tuesday, wednesday, thurday, friday you'll find almost the same trend in accidents time.
# -  While on saturday and sunday the is a different trend i.e. from 10 am to 7 pm the frequency of accident is more.**

# ## Analysis for Month distribution

# In[55]:


sns.distplot(df.Start_Time.dt.month, bins = 12, kde = False, norm_hist = True, color = 'green')


# - The accidents are high from December and it is lowest at july. The rise continues to increase from the month of July.
# - It's seems during summer there are less accidents but as the winter starts the is a increasing trend in accidents.

# # Analysis for Year

# In[56]:


df.Start_Time.dt.year


# In[59]:


df_2019 = df[df.Start_Time.dt.year == 2019]
sns.distplot(df_2019.Start_Time.dt.month, bins = 12, kde = False, norm_hist = True, color = 'Blue')


# In[62]:


df_2020 = df[df.Start_Time.dt.year == 2020]
sns.distplot(df_2020.Start_Time.dt.month, bins = 12, kde = False, norm_hist = True, color = 'Blue')


# In[61]:


df_2021 = df[df.Start_Time.dt.year == 2021]
sns.distplot(df_2021.Start_Time.dt.month, bins = 12, kde = False, norm_hist = True, color = 'Blue')


# In[63]:


df_2022 = df[df.Start_Time.dt.year == 2022]
sns.distplot(df_2022.Start_Time.dt.month, bins = 12, kde = False, norm_hist = True, color = 'Blue')


# - Much data is missing for yearly analysis 
# - so,need to check some other colunm affected by our study, we can analysis source dataset

# In[64]:


df.Source


# In[72]:


df_2019 = df[df.Start_Time.dt.year == 2019]
df_2019_Source1=df_2019[df_2019.Source == 'Source1']
#sns.distplot(df_2019_Source1.Start_Time.dt.month, bins=12, kde=False,norm_hist = True)
sns.histplot(df_2019_Source1['Start_Time'].dt.month, color='blue', bins=12, stat='percent')


# In[73]:


df_2019 = df[df.Start_Time.dt.year == 2019]
df_2019_Source2=df_2019[df_2019.Source == 'Source2']
#sns.distplot(df_2019_Source2.Start_Time.dt.month, bins=12, kde=False,norm_hist=True)
sns.histplot(df_2019_Source2['Start_Time'].dt.month, color='blue', bins=12, stat='percent')


# In[74]:


df_2019 = df[df.Start_Time.dt.year == 2019]
df_2019_Source3=df_2019[df_2019.Source == 'Source3']
#sns.distplot(df_2019_Source3.Start_Time.dt.month, bins=12, kde=False,norm_hist=True)
sns.histplot(df_2019_Source3['Start_Time'].dt.month, color='blue', bins=12, stat='percent')


# In[46]:


df.Source.value_counts().plot(kind = 'pie')


# - There seems to be some issue with the Source2 and Source3 data so consider excluding Source2 and Source3 **

# ## Start Latitude & Longitude

# In[75]:


df.Start_Lat


# In[76]:


df.Start_Lng


# In[77]:


# use sample function to extract 10% Data
sample_df = df.sample(int(0.1 * len(df)))


# In[80]:


sns.scatterplot(y = sample_df.Start_Lat, x = sample_df.Start_Lng,size = 0.001)


# In[81]:


# show the above Lat & Lng scatter plot in Map (use libraries folium)
import folium


# In[82]:


lat,lon = df.Start_Lng[0],df.Start_Lat[0]
lat,lon


# In[83]:


# sample().iteritems() used to show only 100 results
for x in df[['Start_Lat','Start_Lng']].sample(100).iteritems():
    print(x[1])


# In[84]:


# creat heatmap 
from folium.plugins import HeatMap


# In[85]:


# zip used to pair the both list, it is nescessary to convert list of lat & lng pairs to create heatmap
zip(list(df.Start_Lat),list(df.Start_Lng))


# In[86]:


sample_df = df.sample(int(0.001*len(df)))
lat_lng_pairs = zip(list(df.Start_Lat),list(df.Start_Lng))


# In[87]:


map = folium.Map()
HeatMap(lat_lng_pairs).add_to(map)
map


# # Are there more accidents in warmer or colder areas

# In[93]:


df['Temperature(F)']


# In[94]:


# Create temperature bins (customize according to your data)
bins = [0, 50, 75, 100]
labels = ['Cold', 'Moderate', 'Warm']
# Assign temperature ranges to each row
df['Temperature_Category'] = pd.cut(df['Temperature(F)'], bins=bins, labels=labels, include_lowest=True)
df['Temperature_Category']


# In[95]:


# Group by temperature category and calculate the number of accidents
#accidents_by_temperature = df.groupby('Temperature_Category', observed=False).size().reset_index(name='Accidents')

accidents_by_temperature = df['Temperature_Category'].value_counts()
df['Temperature_Category'].value_counts().plot(kind='pie')


# -  Moderate temperature days more accident happens

# ## Analyzing the data by state 

# In[99]:


states = df['State'].value_counts().head(5)
states
# The data indicates california is the highest accident state 


# In[100]:


sns.barplot(y=states , x = states.index, palette="RdPu")


# ### Summary and Conclusion
#  Insights:
#  
# - The cities with the highest reported accidents are Miami, Houston, Los Angeles, Charlotte, Dallas, Orlando, Austin, Raleigh,     Nashville, Baton Rouge, Atlanta, Sacramento, San Diego, Phoenix, Minneapolis, Richmond, Oklahoma City, Jacksonville, Tucson,     and Columbia.
# - About 8.9% of cities experience a high number of accidents.
# - The majority of cities (91%) have a low number of accidents.
# - Over 1023 cities reported just 1 accident, suggesting the presence of potential outliers that may need to be addressed.
# - There is a notable spike in accidents around 7-8 AM, possibly correlated with morning rush hours and commuting to work or      school.
# - Another spike occurs around 4-5 PM, likely associated with evening rush hours and the return home from work or recreational  activities.
# - On weekdays (Monday to Friday), the trend in accident times is consistent.
# - On weekends (Saturday and Sunday), there is a different trend, with a higher frequency of accidents between 10 AM and 7 PM.
# - There is a seasonal variation in accidents, with fewer incidents during the summer and an increasing trend as winter  approaches.
# - The use of Folium indicates that many people live near bay areas.
# - No data from New York
# - California, Florida, Texas, South Carolina, and New York emerge as the top 5 states with the highest number of accidents
# - Moderate temperature days more accident happens
