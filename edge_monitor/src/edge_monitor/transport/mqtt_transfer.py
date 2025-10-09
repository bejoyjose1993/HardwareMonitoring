import json
import time
import paho.mqtt.client as mqtt

class MQTTPublisher:

    def __init__(self, broker: str, port: int, topic: str):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()
        print("In MQTTPublisher Init...")
        print(f"[DEBUG] Trying to connect to MQTT broker {broker}:{port}:{topic}")
        try:
            self.client.connect(broker, port, 60)
            self.client.loop_start()
            print(f"[INFO] Connected to MQTT broker {broker}:{port}")
        except Exception as e:
            print(f"[ERROR] MQTT connection failed: {e}")

    def send(self, data: dict):
        print("Data Published in MQTT")
        try:
            print(self.topic)
            print(json.dumps(data))
            self.client.publish(self.topic, json.dumps(data), qos=1)
        except Exception as e:
            print(f"[ERROR] MQTT send failed: {e}")

            
    def loop_forever(self, get_metrics_func, interval=1):
        """Continuously send metrics every `interval` seconds"""
        try:
            while True:
                data = get_metrics_func()
                self.send(data)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("[INFO] Stopping MQTT publisher")
            self.client.disconnect()