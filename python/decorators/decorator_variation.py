def small_numbers(fn):
	''' raise ValueError when any numeric arg is > 100 '''
    def wrapper(*args):
        for arg in args:
            if type(arg) in [int, float]:
                if arg > 100:
                    raise ValueError
        return fn(*args)
    return wrapper


#########
# Tests #
#########

@small_numbers
def my_func(number_param, string_param):
  pass

my_func(99, "Hi")  # OK
my_func(101, "Oh no!")  # ValueError raised