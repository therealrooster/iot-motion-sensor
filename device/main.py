from MQTTLib import AWSIoTMQTTClient
from network import WLAN
from get_data import motion_data
import time
import json

# Wifi Data
WIFI_SSID = 'M1-8790'
WIFI_PASS = '9070868780'

# Connect to wifi
wlan = WLAN(mode=WLAN.STA)
wlan.connect(WIFI_SSID, auth=(None, WIFI_PASS), timeout=5000)
while not wlan.isconnected():
    time.sleep(0.5)
print('WLAN connection succeeded!')

# AWS Configuration
AWS_PORT = 8883
AWS_HOST = 'a2kous076awbqo-ats.iot.ap-southeast-1.amazonaws.com'
AWS_ROOT_CA = '/flash/cert/root-CA.crt'
AWS_CLIENT_CERT = '/flash/cert/mrt-sensor.cert.pem'
AWS_PRIVATE_KEY = '/flash/cert/mrt-sensor.private.key'
CLIENT_ID = 'basicPubSub'
TOPIC = 'sdk/test/Python'


def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(AWS_HOST, AWS_PORT)
myAWSIoTMQTTClient.configureCredentials(AWS_ROOT_CA, AWS_PRIVATE_KEY, AWS_CLIENT_CERT)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

if myAWSIoTMQTTClient.connect():
    print('AWS connection successful!')

# Subscribe to topic
myAWSIoTMQTTClient.subscribe(TOPIC, 1, customCallback)
time.sleep(2)

# Publish Data to AWS
for i in motion_data:
    message = {}
    message['message'] = i
    messageJson = json.dumps(message)
    myAWSIoTMQTTClient.publish(TOPIC, messageJson, 1)
