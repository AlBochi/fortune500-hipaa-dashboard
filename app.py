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
    "Quarter": ["Q3 2024", "Q4 2024", "Q1 2025", "Q2 2025"],
    "Score": [68, 75, 82, 88]
})
fig = px.line(trend_data, x="Quarter", y="Score", markers=True, title="HIPAA Compliance Progress")
st.plotly_chart(fig, use_container_width=True)

# Control status table
st.subheader("Control Status Overview")
st.dataframe(df, use_container_width=True, hide_index=True)

# Control detail view
st.subheader("🔍 Control Detail Explorer")
selected_control = st.selectbox("Select HIPAA Control", df["Control"].unique())
row = df[df["Control"] == selected_control].iloc[0]

cols = st.columns([1, 2])
with cols[0]:
    st.metric("Current Status", row['Status'])
    st.metric("Control Owner", row['Owner'])
    st.metric("Severity", row['Severity'])

with cols[1]:
    st.write(f"**Last Reviewed:** {row['Last Reviewed']}")
    st.write(f"**Systems Affected:** {row['Systems Affected']}")
    with open(row["Evidence"], "rb") as file:
        st.download_button("📄 Download Evidence Package",
                           file,
                           file_name=f"{selected_control.replace('.', '_')}_evidence.pdf")

    if row['Status'] != '✅':
        st.warning("Remediation Required")
        st.progress(30, text=f"Remediation progress for {selected_control}")
        st.write("**Action Plan:**")
        st.markdown("""
        - [ ] Update IAM policies by 2025-07-15
        - [ ] Conduct access review by 2025-07-20
        - [ ] Validate encryption settings
        """)

# Auditor notes section
st.divider()
with st.expander("Auditor Notes"):
    st.text_area("Internal Observations",
                 "Access control exceptions detected in AWS us-east-1. Temporary admin permissions not rotated per policy NHS-AC-2025. Requires remediation before final audit.")
    st.caption("Last updated: 2025-07-09 by jsmith@healthcare.org")

# Footer
st.divider()
st.caption("© 2025 Confidential Healthcare Provider - Audit Dashboard | Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M"))

