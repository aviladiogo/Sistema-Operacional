from random import uniform
from threading import Thread
import time


First = [0, 0]
valida = False
def carrinho(nome):
    distancia = 0
    global valida
    while distancia <= 50:
        velocidade = uniform(1.1, 1.9)
        distancia= round(distancia, 2)

        if(valida == False):
            print("Piloto :",nome,distancia)
            distancia += velocidade
       
        if(distancia > First[0]):
            First[0] = distancia
            First[1] = nome

        if(distancia >= 50 and valida == False):
            valida = True
            print("O macaco ganhador foi: " + First[1])  

        time.sleep(0.3)
    
    
carrinho1 = Thread(target=carrinho,args=["Henry"])
carrinho2 = Thread(target=carrinho,args=["Matheus"])
carrinho3 = Thread(target=carrinho,args=["Diogo"])
carrinho4 = Thread(target=carrinho,args=["Bruno"])

print("ready")
time.sleep(1)
print("set")
time.sleep(1)
print("go")
time.sleep(1)

def thread():
    carrinho1.start()
    carrinho2.start()
    carrinho3.start()
    carrinho4.start()

thread()



