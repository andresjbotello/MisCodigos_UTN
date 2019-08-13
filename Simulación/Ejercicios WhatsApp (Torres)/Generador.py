z0 = 7
m = 16
a = 4 
c = 4

x = []
for i in range(20):
    z = (a*z0+c)%m
    x.append(z)
    z0 = z

print(x)