sec=int(input("초:"))

min=sec // 60 #분
second=sec%60

print("%d초 = %d분 %d초" % (sec,min,second))
print("{}초 = {}분 {}초".format(sec,min,second))
