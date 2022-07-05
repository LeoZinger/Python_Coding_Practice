#Find user with lowest latency from log file:
# 200,John,/home,60ms
# 200,Sarah,/log,13ms
# 500,Jack,/home,40ms

name = {}
latency = {}
sorted_latency = {}
with open ("test.log", "+r") as logfile:
    for line in logfile:
        name[line.split(",")[0].strip()] = line.split(",")[1].strip()
        latency[line.split(",")[0].strip()] = int(line.split(",")[3].strip().strip("ms"))
print(name)
print(latency)
sorted_latency = {y:latency[y] for y in sorted(latency, key= lambda x:latency[x])}
print("sorted_latency=", sorted_latency)
id = list(sorted_latency.keys())[0]
lowest_latency = list(sorted_latency.values())[0]
print(id)
lowest_latency_name = name[id]
print(f"{lowest_latency_name}[{id}] has the lowest latency of {lowest_latency}")


# How to sort a dicctionary by keys and values
dict1 = {'200': 60, '300': 13, '500': 3, '600': 45, '900': 5, '100': 50, '800': 8}
del dict1[1]
dict2 = {}
# for i in sorted(dict1):
#     dict2[i] = dict1[i]
#     print("i = " + i)
#     print("dict2[" + i + "] :" + str(dict2[i]))
print([x for x in dict1.items()])
dict2 = dict(sorted(dict1.items(), key=lambda x:x[1]))
print('original dict : ', dict1) # 3
print('sorted dict : ', dict2) # 3
# print('Minimum Key',min(dict1)) # 1

