#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import joblib
import pandas as pd
from PIL import Image


# In[2]:


#@st.cache(allow_output_mutation=True)
@st.cache_data
def load(model_path):
    df = pd.read_pickle(model_path)
    return df


# In[4]:


loaded_model=joblib.load('similarities.joblib')


# In[5]:


new_df=pd.read_csv('data.csv')


# In[7]:

list_1=[]
def recommend(anime):
    movie_index = new_df[new_df['Name'] == anime].index[0]
    distances = loaded_model[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:15]
    for i in movies_list:
        list_1.append(new_df.iloc[i[0]].Name)    
    df_result=pd.DataFrame(list_1)
    return df_result


# In[8]:


#recommend("Shingeki no Kyojin")


# In[9]:


st.title('Anime Recommendation App')
st.write('Based on your favs we will give you another 10 anime to binge watch')
image = Image.open('image.png')


# In[10]:


st.image(image, use_column_width=True)
dataframe = load('models/df.zip')


# In[11]:


option = st.selectbox('Please select your favorite anime', (dataframe.columns))

st.write('You selected:', option)

if (st.button('Get Recommendation')):
    # dataframe = load('../models/df.pkl')
    result = recommend(option)
    st.write(result.head(10))
    st.balloons()


# In[ ]:




