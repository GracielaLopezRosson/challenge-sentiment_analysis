# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:46:27 2021

@author: graci
"""
import streamlit as st

import pandas as pd

import numpy as np

import pickle

import base64

import seaborn as sns

import matplotlib.pyplot as plt

#Title of the webpage
st.write("""
         ## Welcome to the Twitter Sentiment analysis of your favorite series
         """)

st.write("Available series")
col1, mid, col2 = st.columns([1,1,1000])
with col1:
    st.image('lucifer1.jpg', width=500)
with col2:
    st.image('squid.jpg', width=500)

         
#Side bar options for user selection
def user_input_features():

    pass

df_app = pd.read_csv('df_app.csv')

#***************************************
#Add later twitter exemple
#***************************************

#def user_input_features():

series = st.sidebar.selectbox('Series',('Choose your series','Lucifer','Squid game'))

   # Twitters = st.sidebar.selectbox('PaymentMethod',('Bank transfer (automatic)', 'Credit card (automatic)', 'Mailed check', 'Electronic check'))
number_tweets = st.sidebar.slider('Number of tweets', 1,1400, 1)
    # data = {'gender':[gender], 

    #         'PaymentMethod':[PaymentMethod], 

    #         }


#**********Plots***************
# def countPlot():
#     fig = plt.figure(figsize=(10, 4))
#     
#     fig = sns.countplot(x='sentiment_analysis', data=df_app)
#     st.pyplot(fig)

# countPlot()
#fig = plt.figure(figsize=(10, 4))
fig, ax = plt.subplots()
ax = sns.countplot(x='sentiment_analysis', data=df_app)
#fig.update_layout(title_text="Sentiment Score Histogram", title_x=0.5)
#fig.update_xaxes(title_text='Sentiment score from 1 (negative) to 5 (positive)')
#fig.update_yaxes(title_text='Count')
st.pyplot(fig)
    

    # features = pd.DataFrame(data)

    #return features