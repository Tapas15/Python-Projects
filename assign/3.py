#Python Assignment no 3 
#import  bisect
data = {
        'hello':     ['doc1'], 
        'my':        ['doc1'], 
        'name':      ['doc1'], 
        'is':        ['doc1', 'doc2'], 
        'james':     ['doc1', 'doc2'], 
        'a':         ['doc2'], 
        'developer': ['doc2']
        }
print(type(data)) # data are in dict form  lest convert into list 
#print(data)
lists_of_tup = [(k,v)for k,v in data.items()]
#print(lists_of_tup)
list1 =[]
for a in lists_of_tup:
        if a[0] == 'a':
                #print(a)
                list1.append(a)
                for a in lists_of_tup:
                        if a[0] == 'developer':
                               # print(a)
                                list1.append(a)
                                #print(list1)
                                for a in lists_of_tup:
                                        if a[0] == 'hello':
                                                #print(a)
                                                list1.append(a)
                                                #print(list1)
                                                for a in lists_of_tup:
                                                        if a[0] == 'my':
                                                                #print(a)
                                                                list1.append(a)
                                                                #print(list1)
                                                                for a in lists_of_tup:
                                                                        if a[0] == 'name':
                                                                                #print(a)
                                                                                list1.append(a)
                                                                                #print(list1)
                                                                                for a in lists_of_tup:
                                                                                        if a[0] == 'is':
                                                                                                #print(a)
                                                                                                list1.append(a)
                                                                                                #print(list1)
                                                                                                for a in lists_of_tup:
                                                                                                        if a[0] == 'james':
                                                                                                                #print(a)
                                                                                                                list1.append(a)
                                                                                                                print(list1)



"Achieved output by iteratiing through another method "
"[('a', ['doc2']), ('developer', ['doc2']), ('hello', ['doc1']), ('my', ['doc1']), ('name', ['doc1']), ('is', ['doc1', 'doc2']), ('james', ['doc1', 'doc2'])]"
"Tried several method but may be out of logic below "
"But this is not correct logic may be logic improvement required or some basic missing"
# lists = [(key,value) for key , value in data.items()] # converted into a list 
# print(type(lists.pop())) # achieve a tuple inside a list items 
# print(type(lists)) # here we cannot chage any content of tupple 
# print(lists)
# for a in lists:
#         if a[0] == 'a':
#                 print(a)
# for b in lists:
#         if b[0] == 'hello':
#                 print(b)






# for i in range(0,len(lists),1):
#         if(lists[i]>=lists[i]):
#                 print(lists[i+0][1])
        #print(lists[i][0],lists[i+0][1])
        

#lists 
# def SortTuple(lists):
#         n =len(lists)
#         #print(n)
#         for i in range(n):
#                 for j in range(n -i -1):
#                         print(j)
# SortTuple(lists)

# how to get the result required it not clear
# second_tupple_elements = []
# for a_tupple in lists:
#         second_tupple_elements.append(a_tupple[1])
# print(second_tupple_elements)

# for key in data.items():
#         for value in lists:
#                 if(key == value):
#                         print(key)





#print(lists)
#tup = []
# for value in data.items():
#         for val in lists:
#                 if(value == val[1]):
#                         print(val)
        
#print(len(lists))

# #get key value pairs 
# dict1 = data.items() # got key value paris of dictionary 
# sort = sorted(dict1) # dictionary value sorted 
# new_list = sorted(data, key=lambda x: (len(x), x))
# print(new_list)

# import operator 
# sorted_tuples = sorted(data.items(), key=operator.itemgetter(-2),reverse=False)
# print(sorted_tuples)
# #print(sorted(data.values(),reverse=True)) # printed turple valie in reverse
