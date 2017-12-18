def pretty_result(original_function):
    def wrapper(num1, num2):
        return "The result of the function '{}' is: {}".format(
        										original_function.__name__,
        										original_function(num1, num2)
        										)
    return wrapper



#########
# Tests #
#########

@pretty_result
def add(x, y):
    return x + y

print(add(2, 5))
