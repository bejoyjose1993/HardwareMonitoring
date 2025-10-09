import asyncio
from .metrics import get_cpu_usage, get_ram_usage, get_disk_usage, get_gpu_usage
from .transport import file_transfer, http_transfer
from .transport.mqtt_transfer import MQTTPublisher
import os

from .utils import (
    print_metrics,
    register_signal_handlers,
    shutdown_event, 
    log_to_file,
    bytes_to_mb,
    bytes_to_gb,
    current_timestamp
)

class EdgeMonitor:
    def __init__(self, transport="http", interval=5, endpoint=None, broker=None, port=None):
        self.transport = transport or os.getenv("TRANSPORT", "mqtt")
        self.interval = interval or int(os.getenv("INTERVAL", 5))
        self.endpoint = endpoint or os.getenv("ENDPOINT")
        self.broker = broker or os.getenv("BROKER")
        self.port = port or int(os.getenv("PORT", 1883))
        self.mqtt_client = None

        # if self.transport == "mqtt" and broker and port:
        #     self.mqtt_client = MQTTPublisher(broker, port, "edge/metrics")

        if self.transport == "http" and endpoint:
            self.http_endpoint = endpoint
            
    async def run(self, shutdown_event: asyncio.Event):
        print("EdgeMonitor started...")
        while not shutdown_event.is_set():
            try:
                cpu = get_cpu_usage()
                ram = get_ram_usage()
                disk = get_disk_usage()
                gpu = get_gpu_usage()

                data = {
                    "timestamp": current_timestamp(),
                    "cpu_percent": cpu,
                    "ram": {"total_mb": bytes_to_mb(ram["total"]),
                            "used_mb": bytes_to_mb(ram["used"]),
                            "percent": ram["percent"]},
                    "disk": {"total_gb": bytes_to_gb(disk["total"]),
                            "used_gb": bytes_to_gb(disk["used"]),
                            "percent": disk["percent"]},
                    "gpu": gpu
                }

                if self.transport == "file":
                    file_transfer.send(data)
                elif self.transport == "http":
                    try:
                        await http_transfer.send(self.endpoint, data)
                        print(f"[INFO] Sent metrics successfully to {self.endpoint}")
                    except Exception as e:
                        print(f"[ERROR] HTTP send failed: {e}")

                await asyncio.sleep(self.interval)

            except asyncio.CancelledError:
                break

        print("EdgeMonitor stopped.")