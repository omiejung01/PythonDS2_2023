
# range (6) --> [0,1,2,3,4,5]

#range (1,6) --> [1,2,3,4,5]


def sum1(num): # 1 + 2 + 3 + ... + num
   sum = 0
   # [1, 2 , 3, 4, 5]
   for x in range(1, num+1):
       sum += x
   return sum


def sum2(num):
   if num == 0:
       return 0
   elif num == 1:
       return 1
   else:
       return num + sum2(num - 1)
   # 5 + 4 + 3 + 2 + 1


def factorial(num):
   if num == 0:
       return 1
   elif num == 1:
       return 1
   else:
       return num * factorial(num - 1)
   # 5 * 4 * 3 * 2 * 1
   # A and B
   # A B
   # B A --> 2
   # A B C --> A B C , A C B, B A C, B C A, C A B , C B A --> 6


def run():
   #print(sum1(5)) # 1 + 2 + 3 + 4 + 5 = 15
    #print(sum2(6))
   print(factorial(7))

   str = 'Hello'
   # 0 -> H, 1 -> e, 2 -> l, 3 -> l, 4->o, 5 --> Error

   print(str[5])

