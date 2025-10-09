# run_all.py
import asyncio
from edge_monitor.edge_monitor import EdgeMonitor
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import signal

metrics_store = {}

# FastAPI server
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ingest")
async def ingest(data: dict):
    metrics_store.update(data)
    print("\n✅ Metrics received:", data)
    return {"status": "ok"}

@app.get("/metrics")
async def get_metrics():
    return metrics_store

async def run_edge_monitor(shutdown_event: asyncio.Event):
    monitor = EdgeMonitor(transport="http", endpoint="http://localhost:8000/ingest", interval=5)
    await monitor.run(shutdown_event)

async def run_server(shutdown_event: asyncio.Event):
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server_task = asyncio.create_task(server.serve())

    # Wait for shutdown
    await shutdown_event.wait()
    server.should_exit = True
    await server_task

async def main():
    shutdown_event = asyncio.Event()

    # Ctrl+C handler
    def stop_app(sig, frame):
        print("Exiting...")
        shutdown_event.set()

    signal.signal(signal.SIGINT, stop_app)
    signal.signal(signal.SIGTERM, stop_app)

    # Run both tasks concurrently
    await asyncio.gather(
        run_server(shutdown_event),
        run_edge_monitor(shutdown_event)
    )

if __name__ == "__main__":
    asyncio.run(main())
