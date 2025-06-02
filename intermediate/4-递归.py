# 5! = 5*4*3*2*1
# 5 * (4!)
#      4 * (3!)
#           3 * (2!)
def jie_cheng(n):
  print(n)
  if n == 0:
    return 1
  else:
    return n*jie_cheng(n-1)


print(jie_cheng(3))