#!/usr/bin/env python3
"""
Compliance Summary Reporter v1.0
Generates executive summary from controls.csv
"""

import pandas as pd
from datetime import datetime

def generate_summary():
    df = pd.read_csv("controls.csv")

    total_controls = df.shape[0]
    compliant = df[df["Status"] == "✅"].shape[0]
    non_compliant = df[df["Status"] == "❌"].shape[0]
    needs_attention = df[df["Status"] == "⚠️"].shape[0]

    summary = f"""
    ================================
    📋 HIPAA Compliance Executive Summary
    ================================
    Report Date: {datetime.now().strftime("%Y-%m-%d")}

    Total Controls Monitored : {total_controls}
    ✅ Compliant             : {compliant}
    ⚠️ Needs Attention       : {needs_attention}
    ❌ Non-Compliant         : {non_compliant}

    Compliance Score         : {round((compliant / total_controls) * 100)}%
    ================================
    """
    print(summary)

if __name__ == "__main__":
    generate_summary()
