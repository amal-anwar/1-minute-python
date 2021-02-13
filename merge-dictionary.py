def Merge(a,b):
    x = {**a, **b}
    return x

#Driver code
a = {"k1": "v1", "k2": "v2"}
b = {"k3": "v3", "k4": "v4"}

c = Merge (a,b)

print (c)
