class MyClass:
  def public_mythod(self):
    print("This is a public func.")

  def __private_method(self):
    print("This is a private func.")

classa = MyClass()
classa.public_mythod()
classa._MyClass__private_method()