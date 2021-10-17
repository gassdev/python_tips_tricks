# Decorators

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(f'{prefix} executed before {original_function.__name__}')
            result =  original_function(*args, **kwargs)
            print(f'{prefix} executed after {original_function.__name__}')
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('TESTING:')
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

display_info('Developer', 18)
display_info('Administrator', 25)

def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

# display_info = prefix_decorator('TRYING:')(display_info)
# display_info('Administrator', 25)

# display_info_func = prefix_decorator('DISPLAY:')
# display_info = display_info_func(display_info)
# display_info('Developer', 18)
