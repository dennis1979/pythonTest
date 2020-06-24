import pandas as pd

print("pandas version : {}", pd.__version__)

print("----------my_obj----------")
my_obj = pd.Series([4, 7, -5, 3])
print(my_obj.values)
print(my_obj.index)

print("----------my_obj2----------")
my_obj2 = pd.Series([8, 9, 10, 11], index=['a', 'b', 'c', 'd'])
print(my_obj2)
print(my_obj2.values)
print(my_obj2.index)
print(my_obj2['a'])
print("index 'a' in series:", 'a' in my_obj2)

print("----------Dictionary to Series----------")
dic_data = {'name': 'apple', 'birthday': '1996-1-1', 'luckynumber': 7}
my_obj3 = pd.Series(dic_data)
print(my_obj3)

print("----------Series內部資料型態----------")
registration = [True, False, True, True]
registration = pd.Series(registration)
print(registration)

dictionary = {'A': 'an animal', 'B': 'a color', 'C':'a fruit'}
dictionary = pd.Series(dictionary)
print(dictionary)

print("----------DataFrame----------")
data = {'name': ['Bob', 'Nancy', 'Amy', 'Elsa', 'Jack'],
        'year': [1996, 1997, 1997, 1996, 1997],
        'month': [8, 8, 7, 1, 12],
        'day': [11, 23, 8, 3, 11]}
myframe = pd.DataFrame(data)
print(myframe)

print("----------更改columns順序----------")
myframe2 = pd.DataFrame(data, columns=['name', 'year', 'day', 'month', 'day'])
print(myframe2)

print("----------新增columns----------")
myframe3 = pd.DataFrame(data, columns = ['name', 'year', 'month', 'day', 'luckynumber'])
print("----------新增columns, 'luckynumber', but no data----------")
print(myframe3)
print("----------新增columns, 'luckynumber', with data----------")
luckynumber = ['3', '2', '1', '7', '8']
luckynumber = pd.Series(luckynumber)

myframe3['luckynumber'] = luckynumber
print(myframe3)
