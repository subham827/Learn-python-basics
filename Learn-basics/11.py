#File Handling
# f = open('data.txt', 'r')
# print(f.readline())
# print(f.read())
# for line in f:
#     print(line)
# f.close()

# This was obsolete method
# This is new method

with open('data.txt') as f:
    # for line in f:
    #     print(line)

    print(f.read(10))    
    print(f.read(10))
    f.seek(13)
    print(f.read(10))

line_data = ['Shlok','Yash','Aamir']
with open('data1.txt','w') as f:
    f.write('This is a new line')
    f.write('\n')
    f.writelines(line_data)

with open ('data1.txt','a') as f:
    f.write('This is appended')