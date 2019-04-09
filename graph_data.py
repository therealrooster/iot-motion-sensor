from matplotlib import pyplot as plt
import csv
import json

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Format data
file = open('output.csv', newline='')
reader = csv.reader(file)
raw_data = [i for i in reader][1:]  # Remove first line.
data = [json.loads(i[0])['message'] for i in raw_data]
# data = [[float(j['N']) for j in json.loads(i[2])['message']['L']] for i in raw_data]
z_acc = [i[2] for i in data]

# Plot graph
ax1.plot(z_acc)
plt.show()
