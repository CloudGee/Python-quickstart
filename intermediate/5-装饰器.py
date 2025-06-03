from functools import wraps
# def my_decorator(func):
#   def wrapper(*args, **kwargs):
#     print("Start")
#     func(*args, **kwargs)
#     print("Finish")
#   return wrapper

# # say_hello = my_decorator(say_hello)
# @my_decorator
# def say_hello():
#   """
#   This is say hello func.
#   """
#   print("Hello!")

# say_hello()

def repeat_decorator(n):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator

# say_hello = repeat_decorator(10)(say_hello)
@repeat_decorator(10)
def say_hello():
  """
  This is say hello func.
  """
  print("Hello!")

# say_hello()

print(say_hello.__name__)