import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
def log_decorator(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        message = (
            f"function: {func.__name__}\n"
            f"positional parameters: {list(args) if args else None}\n"
            f"keyword parameters: {kwargs if kwargs else None}\n"
            f"return: {result}\n"
            )
        logger.log(logging.INFO, message)
        return result
    return wrapper
@log_decorator
def hello():
    print("Hello, World!")
@log_decorator
def positional(*args):
    return True
@log_decorator
def keywords(**kwargs):
    return log_decorator()
print(hello())
print(positional(1,2,3,4))
print(keywords(**{"key":"value"}))
