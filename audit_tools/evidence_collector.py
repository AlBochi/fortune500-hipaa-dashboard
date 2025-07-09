#!/usr/bin/env python3
"""
HIPAA Evidence Collector v1.2
Simulates automated evidence gathering from AWS/GCP environments
"""

import time

def collect_aws_evidence():
    print("[+] Collecting AWS Config compliance data...")
    time.sleep(1)  # Simulate time delay
    print("[+] AWS evidence collected.")

def collect_gcp_evidence():
    print("[+] Collecting GCP Security Scanner data...")
    time.sleep(1)
    print("[+] GCP evidence collected.")

if __name__ == "__main__":
    collect_aws_evidence()
    collect_gcp_evidence()
