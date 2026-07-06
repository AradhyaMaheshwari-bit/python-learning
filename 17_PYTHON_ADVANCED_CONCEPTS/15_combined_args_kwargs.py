# for using args and kwargs in the same function "args" must come before "kwargs"

def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 5, jack=34, jill=45, marie=54)
