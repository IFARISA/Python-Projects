errors = (FileNotFoundError ,SyntaxError, ZeroDivisionError, TypeError, EnvironmentError)
try:
    print(10/0)
except errors:
    print('Check')