import streamlit as st
import pandas as pd

df = pd.read_csv("aggregated_insurance.csv")

st.title("PhonePe Insurance Data Analysis")

st.subheader("Raw Data")
st.write(df)

st.subheader("Year-wise Transaction Amount")
year_data = df.groupby("year")["amount"].sum()
st.bar_chart(year_data)

st.subheader("Quarter-wise Transaction Amount")
quarter_data = df.groupby("quarter")["amount"].sum()
st.bar_chart(quarter_data)