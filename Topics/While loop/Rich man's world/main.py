n = int(input())
r = 1.071
cd = 700000
c = 0
while n < cd:
    n *= r
    c = c + 1
print(c)
