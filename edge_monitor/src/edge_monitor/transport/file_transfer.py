import json
from pathlib import Path

LOG_FILE = Path("metrics.log")

def send(data: dict):
    """
    Append metrics to a local log file in JSON format.
    """
    with LOG_FILE.open("a") as f:
        json.dump(data, f)
        f.write("\n")