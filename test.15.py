x=float(input("1초당 움직인 거리:"))

m=x*(60*60)


print("시속:%.2f m/h, 시속:%.2f km/h" % (m,m/1000))
print("시속{}m/h, 시속:{}km/h".format(m,m/1000))