# get vs [] for reteriving element
my_dict={'name': 'jack', 'age':26}
# output jack
print(my_dict['name'])

# output 26
print(my_dict.get('age'))

# trying to access keys which does not  exit throns error
# output none
print(my_dict.get('address'))

# output key error 
# print(my_dict['address'])

# update and add dictonary value

my_dic={'name' : 'jack', 'age':26}
# update value
my_dic['age']=27
print(my_dic)

# add item
my_dic['address']='hometown'
print(my_dic)

# removing an element from dictonary
# create dictonary
my_dct={1:1,2:4,3:9,4:16,5:25}
# remove a particular items returns its value
# output 16
print(my_dct.pop(4))

# output(1:1,2:4,3:6,5:25)
print(my_dct)

# remove an arbitrary item return (key,value)

# print(my_dct.popitems(5))

# output: (1:1,2:4,3:9)
# remove all items
my_dct.clear()
# output: ()
print(my_dct)
# delete the dictonary itself
del my_dct

