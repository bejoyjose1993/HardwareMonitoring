import signal
import sys
import time
import json
from pathlib import Path 
import threading

# Shutdown flag (Initilly used now handled in run_all.py)
shutdown_event = threading.Event()

# Handler for Ctrl+C / Termination (Initilly used now handled in run_all.py)
def handle_exit(sig=None, frame=None):
    if not shutdown_event.is_set():
        print("Exiting...")
        shutdown_event.set() 

#(Initilly used now handled in run_all.py)
def register_signal_handlers():
    try:
        # Register signals normally (Unix)
        signal.signal(signal.SIGINT, handle_exit)   # For Ctrl+C
        signal.signal(signal.SIGTERM, handle_exit)  # For Termination signal
    except ValueError:
            # Windows may raise ValueError for signals in threads
            print("[WARN] Signals not fully supported, relying on shutdown_event and KeyboardInterrupt")
            pass
    
# For Time formatting 
def current_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# Written For Logging the data
def log_to_file(file_path: str, data: dict):
    path = Path(file_path)
    with path.open("a") as f:
        json.dump(data, f)
        f.write("\n")

def print_metrics(data: dict):
    print(f"[{current_timestamp()}] Metrics:")
    for k, v in data.items():
        print(f"  {k}: {v}")
    print("-" * 30)

# Helper function for Byte conversion
def bytes_to_mb(bytes_val):
    return round(bytes_val / (1024 * 1024), 2)

def bytes_to_gb(bytes_val):
    return round(bytes_val / (1024 * 1024 * 1024), 2)
