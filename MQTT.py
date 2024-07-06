import paho.mqtt.client as mqtt

MQTT_BROKER = "your_mqtt_broker_address"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/alerts"

# Define the MQTT client
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message Published")

client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Send alerts if anomalies are detected
for i, anomaly in enumerate(anomalies):
    if anomaly:
        message = f"Anomaly detected in data point {i} with error {reconstruction_errors[i]}"
        client.publish(MQTT_TOPIC, message)
        print("Alert Sent:", message)

client.loop_forever()
