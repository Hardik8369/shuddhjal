import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import spacy
from wordcloud import WordCloud
import warnings

original_df = pd.read_csv("C:\\Users\\WELCOME\\Downloads\\archive\\Water_pond_tanks_2021.csv", encoding='latin1')
original_df.head()
original_df.info()
original_df=original_df.replace('-', np.nan)
original_df=original_df.replace('\n4', '',regex=True)
original_df=original_df.replace('\n', ' ',regex=True)
original_df.iloc[:,4:20]=original_df.iloc[:,4:20].astype(float)
original_df.info()
original_df.isnull().sum()
df=original_df.copy(deep=True)
df_type_wb = df.dropna(subset=['Type Water Body'])
colors_10 = ['DarkRed', 'FireBrick','Red', 'Crimson', 'IndianRed', 'slategray', 'gray', 'dimgrey', 'DarkSlateGrey', 'black']
water_bodies_list = df_type_wb['Type Water Body'].str.split(',') #split the list into names
wb_type_list = {} #create an empty list
for types in water_bodies_list: # for any names in series_gen_list
    for type in types: # for any genre in genres
        if (type in wb_type_list): #if this genre is already present in the s_gen_list
            wb_type_list[type]+=1 # increase his value
        else:  # else
            wb_type_list[type]=1 # Create his index in the list
wb_type_df = pd.DataFrame(wb_type_list.values(),index = wb_type_list.keys(),
                        columns = {'Counts of types of water bodies'}) #Create a s_gen_df
wb_type_df.sort_values(by = 'Counts of types of water bodies',ascending = False,inplace = True) #Sort the dataframe in ascending order
top_10_wb_type = wb_type_df[0:10]
fig = go.Figure(data=[go.Bar(
    x = top_10_wb_type.index,
    y = top_10_wb_type['Counts of types of water bodies'],
    text = top_10_wb_type['Counts of types of water bodies'],
    textposition='auto',
    marker_color=colors_10
)])
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(title_text= 'How many different types of water bodies are available?',
                  uniformtext_minsize=8, uniformtext_mode='hide',
                  yaxis=dict(
                  title='Quantity',
                  titlefont_size=14),
                  xaxis=dict(
                  title='Types of water bodies',
                  titlefont_size=14))
df_states = df.dropna(subset=['State Name'])
ax= px.treemap(df_states,path=["State Name"])
ax.show()
df = df.dropna(subset=['Temperature\n?C (Min)', 'Temperature\n?C (Min)'])
df = df.loc[(df['Temperature\n?C (Min)'] >= 20)]
df = df.loc[(df['Temperature\n?C (Max)'] <= 30)]
df.head()
df = df.dropna(subset=['Dissolved Oxygen (mg/L) (Min)', 'Dissolved Oxygen (mg/L) (Max)'])
df = df.loc[(df['Dissolved Oxygen (mg/L) (Min)'] >= 4)]
df = df.loc[(df['Dissolved Oxygen (mg/L) (Max)'] <= 8)]
df.head()
df = df.dropna(subset=['pH (Min)', 'pH (Max)'])
df = df.loc[(df['pH (Min)'] >= 6)]
df = df.loc[(df['pH (Min)'] <= 8)]
df.head()
df = df.dropna(subset=['Conductivity (?mhos/cm) (Min)', 'Conductivity (?mhos/cm) (Max)'])
df = df.loc[(df['Conductivity (?mhos/cm) (Min)'] >= 150)]
df = df.loc[(df['Conductivity (?mhos/cm) (Max)'] <= 500)]
df.head()
df = df.dropna(subset=['BOD (mg/L) (Min)', 'BOD (mg/L) (Max)'])
df = df.loc[(df['BOD (mg/L) (Max)'] <= 5)]
df.head()
df = df.dropna(subset=['Nitrate N + Nitrite N(mg/L) (Min)', 'Nitrate N + Nitrite N(mg/L) (Max)'])
df = df.loc[(df['Nitrate N + Nitrite N(mg/L) (Max)'] <= 5.5)]
df.head()
df = df.dropna(subset=['Fecal Coliform (MPN/100ml) (Min)', 'Fecal Coliform (MPN/100ml) (Max)'])
df = df.loc[(df['Fecal Coliform (MPN/100ml) (Max)'] <= 200)]
df.head()
df = df.dropna(subset=['Total Coliform (MPN/100ml) (Min)', 'Total Coliform (MPN/100ml) (Max)'])
df = df.loc[(df['Total Coliform (MPN/100ml) (Max)'] <= 500)]
df.head()
df.info()
df['State Name'].value_counts()[:20].plot(kind='bar', color=['DarkRed', 'FireBrick','Red', 'Crimson', 'IndianRed', 'slategray', 'gray', 'dimgrey', 'DarkSlateGrey', 'black'])
plt.title("State with the best water quality")
plt.show()
df['Type Water Body'].value_counts()[:20].plot(kind='bar', color=['DarkRed', 'FireBrick','Red', 'Crimson', 'IndianRed', 'slategray', 'gray', 'dimgrey', 'DarkSlateGrey', 'black'])
plt.title("Type of water body with the best water quality")
plt.show()
new_df=original_df.copy(deep=True)
new_df = new_df.dropna(subset=['Dissolved Oxygen (mg/L) (Min)', 'Dissolved Oxygen (mg/L) (Max)', 'Temperature\n?C (Min)', 'Temperature\n?C (Min)'])
new_df.plot(x="State Name", y=["Dissolved Oxygen (mg/L) (Max)", "Temperature\n?C (Min)"],
        kind="line", figsize=(10, 10))
plt.title("Dissovled oxygen vs Temperature")
plt.show()
new_df = new_df.dropna(subset=['Dissolved Oxygen (mg/L) (Min)', 'Dissolved Oxygen (mg/L) (Max)', 'Nitrate N + Nitrite N(mg/L) (Min)', 'Nitrate N + Nitrite N(mg/L) (Max)'])
new_df.plot(x="State Name", y=["Dissolved Oxygen (mg/L) (Max)", "Nitrate N + Nitrite N(mg/L) (Min)"],
        kind="area", figsize=(10, 10))
plt.title("Dissovled oxygen vs (Nitrate N + Nitrite)")
plt.show()