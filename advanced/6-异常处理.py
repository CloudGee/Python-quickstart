# try:
#   # 可能发生异常的代码块
#   sdfjlasfjdl
#   x = 1/0
# except ZeroDivisionError as err:
#   # 接收到 ZeroDivisionError 异常的处理逻辑
#   print("分母不能为0")
#   raise err
# except Exception as e:
#   print("Other error")
#   raise e
# else:
#   # 没有异常发生，要执行的代码
#   print("No error")
# finally:
#   # 不管有没有异常都会被执行
#   print("程序断开连接")

# def verify_data(data):
#   if not data:
#     raise ValueError("Data in verify_data func can not be empty.")

# verify_data(data="")

class ServerInternalError(Exception):
  pass

def server_error():
  raise ServerInternalError("Server has some problems.")

try:
 server_error()
except ServerInternalError as e:
  print(f"some error happen {e}")