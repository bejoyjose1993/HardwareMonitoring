import asyncio
from .metrics import get_cpu_usage, get_ram_usage, get_disk_usage, get_gpu_usage
from .transport import file_transfer, http_transfer, mqtt_transfer
from .utils import (
    print_metrics,
    register_signal_handlers,
    log_to_file,
    bytes_to_mb,
    bytes_to_gb,
    current_timestamp
)

class EdgeMonitor:
    def __init__(self, transport="file", interval=5, endpoint=None, broker=None, port=None):
        self.transport = transport
        self.interval = interval
        self.endpoint = endpoint
        self.broker = broker
        self.port = port

    async def run(self):
        register_signal_handlers()
        while True:
            print("Collecting metrics...")
            cpu = get_cpu_usage()
            ram = get_ram_usage()
            disk = get_disk_usage()
            gpu = get_gpu_usage()


            # Convert RAM and Disk to human-readable MB/GB
            ram_data = {
                "total_mb": bytes_to_mb(ram["total"]),
                "used_mb": bytes_to_mb(ram["used"]),
                "percent": ram["percent"]
            }
            disk_data = {
                "total_gb": bytes_to_gb(disk["total"]),
                "used_gb": bytes_to_gb(disk["used"]),
                "percent": disk["percent"]
            }

            data = {
                "timestamp": current_timestamp(),
                "cpu_percent": cpu,
                "ram": ram_data,
                "disk": disk_data,
                "gpu": gpu
            }

            # Print metrics to console for debugging
            print_metrics(data)

            # Log metrics to local file
            log_to_file("metrics.log", data)

            if self.transport == "file":
                file_transfer.send(data)
            elif self.transport == "http":
                await http_transfer.send(self.endpoint, data)
            elif self.transport == "mqtt":
                mqtt_transfer.send(self.broker, self.port, "edge/metrics", data)

            await asyncio.sleep(self.interval)
