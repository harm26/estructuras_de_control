def es_primo(num):
   if num == 1:
       return False
   elif num == 2:
       return True
   else:
       for i in range(2, num):
           if num % i == 0:
               return False
       return True

res = es_primo(11)
if res:
    print("es primo")
else:
    print("no es primo")

