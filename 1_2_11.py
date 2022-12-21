array = ["Bob", "Alex", "Bob", "John"]
d=dict()
for a in array:
    try:   d[a] += 1
    except KeyError: d[a] = 1
print(d)
