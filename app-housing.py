import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('Califorlia Housing Data (1990) by Yanqi Yu')
df = pd.read_csv('housing.csv')

housing_filter = st.slider('Minimal Median House Price):', 0, 500001, 200000)

location_filter = st.sidebar.multiselect( 'Choose the location type', df.ocean_proximity.unique(),  df.ocean_proximity.unique())

income_filter = st.sidebar.radio(
    label='Choose income level',
    options=('Low', 'Medium', 'High'),
)

df = df[df.median_house_value >= housing_filter]

df = df[df.ocean_proximity.isin(location_filter)]

if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[df.median_income <= 4.5]
elif income_filter == 'High':
    df = df[df.median_income > 4.5]
else:
    pass

st.subheader('See more filters in the sidebar:')
st.map(df)

st.subheader('Histogram of the Median House Value:')
fig, ax = plt.subplots(figsize=(15,10))
df.median_house_value.hist(bins=30)
st.pyplot(fig)

