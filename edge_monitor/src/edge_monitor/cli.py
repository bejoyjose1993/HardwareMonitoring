"""Console script for edge_monitor."""
import typer
import argparse
import asyncio
from .edge_monitor import EdgeMonitor

app = typer.Typer() 

@app.command()
def main():

    parser = argparse.ArgumentParser(description="Edge Device Monitoring Tool")
    parser.add_argument("--transport", choices=["file", "http", "mqtt"], default="http")
    parser.add_argument("--interval", type=int, default=5)
    parser.add_argument("--endpoint", type=str, default="http://localhost:8000/ingest")
    parser.add_argument("--broker", type=str, default="localhost", help="MQTT broker hostname")
    parser.add_argument("--port", type=int, default=1883, help="MQTT broker port")
    args = parser.parse_args()

    print(f"[INFO] Starting EdgeMonitor with transport={args.transport}, broker={args.broker}:{args.port} ...")
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
