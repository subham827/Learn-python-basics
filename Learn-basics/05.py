#range

a = list(range(10))
b = list(range(1,10))
c = list(range(1,10,2))
print(a)
print(b)
print(c)
#for loop
for i in range(10):
    print(i)
for i in range(10):
    print(i, end=",")
#Pascal's Triangle
for i in range(1,10):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

a = ['Aamir','Selmon','Srk']
for i in a:
    print(i*3,end=" ")

#while loop
i = 0
while i < 10:
    print(i)
    i += 1

#break and continue
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)
#break takes you out of the loop whereas continue is used to skip the current iteration
    