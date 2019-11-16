x=str(input("Write your sentence:"))
k = ''
n = ''
y = x.split(" ")
for z in y:
    i = len(z)
    for j in range(i):
        k = k + z[i - 1 - j]
    k = k + ' '
print (k)


print(x[::-1])


