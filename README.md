# 🗂️ Event Timeline Generator

A simple Python script that parses system logs and builds a clean, timestamped timeline of security-related events — just like a SOC analyst would during incident response.

---

## 🔍 What It Does

- Reads a log file (`sample.log`)
- Scans for specific event patterns like:
  - `Failed password`
  - `Accepted password`
  - `sudo:` activity
- Extracts the timestamp and labels the event
- Outputs a structured timeline to `timeline.txt`
- Displays captured events in real time

---

## ✅ Features

- 🕒 Timestamped entries
- 🔐 Detection of login attempts and privilege escalation
- 📝 Output stored in `timeline.txt` for later review
- 🧠 Easy to expand with more keywords and event types

---

## 📁 Folder Structure

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/ArmandoSNHU/Event-Timeline-Generator.git
   cd Event-Timeline-Generator

run script:
   python3 timeline_generator.py

check the output:
cat timeline.txt
