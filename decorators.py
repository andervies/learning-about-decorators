# def add(a, b):
#     return a + b


# sum = add(1,)

# print(sum(4,3))

# print("After assigning add to sum")
# print("After calling sum")


# def outer():
#     print("This runs first")

#     def inner():
#         print("This runs second")

#     inner()
#     print('done calling inner function')

# outer()


# def parent():
#     print("I am a parent calling my child")

#     def child():
#         print("I am just a childddddd")
    
#     child()


# new_parent = parent

# new_parent()

# def outer():
#     def inner():
#         print("I am returned!")
#     return inner


# my_func = outer()
# my_func()

def python():
    def inner_python():
        print("python is cool")
    return inner_python

python_func = python()

python_func()
