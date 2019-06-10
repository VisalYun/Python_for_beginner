amount = input("Please enter your amount: ")
while(amount.isdigit()==False):
    print("Number is incorrect, try again.")
    amount = input("Please enter your amount: ")
rate = input("Pleae enter tax rate: ")
while(rate.isdigit()==False or int(rate)>=99 or int(rate)<=1):
    print("Rate is incorrect, try again.")
    rate = input("Please enter tax rate: ")
print("==== ==== ==== ==== ====")
print("AMOUNT: "+str(amount)+"$")
print("RATE: "+str(rate)+"%")
print("==== ==== ==== ==== ====")
tax= round(float(amount)*(float(rate)/100),2)
net = round(float(amount)-tax , 2)
print("==== ==== ==== ==== ====")
print("TAX: "+str(tax)+"$")
print("NET: "+str(net)+"$")
print("==== ==== ==== ==== ====")




