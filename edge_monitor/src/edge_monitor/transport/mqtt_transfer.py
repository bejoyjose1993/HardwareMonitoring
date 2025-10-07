import json
import paho.mqtt.client as mqtt

def send(broker: str, port: int, topic: str, data: dict):
    """
    Publish metrics to an MQTT broker.
    """
    try:
        client = mqtt.Client()
        client.connect(broker, port, 60)
        client.publish(topic, json.dumps(data))
        client.disconnect()
        print(f"[INFO] Published metrics to {broker}:{port} on topic '{topic}'")
    except Exception as e:
        print(f"[ERROR] MQTT send failed: {e}")