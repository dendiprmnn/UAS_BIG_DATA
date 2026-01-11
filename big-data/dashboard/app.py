import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analisis Pelayanan Publik", layout="wide")

st.title("📊 Dashboard Analisis Pelayanan Publik")
st.markdown("""
Dashboard ini menyajikan hasil integrasi data pelayanan publik dari data pemerintah
dan opini publik media sosial menggunakan pendekatan Big Data.
""")

# =====================
# LOAD DATA
# =====================
twitter = pd.read_csv("../data/twitter_sentiment.csv")
edges = pd.read_csv("../data/sna_edges.csv")

# =====================
# FILTER
# =====================
st.sidebar.header("🔍 Filter Data")
sentiment_filter = st.sidebar.selectbox(
    "Pilih Sentimen",
    ["Semua", "Positif", "Negatif"]
)

if sentiment_filter != "Semua":
    twitter = twitter[twitter["sentiment"] == sentiment_filter]

# =====================
# KPI SECTION
# =====================
st.subheader("📌 Ringkasan Sentimen Publik")

total = len(twitter)
positif = len(twitter[twitter["sentiment"] == "Positif"])
negatif = len(twitter[twitter["sentiment"] == "Negatif"])

col1, col2, col3 = st.columns(3)
col1.metric("Total Tweet", total)
col2.metric("Sentimen Positif", positif)
col3.metric("Sentimen Negatif", negatif)

# =====================
# SENTIMENT CHART
# =====================
st.subheader("📈 Distribusi Sentimen")

sentiment_count = twitter["sentiment"].value_counts()

col4, col5 = st.columns(2)

with col4:
    st.bar_chart(sentiment_count)

with col5:
    fig1, ax1 = plt.subplots()
    ax1.pie(
        sentiment_count,
        labels=sentiment_count.index,
        autopct="%1.1f%%",
        startangle=90
    )
    ax1.axis("equal")
    st.pyplot(fig1)

# =====================
# DATA TABLE
# =====================
st.subheader("📝 Data Tweet")
st.dataframe(twitter[["username", "tweet_text", "sentiment"]])

# =====================
# SNA SECTION
# =====================
st.subheader("🌐 Social Network Analysis (SNA)")

G = nx.from_pandas_edgelist(edges, "source", "target")

fig2, ax2 = plt.subplots(figsize=(8, 6))
nx.draw(
    G,
    with_labels=True,
    node_size=1500,
    font_size=8,
    ax=ax2
)
st.pyplot(fig2)
