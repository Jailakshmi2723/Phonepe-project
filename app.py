import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("📊 PhonePe Insurance Data Analysis Dashboard")

# =========================
# LOAD DATA
# =========================
agg_df = pd.read_csv("aggregated_insurance.csv")
map_df = pd.read_csv("map_insurance.csv")

# If you have top data
try:
    top_df = pd.read_csv("top_insurance.csv")
except:
    top_df = None

# =========================
# KPI SECTION
# =========================
st.subheader("📌 Key Metrics")

total_amount = agg_df["amount"].sum()
total_transactions = agg_df["count"].sum()
avg_transaction = agg_df["amount"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Amount", f"₹ {total_amount:,.0f}")
col2.metric("Total Transactions", f"{total_transactions:,}")
col3.metric("Average Transaction", f"₹ {avg_transaction:,.0f}")

# =========================
# YEAR-WISE & QUARTER-WISE
# =========================
st.subheader("📈 Trends Analysis")

col1, col2 = st.columns(2)

year_data = agg_df.groupby("year")["amount"].sum()
quarter_data = agg_df.groupby("quarter")["amount"].sum()

col1.write("### Year-wise Transactions")
col1.line_chart(year_data)

col2.write("### Quarter-wise Transactions")
col2.bar_chart(quarter_data)

# =========================
# STATE ANALYSIS (MAP DATA)
# =========================
st.subheader("🗺️ State-wise Analysis")

state_data = map_df.groupby("state")["amount"].sum().sort_values(ascending=False)

st.bar_chart(state_data)

# =========================
# TOP ANALYSIS
# =========================
if top_df is not None:
    st.subheader("🏆 Top States")

    top_states = top_df.groupby("state")["amount"].sum().sort_values(ascending=False).head(10)

    st.bar_chart(top_states)

# =========================
# RAW DATA
# =========================
st.subheader("📄 Raw Data")

st.write("Aggregated Data")
st.dataframe(agg_df)

st.write("Map Data")
st.dataframe(map_df)

# TOP ANALYSIS

st.subheader("🏆 Top Performing States")

top_states = top_df.groupby("state")["amount"].sum().sort_values(ascending=False).head(10)

st.bar_chart(top_states)