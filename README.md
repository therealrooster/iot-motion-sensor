# IoT Motion Sensor with Pycom

### Objective
To create a motion sensor that collects acceleration data and sends it to the cloud.

### Hardware Details
[WiPy 3.0 Development Board](https://pycom.io/product/wipy-3-0/): WiFi & Bluetooth IoT development platform.
[Pytrack Sensor Shield](https://pycom.io/product/pytrack/): 3 axis 12-bit accelerometer.

### Code Specifications
* Maximum sampling rate of about 300Hz.
* Data stored within IoT device.
#### Process
1. When main.py is run by the IoT device, the device attempts to
    1. Connect to the WiFi.
    2. Configure AWS (Client ID, security certificates, host, port, etc.)
    3. Connect to AWS with MQTT and subscribe and publish data to AWS topic.
2. When data is published to AWS, it is sent to DynamoDB.
3. Data in DynamoDB can be extracted into output.csv using the [DynamoDBtoCSV](
https://github.com/edasque/DynamoDBtoCSV) tool.
4. Data in output.csv can be graphed with graph_data.py script.

### Notes
* When using pymakr, usb port must have administrative rights, otherwise the device will not be able to connect. See [here](https://github.com/GoldenCheetah/GoldenCheetah/wiki/Allowing-your-linux-userid-permission-to-use-your-usb-device).
