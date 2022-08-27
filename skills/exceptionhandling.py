from typing import Type


z = 2

if z < 0:
    raise Exception('x should be positive')

assert(3>2), 'X is smaller'

try:
    # b = a + '10'
    a = 5/1
except ZeroDivisionError as e:
    print(e)
    print('kernel panic')
except NameError as e:
    print(e)
else:
    print("successful execution")
finally:
    print('cleaning up')

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message 
        self.value = value

    def runtimefix(self):
        print("Running logging and attempted runtime fix")

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    elif x < 10:
        raise ValueTooSmallError('Value too small', x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message)
    print(e.value)
    e.runtimefix()