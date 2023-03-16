# 1)
# my_list = ['qwe', 'qwer', 'qwert', 'qwerty', 'qwertyu', 'qwertyui', 'qwertyuio']
# new_list = []
# for index in range(len(my_list)):
#     if index % 2:
#         new_list.append(my_list[index][::-1])
#     else:
#         new_list.append(my_list[index])
# print(new_list)

#2)
# my_list = ['awe', 'qwer', 'wert', 'awerty', 'qwertyu', 'qwertyui', 'awertyuio']
# new_list = []
# for symbol in my_list:
#     if 'a' in symbol[0::][0]:
#         new_list.append(symbol)
# print(new_list)

# 3)

# my_list = ['awe', 'qwar', 'wert', 'weraty', 'qwertyu', 'qwertyui', 'awertyuio']
# new_list = []
# for symbol in my_list:
#      if 'a' in symbol:
#          new_list.append(symbol)
# print(new_list)

# persons = [{
#     'first name':'John',
#     'age':'15',
#     'adress':'Kremlin',
# },
#     {'first name':'Drake',
#      'age':'30',
#      'adress':'New Orelean'
#         },
# {'first name':'Make',
#      'age':'77',
#      'adress':'London'
#         },
# {'first name':'Brandon',
#      'age':'22',
#      'adress':'Kyiv'
#         }]
# min_age_person = []
#
# for i in persons:
#     if i["age"] not in min_age_person:
#         min_age_person.append(i["age"])
#     else:
#         min_age_person.append(i["age"])
# print(min(min_age_person))

# 4, б)
# people = [{"name": "Sid", "age": 40},
#           {"name": "jon", "age": 55},
#           {"name": "Amm", "age": 15},
#           {"name": "Brandon", "age": 22},
#           {"name": "Joseph", "age": 11},
#           {"name": "Mike", "age": 32}]
#
# longest_names = []
# max_length = 0
#
# for person in people:
#     name_length = len(person["name"])
#     if name_length > max_length:
#         longest_names = [person["name"]]
#         max_length = name_length
#     elif name_length == max_length:
#         longest_names.append(person["name"])
#
# print(longest_names)

# 4, в)
#
# people = [{"name": "Sid", "age": 40},
# #           {"name": "jon", "age": 55},
# #           {"name": "Amm", "age": 15},
# #           {"name": "Brandon", "age": 22},
# #           {"name": "Joseph", "age": 11},
# #           {"name": "Mike", "age": 32}]
#
# total_age = 0
# num_people = len(people)
#
# for person in people:
#     total_age += person["age"]
#
# average_age = total_age / num_people
#
# print(average_age)

# 5,а
# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
# keys_1 = set(my_dict_1.keys())
# keys_2 = set(my_dict_2.keys())
# common_keys = list(keys_1 & keys_2)
# print(common_keys)

# 5,б
# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
# keys_1 = set(my_dict_1.keys())
# keys_2 = set(my_dict_2.keys())
#
# unique_keys = list(keys_1 - keys_2)
# print(unique_keys)
# 5, в
# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
# unique_keys = set(my_dict_1.keys()) - set(my_dict_2.keys())
# new_dict = {key: my_dict_1[key] for key in unique_keys}
# print(new_dict)

# 5, г
# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
# new_dict = {}
#
# for key in set(my_dict_1.keys()) | set(my_dict_2.keys()):
#     if key in my_dict_1 and key not in my_dict_2:
#         new_dict[key] = my_dict_1[key]
#     elif key in my_dict_2 and key not in my_dict_1:
#         new_dict[key] = my_dict_2[key]
#     else:
#         new_dict[key] = [my_dict_1[key], my_dict_2[key]]
#
# print(new_dict)