from math import sin as sinus
from math import cos as cosine
from math import radians
def sin(degrees):
    return(sinus(radians(degrees)))
def cos(degrees):
    return(cosine(radians(degrees)))
def x_ray_calculation(a, C):
    "Вычисляет X луча с данным в параметрах углом(a), и длиной луча(C)."
    return(sin(a)*C)
def y_ray_calculation(a, C):
    "Вычисляет Y луча с данным в параметрах углом(a), и длиной луча(C)."
    return(cos(a)*C)
import time
if __name__=="__main__":
    while True:
        print("Расчёт лучей.")
        S=float(input("Сколько шагов пройдёт луч: "))
        a=float(input("Под каким градусом: "))
        X=x_ray_calculation(a, S)
        Y=y_ray_calculation(a, S)
        print("Считаем", end="")
        for i in range(3):
            print(end=".")
            time.sleep(0.3)
        print("\n")
        print("X луча:"+str(X)+", Y луча:"+str(Y))
        input()
        print("\n"*10)
        print("\n"*10)
        print("\n"*10)
        print("\n"*10)
        print("\n"*10)
