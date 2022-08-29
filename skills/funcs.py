# def foo(a):
#     a += [200,300,400]

# a_list = [1,2,3]
# foo(a_list)
# print(a_list)

def boo(a, b, *args, **kwargs):
    print(a)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
    print(b)

boo(1,2,3,4,5,6,7,d='kwarg')

numbers = [1,2,3,4,5,6]
*beginning, last = numbers 
print(beginning)
print(last)