## python decorators

1. ```python
   def decorator_function(original_function):
       def wrapper_function(*args, **kwargs):
           return original_function(*args, **kwargs)
       return wrapper_function

    # examples
    def func1():
        return 'do something'
    func1 = decorator_function(func1)
    func1()

    @decorator_function
    def func2():
        return 'do something'
    func2()
   ```

2. ```python
   class decorator_class(object):
       def __init__(self, original_function):
           self.original_function = original_function

       def __call__(self, *args, **kwargs):
           return self.original_function(*args, **kwargs)

    # examples
    def func1():
        return 'do something'
    func1 = decorator_class(func1)
    func1()

    @decorator_class
    def func2():
        return 'do something'
    func2()
   ```
