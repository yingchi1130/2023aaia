a = 120
# 1 2 3 4 5 6 8 10 12 15 ... for迴圈
ans = 0 #迴圈前面,0個
for i in range(1, a+1): # 包含1...a本身
  if a%i==0:
    print( i, end=' ')
    ans += 1 #迴圈裡面,ans增加
print('有幾個整除? ', ans) #迴圈後面,把ansa拿來用