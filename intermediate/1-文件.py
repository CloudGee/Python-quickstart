try:
  with open("example.txt", "x") as file_object:
    file_object.write("This is a try.\n")
    print("write data into file scuessfully.")
except FileExistsError:
  print("File already exist, pls change a file name.")
