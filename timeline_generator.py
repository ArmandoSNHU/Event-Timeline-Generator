import re

LOG_FILE = "sample.log"
TIMELINE_FILE = "timeline.txt"

KEYWORDS = {
    "Failed password": "Failed Login Attempt",
    "Accepted password": "Successful Login",
    "sudo:": "Privilege Escalation Attempt"
}

def generate_timeline():
    with open(LOG_FILE, "r", encoding="utf-8") as log, open(TIMELINE_FILE, "w", encoding="utf-8") as timeline:
        for line in log:
            for keyword, label in KEYWORDS.items():
                if keyword in line:
                    timestamp = " ".join(line.split()[0:3])
                    timeline.write(f"{timestamp} — {label} — {line.strip()}\n")
                    print(f"[+] Event captured: {label}")

    print(f"\n📄 Timeline saved to {TIMELINE_FILE}")

if __name__ == "__main__":
    print("🔍 Building security event timeline...")
    generate_timeline()
