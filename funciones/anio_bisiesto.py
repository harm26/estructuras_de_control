# 2000 fue bisiesto

def es_bisiesto(anio):
    if anio == 1:
        return "es bisiesto"
    elif(anio % 4 ==0):
        return "es bisiesto"
    else:
        return "no es bisiesto"

res = es_bisiesto(2001)
print(res)