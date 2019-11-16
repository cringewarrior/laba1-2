text = str(input("Write something:"))
i = 0
for j in text:
    if j.isalnum() and not j.isnumeric():
        i += 1
print (i)

prise = []
[prise.append(x) for x in text if not x.isalpha()]
print(len(prise))

