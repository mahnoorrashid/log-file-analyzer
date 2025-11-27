#!/usr/bin/env python3

"""
Simple Log File Analyzer

- Counts total lines
- Counts ERROR / WARNING / INFO entries
- Extracts IP addresses and shows the most common ones
- Shows lines that look like failed login attempts

Author: Mahnoor Rashid
"""

import re
from collections import Counter


def read_log_file(path: str) -> list[str]:
    """Read the log file and return a list of lines."""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"[!] File not found: {path}")
        return []
    except OSError as e:
        print(f"[!] Error reading file: {e}")
        return []


def count_levels(lines: list[str]) -> dict:
    """Count how many lines contain ERROR / WARNING / INFO."""
    levels = {"ERROR": 0, "WARNING": 0, "INFO": 0}

    for line in lines:
        upper = line.upper()
        if "ERROR" in upper:
            levels["ERROR"] += 1
        if "WARNING" in upper:
            levels["WARNING"] += 1
        if "INFO" in upper:
            levels["INFO"] += 1

    return levels


def extract_ips(lines: list[str], top_n: int = 5) -> Counter:
    """
    Extract IPv4 addresses from the log lines and
    return a Counter with the most common ones.
    """
    ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
    ips = []

    for line in lines:
        ips.extend(ip_pattern.findall(line))

    return Counter(ips).most_common(top_n)


def find_failed_logins(lines: list[str], limit: int = 10) -> list[str]:
    """
    Return up to `limit` lines that look like failed login attempts.
    Looks for 'failed' (case-insensitive) in the line.
    """
    failed_lines = []

    for line in lines:
        if "failed" in line.lower():
            failed_lines.append(line.strip())
            if len(failed_lines) >= limit:
                break

    return failed_lines


def main() -> None:
    print("🔎 Simple Log File Analyzer")
    log_path = input("Enter path to log file (e.g. sample.log): ").strip()

    lines = read_log_file(log_path)
    if not lines:
        return

    total_lines = len(lines)
    levels = count_levels(lines)
    common_ips = extract_ips(lines)
    failed_attempts = find_failed_logins(lines)

    print("\n===== SUMMARY =====")
    print(f"Total lines: {total_lines}")
    print(f"ERROR lines:   {levels['ERROR']}")
    print(f"WARNING lines: {levels['WARNING']}")
    print(f"INFO lines:    {levels['INFO']}")

    print("\n===== TOP IP ADDRESSES =====")
    if common_ips:
        for ip, count in common_ips:
            print(f"{ip} -> {count} hits")
    else:
        print("No IP addresses found.")

    print("\n===== SAMPLE FAILED LOGIN LINES =====")
    if failed_attempts:
        for line in failed_attempts:
            print(f"- {line}")
    else:
        print("No failed login attempts detected (based on keyword search).")

    print("\n✅ Analysis complete.")


if __name__ == "__main__":
    main()
