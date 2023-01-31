import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import numpy as np

#dash.Dash= The Application
#dash.dcc= Interactive Components
#dash.html= HTML Tags

#Step 1
#We need to load our data into a df and clean it up

df= pd.read_csv(r"C:\Users\SamanthaGrzegorzewsk\pandas_demos\dash_demo\household_median_income_2017.csv")
#print(df.dtypes)
#print(df.columns.dtype)

#trim down our dateframe to the columns we are working with
df_new= df[['State', '2017', '2016', '2015', '2014']]
#print(df_new.head())

#turn the values in each of the year columns into integers *** You change the rest
df_new['2017']= df_new['2017'].str.replace(',', '')
df_new['2017']= df_new['2017'].astype(int)

#delete the first unnecessary row
df_new= df_new.drop(labels= 0, axis=0)
print(df_new.head())


#we are going to make our app

app= Dash(__name__)

#create the layout of our application
#<div>
    ##<h1> I Am A Title </h1>
#</div>
app.layout = html.Div([
    html.H1("Median Income 2014-2017 by State"),

    dcc.Dropdown(id='year_dropdown',
                options=[
                    {'label': 'Samantha', 'value': '2017'},
                    {'label': '2016', 'value': '2016'},
                    {'label': 'Ben', 'value': '2015'},
                    {'label': '2014', 'value': '2014'}],
                multi= False,
                value= '2017', 
                style= {'width': '40%'}
                ),

    dcc.Graph(id='map', figure={})
    
])

if __name__ == '__main__':
    app.run_server(debug=True)