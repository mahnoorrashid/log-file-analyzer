# 🔎 Log File Analyzer (Python)

A simple log file analyzer written in Python.

It reads a `.log` file and:
- Counts total log lines
- Counts how many lines contain `ERROR`, `WARNING`, and `INFO`
- Extracts IP addresses and shows the most frequent ones
- Shows sample lines that look like failed login attempts

This is a beginner-friendly cybersecurity / DevOps style project.

---

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Clone or download this repository.
3. Put your log file in the same folder (e.g. `sample.log`).
4. Run:

```bash
python3 log_analyzer.py

📘 Example Output
🔎 Simple Log File Analyzer
Enter path to log file (e.g. sample.log): sample.log

===== SUMMARY =====
Total lines: 7
ERROR lines:   2
WARNING lines: 2
INFO lines:    3

===== TOP IP ADDRESSES =====
192.168.0.10 -> 3 hits
10.0.0.5 -> 2 hits
203.0.113.8 -> 1 hits

===== SAMPLE FAILED LOGIN LINES =====
- 2025-11-10 10:04:02 ERROR Failed password for root from 203.0.113.8 port 22 ssh2

✅ Analysis complete.

📝 Future Improvements
	•	Support JSON or CSV log formats
	•	Filter by date range or log level
	•	Export findings to a report file
	•	Add coloured terminal output or a GUI

⸻

👩🏽‍💻 Author

Mahnoor Rashid
