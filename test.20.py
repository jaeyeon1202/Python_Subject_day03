num1=1
num2=1
num3=0
print("%d %d" % (num1,num2),end="")

for i in range(8):
    num3=num1+num2
    print(" %d " % (num3), end="")
    num1=num2
    num2=num3
