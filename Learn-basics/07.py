#lists
my_list = ["Aamir", "Selmon", 12,12.8,"Srk"]
print(my_list)
print(my_list[0])
print(my_list[0].upper())

print(my_list[3])
print(my_list[-1])
my_list[1] = "hrx"
del my_list[3]
print(my_list)
#list comprehension
my_list = [i for i in range(10)]
print(my_list)
pow = [2**i for i in range(10)]
print(pow)
evnno = [i for i in range(10) if i%2==0]
print(evnno)
#list methods
my_list = [1,2,23,4,5,6,7,8,9,10]

my_list.append(11)
print(my_list)
my_list.insert(7,0.9)
print(my_list)
my_list.remove(0.9)
print(my_list)
my_list.pop(0)
my_list.sort()
fruits = ['Apple','Banana','Banana','Orange','Mango','Pineapple']
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(fruits.count('Banana'))
print(max(my_list))
#Loops in list
for i in my_list:
    print(i*2,end = " ")

