"""Console script for edge_monitor."""
import typer
import argparse
import asyncio
from .edge_monitor import EdgeMonitor

app = typer.Typer() 

@app.command()
def main():

    parser = argparse.ArgumentParser(description="Edge Device Monitoring Tool")
    parser.add_argument("--transport", choices=["file", "http", "mqtt"], default="file")
    parser.add_argument("--interval", type=int, default=5)
    parser.add_argument("--endpoint", type=str, default="http://localhost:8000/ingest")
    parser.add_argument("--broker", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=1883)
    args = parser.parse_args()

    print("[INFO] Starting EdgeMonitor...")
    monitor = EdgeMonitor(
        transport=args.transport,
        interval=args.interval,
        endpoint=args.endpoint,
        broker=args.broker,
        port=args.port
    )

    asyncio.run(monitor.run())

if __name__ == "__main__":
    app()
