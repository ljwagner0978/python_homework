import logging
def logger_decorator(func):
    def wrapper(*args, **kwargs):
    #return to a file ./decorator.log
        logger = logging.getLogger(func.__name__ + "_parameter_log")
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.FileHandler("./decorator.log","a"))
        logger.log(logging.INFO, f"function: {func.__name__}")
        if args:
            logger.log(logging.INFO, f"positional parameters: {list(args)}")
        else:
            logger.log(logging.INFO, f"positional parameters: none")
        if kwargs:
            logger.log(logging.INFO, f"keyword parameters: {tuple(kwargs.items())}")
        else:
            logger.log(logging.INFO, f"keyword parameters: none")  
        logger.log(logging.INFO, f"return: {func(*args, **kwargs)}")
    return wrapper

@logger_decorator
def hello_world():
    print("Hello, World!")
    
@logger_decorator
def positional_func(*args):
    return True

@logger_decorator
def keywords_func(**kwargs):
    return logger_decorator

    
hello_world()        
positional_func(75,85,95)
keywords_func(Tom=75, Dick=89, Angela=91)