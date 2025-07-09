import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page config
st.set_page_config(
    page_title="HIPAA Compliance Dashboard",
    page_icon="🏥",
    layout="wide"
)

# Load control data
@st.cache_data
def load_data():
    return pd.read_csv("controls.csv")

df = load_data()

# Title and header
st.title("🏥 HIPAA Compliance Dashboard - Fortune 500 Healthcare Provider")
st.caption("Q2 2025 Audit Cycle | AWS + GCP Environments | Dashboard v2.1.4")

# Compliance KPI cards
col1, col2, col3 = st.columns(3)
compliant = df[df['Status'] == '✅'].shape[0]
non_compliant = df[df['Status'] == '❌'].shape[0]
total = df.shape[0]
col1.metric("Compliance Score", f"{int(compliant / total * 100)}%", "↑ from last quarter")
col2.metric("Critical Controls", "92% Compliant", "⚠️ 3 need remediation")
col3.metric("Audit Readiness", "28/45 Days", "✔ 65% complete")

# Trend chart
st.subheader("📈 Compliance Trend")
trend_data = pd.DataFrame({
    "Q

