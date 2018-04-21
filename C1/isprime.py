
#def isprime(a):
emptylist = list()
n = int(input())
num = n**2 + n + 41
for numbers in range(1,n):
    cn = numbers**2 + numbers + 41
    for dividers in range(2,(n-1)):
        if cn%dividers == 0:
            print("value is", cn, "divider is", dividers)
