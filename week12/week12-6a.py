def gcd(a, b):
  print(a, b)
  if a==0: return b
  if b==0: return a
  return gcd(b, a%b)

a = 1500000000 #把數字變很大,變成15億 老大
b = 2000000000 #把數字變很大,變成20億 老二
print( gcd(a, b))