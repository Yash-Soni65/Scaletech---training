# Context manager using 3 rules enter, func , exit 

class MyContext:

    def _enter_(self):
        print("Entering context")
        return self

    def _exit_(self, exc_type, exc_value, traceback):
        print("Exiting context")


with MyContext():
    print("Inside context")


# context manager can be used directly by context library just by adding yield keyword

    from contextlib import contextmanager

@contextmanager
def my_context():
    print("Before")
    
    yield
    
    print("After")


with my_context():
    print("Inside")