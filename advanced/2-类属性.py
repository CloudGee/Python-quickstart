class MyClass:
  def __init__(self, public_attribute, private_attribute):
    self.public_attribute = public_attribute
    self.__private_attribute = private_attribute

  def get_private(self):
    return self.__private_attribute

classA = MyClass("public a", "private a")
print(classA.public_attribute)
print(classA.get_private())