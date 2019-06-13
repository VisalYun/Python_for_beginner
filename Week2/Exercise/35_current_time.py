import datetime
def current_time():
    x = datetime.datetime.now()
    return x.strftime("%H:%M:%S")

print(current_time())
