def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        print(locals())
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func


def func_needs_decorator():
    print('THIS FUNCTION NEED OF A DCORATOR')


func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
