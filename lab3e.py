#!/usr/bin/env python3

# Create the list called "my_list" here, not within any function defined below.
my_list = [ 100, 200, 300, 'six hundred' ]



# That makes it a global object. We'll talk about that in another lab.


def give_list():
    # Does not accept any arguments
    # Returns all of items in the global object my_list unchanged
    first = (my_list[0:])
    return first

def give_first_item():
    # Does not accept any arguments
    # Returns the first item in the global object my_list as a string
    second = str(my_list[0])
    return second

def give_first_and_last_item():
    # Does not accept any arguments
    # Returns a list that includes the first and last items in the global object my_list
    third = [my_list[0], my_list[-1]]
    return third

def give_second_and_third_item():
    # Does not accept any arguments
    # Returns a list that includes the second and third items in the global object my_list
    fourth = [my_list[1], my_list[2]]
    return fourth

if __name__ == '__main__':   # This section also referred to as a "main block"
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())
