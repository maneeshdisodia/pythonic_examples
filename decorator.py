# decorater

def ingredients(func):
    def wrapper():
        print("##totato##")
        func()
        print("##totato##")
        # print("</''''''''\>")

    return wrapper


def bread(func):
    def wrapper():
        print("</''''''''\>")
        func()
        print("<\......../>")

    return wrapper


# def sandwich(food='--ham--'):
#     print(food)
#
#
# sandwich()
# sandwich = bread(ingredients(sandwich))
# sandwich()


@bread
@ingredients
def sandwich(food='--ham--'):
    print(food)

sandwich()