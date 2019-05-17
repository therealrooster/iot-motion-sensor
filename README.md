# IoT Motion Sensor with Pycom

### Objective
To create a motion sensor that collects acceleration data and sends it to the cloud.

### Hardware Details
[WiPy 3.0 Development Board](https://pycom.io/product/wipy-3-0/): WiFi & Bluetooth IoT development platform.
[Pytrack Sensor Shield](https://pycom.io/product/pytrack/): 3 axis 12-bit accelerometer.

### Code Specifications
* Maximum sampling rate of about 300Hz.
* Data stored within IoT device.

### Exporting Data from DynamoDB
* Data from DynamoDB can be exported into a .csv file with [DynamoDBtoCSV](
https://github.com/edasque/DynamoDBtoCSV) tool.
