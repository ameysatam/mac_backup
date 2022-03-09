# #Lists
#
# list1 = [1,2,3,10,3,4,2,5,6,10,9,1,2,3,4,5]
#
# list2 = list(set(list1))
#
# print(list1)
# print(list2)
# def rem_dup(a):
#     i=0
#     while i<len(a):
#         j=i+1
#         while j<len(a):
#             if a[i]==a[j]:
#                 del a[j]
#             else:
#                 j+=1
#         i+=1
#     print(a)
# # rem_dup(list1)
#
# list3 = []
# for i in list1:
#     if i not in list3:
#         list3.append(i)
# print("list3 = "+str(list3))
#
# list3.sort()
# print(list3)
# list3.sort(reverse=True)
# print(list3)
#
# list3.remove(10)
# print(list3)
# list3.pop()
# print(list3)
# list3.extend(list1)
# print(list3)
#
# list4 = list(set(list3))
# print(list4)
#
# list5=[]
# for i in list3:
#     if i not in list5:
#         list5.append(i)
# print(list5)


#Dictionary

# dict1 = {'animal':'lion','color':'blue','number':9}
#
# print(dict1.keys())
# for keys in dict1:
#     print(keys)
# for keys in dict1:
#     print(str(keys) + "--->"+str(dict1[keys]))
#
# for items in dict1.items():
#     print(items)
# print(dict1.values())

# import csv
# with open ("asdf.csv", mode='r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ',')
#     line_count = 0
    # for row in csv_reader:
    #     if line_count == 0:
    #         print(f'Column names are {", ".join(row)}')
    #         line_count+=1
    #     else:
    #         print(f'Rows are {", ".join(row)}')

def remdup(a):
    i=0
    while i<len(a):
        j=i+1
        while j<len(a):
            if a[i]==a[j]:
                del a[j]
            j+=1
        i+=1
    return a

print(remdup([1,2,3,4,5,2,3,4,5,6,5,4,3,2,10]))

a=[1,2,3,4,5,2,3,4,5,6,5,4,3,2,10]
b=list(set(a))
print(b)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

b=['amey', 'anup']

a.extend(b)
print(a)

c=[1,2,3,4,5,2,3,4,5,6,5,4,3,2,10]
c.insert(0,"amey")
print(c)
for i in c:
    if c.count(i)>1:
        c.remove(i)
print(c)

