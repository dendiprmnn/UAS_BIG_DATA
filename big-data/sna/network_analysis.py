import pandas as pd
import networkx as nx

twitter = pd.read_csv("../data/twitter_clean.csv")

keywords = ["bpjs", "rumah sakit", "pelayanan", "antrian"]

edges = []

for _, row in twitter.iterrows():
    user = row["username"]
    text = row["clean_text"]

    for kw in keywords:
        if kw in text:
            edges.append([user, kw])

# Simpan edge list
df_edges = pd.DataFrame(edges, columns=["source", "target"])
df_edges.to_csv("../data/sna_edges.csv", index=False)

print("File sna_edges.csv berhasil dibuat")
