hosttab = {}
with open("logfile.log", 'r') as logfile:
    for line in logfile:
        hosttab[line.split()[0].strip()] = int(line.split()[3].strip())
print(hosttab)
sorted_hosttab = dict(sorted(hosttab.items(), key=lambda x:x[1], reverse=True))
print(sorted_hosttab)
for x in sorted_hosttab:
    print(x," ", sorted_hosttab[x], )

#sorted_hosttab = dict(sorted(hosttab.items(), key=lambda x:x[1], reverse=True))
