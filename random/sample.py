import random
a = random.choice( [1,2,3] ) #=> 1 or 2 or 3
b = random.sample( [1,3,5], k=2 ) #=> [5,3], [1,5] など。重複しない。
print(a, b)
