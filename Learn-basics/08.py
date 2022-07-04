#Sets and dictionary
set1 = {1,2,3,4,5,6,7,8,9,10}
#sets is same as list just all the values are unique and no order
dictionary1 = {'Aamir':'Selmon','Srk':'Selmon','Selmon':'Aamir','Srk':'Hrx'}
#dictionary is a collection of key value pairs
print(dictionary1['Aamir'])
print(dictionary1['Srk'])
dictionary2 = {'Grade': 'A', 'Name': 'Aamir', 'Age': '21','Marks' : [78,89,90,91]}
print(dictionary2['Grade'])
print(dictionary2['Marks'])
dictionary3 = {1:1,2:9,3:7,5:4}
for i in dictionary3:
    print(i,end=" ")
    print(dictionary3[i])
#dictionary methods
dictionary1['Aamir'] = 'Akshay'
print(dictionary1)
dictionary1.pop('Aamir')
print(dictionary1)
dictionary2['Marks'].append(92)
print(dictionary2)