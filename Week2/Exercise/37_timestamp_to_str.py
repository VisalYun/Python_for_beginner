import datetime
def timestamp(a):
    b = int(a)
    x = datetime.datetime.fromtimestamp(b)
    return x

print(timestamp(1623646780))
print(timestamp("1623646780"))
