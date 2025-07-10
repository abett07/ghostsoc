import json
import os
from datetime import datetime

LOG_FILE = "session_log.json"

def log_session(command: str, response: str):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "command": command,
        "response": response
    }

    # Create log file if not exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f, indent=4)

    # Append new entry
    with open(LOG_FILE, "r+") as f:
        data = json.load(f)
        data.append(log_entry)
        f.seek(0)
        json.dump(data, f, indent=4)
