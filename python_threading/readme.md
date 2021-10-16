## run code concurrently using threading module

We can do concurrent execution using **threading** or **concurrent.futures** modules

1. ```python
   # example 1
   # import threading module
   import threading

   # example
   t1 = threading.Thread(target=callable_object)
   t2 = threading.Thread(target=callable_object)

   t1.start()
   t2.start()
   ```

2. ```python
    # example 2
    import concurrent.futures

    # example
    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(callable_object, secs)

   ```
