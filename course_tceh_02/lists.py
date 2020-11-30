# lists:
not_a_list = (1, 2, )
list1 = [1, 2]
list2 = list(not_a_list)

print(list1 == list2, not_a_list == list1)
print(not_a_list, list1, list2)

list1.append(3)
print('append() return None: ', list1.append(4))
print(list1)

list1.append(list2)
print(list1)

list1.extend(list2)
print(list1)

list1.insert(1, 'inserted value')
print(list1)

# LIST ARE MUTABLE
var = ['bar']
new_var = var
var.append('foo')
var[0] = 'baz'
print(new_var)
#end