def bisiesto(año):
    if año%4==0 & año%100==0 & año%400==0:
        return "Es Bisiesto"
    else:
        return "No es Bisiesto"

print(bisiesto(1997))