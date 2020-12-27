"""
Сделайте словарь дней недели {1: "Monday", 2:... } в общем словарь. И потом "переверните" чтоб было {"Monday": 1, ...
"""
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daysOfWeek = {i + 1: days[i] for i in range(len(days))}
reverseDaysOfWeek = {value: key for key, value in daysOfWeek.items()}
print(daysOfWeek)
print(reverseDaysOfWeek)

"""
Task 1
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the 
number of occurrences as values. 
"""
inputString = input('Enter a string \n')
dictFromString = {inputString.split(" ")[i]: inputString.split(" ").count(inputString.split(" ")[i]) for i in
                  range(len(inputString.split(" ")))}
print(dictFromString)

"""
Task 2
Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total 
price of stock.
"""
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def get_price_of_stock(name, price):
    cost = 0
    for nameKey, nameValue in name.items():
        cost += nameValue * price.get(nameKey, 0)
    return cost


print(get_price_of_stock(stock, prices))

'''
Task 3
List comprehension exercise
Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding 
to `i` squared.
'''
squaredList = [(i, i*i) for i in range(1, 11)]
print(squaredList)