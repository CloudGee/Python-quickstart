# class MyClass:
#   """
#   MyClass
#   """
#   def __init__(self):
#     self.a = "hello"
#     self.b = "baba"

#   def __delattr__(self, name):
#     if name == "a":
#       print("Don't allow to delete.")
#     else:
#       object.__delattr__(self, name)

#   def __getattribute__(self, name):
#     if name == "a":
#       return "You can not get this attribute."
#     else:
#       return object.__getattribute__(self, name)

#   def __str__(self):
#     return "aaa"

# obj = MyClass()
# print(obj)
# # print(obj.__class__)
# # del obj.a
# # del obj.b
# print(obj.a)
# print(obj.b)
# print(obj.__doc__)

# class MyBaseClass:
#   @classmethod
#   def __init_subclass__(cls, **kwargs):
#     super().__init_subclass__(**kwargs)
#     cls.my_attribute = "Hello world!"

# class MySubClass(MyBaseClass):
#   pass

# print(MySubClass.my_attribute)

# class MyClass:
#   def __init__(self):
#     self.data = {}

#   def __getitem__(self, key):
#     return self.data[key]

#   def __setitem__(self, key, value):
#     self.data[key] = value

# obj = MyClass()
# obj["Name"] = "myclass"
# print(obj["Name"])

# class MyCallable:
#   def __call__(self, x):
#     return x**2

# obj = MyCallable()
# print(obj(5))

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __eq__(self, other):
#     if isinstance(other, Person):
#       return self.name == other.name and self.age == other.age
#     return NotImplemented


# person1 = Person("Alice", 21)
# person2 = Person("Alice", 21)
# print(person1 != person2)