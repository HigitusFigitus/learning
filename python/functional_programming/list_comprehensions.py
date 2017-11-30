# Imperative vs Declarative

# Imperative
result = []
for name in names:
	result.append(len(name))

# Declarative
[len(name) for name in names]


def remove_duplicates_in_order(a_list):
    [a_list.remove(elem) for elem in a_list if a_list.count(elem) > 1] # remove modfies in place
    return a_list


def reverse_list(a_list):
    a_list.reverse() # reverse also modfies in place
    return a_list


def even_numbers(a_list): # receives a list of numbers and returns only the even elements
    return [elem for elem in a_list if elem % 2 == 0]


def square_elements(a_list):
    return [elem ** 2 for elem in a_list]


def divisible_numbers(a_list, term):
    return [elem for elem in a_list if elem % term == 0]


def divisible_numbers(a_list, a_list_of_terms): # receives a list of numbers and a list of terms and returns only the elements that are divisible by all the terms.
    return [elem for elem in a_list if all([elem % t == 0 for t in a_list_of_terms])]

def to_fahrenheit(a_list):
    return [(lambda elem: elem * 1.8 + 32) (elem) for elem in a_list]
