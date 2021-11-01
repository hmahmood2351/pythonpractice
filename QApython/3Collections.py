# dictionary composed of books and their respective authors

books = {'1984':'George Orwell', 'Brave New World':'Aldous Huxley'}
print(set(list(books.keys()))) # can be turned into a tuple/list/set

bookskeyslist = list(books.keys())
print(bookskeyslist)

# querying author of 1984, using keys only for dicts

print(books['1984'])

# printing certain indexes of a list

numberlist = [1,2,3]
print(numberlist[0:2]) #gives us [1,2]

#Bunch of different operatins relating to the data types, refer to documentation for more information
#on usage of dicts, tuples, sets and lists