import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

DB_USER = os.getenv("POSTGRES_USER", "honeyuser")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "honeypass")
DB_NAME = os.getenv("POSTGRES_DB", "honeypot")
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

st.title("Dashboard Honeypot")

query = """
SELECT id, event_time, src_ip, event_type, username, password, command
FROM cowrie_events
ORDER BY id DESC
LIMIT 200
"""

df = pd.read_sql(query, engine)

st.subheader("Eventos recientes")
st.dataframe(df, use_container_width=True)

if not df.empty:
    st.subheader("Top IPs")
    st.bar_chart(df["src_ip"].value_counts().head(10))

    st.subheader("Tipos de evento")
    st.bar_chart(df["event_type"].fillna("unknown").value_counts())
else:
    st.info("Todavía no hay eventos.")
