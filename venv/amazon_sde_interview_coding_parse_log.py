#Find user with lowest latency from log file:
# 200,John,/home,60ms
# 200,Sarah,/log,13ms
# 500,Jack,/home,40ms

# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

name = {}
latency = {}
sorted_latency = {}
with open ("test.log", "+r") as logfile:
    for line in logfile:
        name[line.split(",")[0].strip()] = line.split(",")[1].strip()
        latency[line.split(",")[0].strip()] = int(line.split(",")[3].strip().strip("ms"))
print(name)
print(latency)
sorted_latency = dict(sorted(latency.items(), key= lambda x:x[1]))
print("sorted_latency=", sorted_latency)
lowest_latency = list(sorted_latency.values())[0]
id = list(sorted_latency.keys())[0]
print("lowest latency = ", lowest_latency)
lowest_latency_name = name[id]
print("lowest latency name = ", lowest_latency_name)
#print("", has the lowest latency,