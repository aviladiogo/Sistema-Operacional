from random import *
import _thread
import time
import turtle
from turtle import *




First = [0, 0]
valida = False


def carrinho(nome, pessoa):
    distancia = 0
    global valida
    while distancia <= 700:
        velocidade = randint(25, 50)
        if(valida == False):
            print("Piloto :",pessoa,distancia)
            distancia += velocidade
            nome.fd(velocidade)
       
        if(distancia > First[0]):
            First[0] = distancia
            First[1] = pessoa

        if(distancia >= 700 and valida == False):
            valida = True
            print("O macaco ganhador foi: " + First[1])  

        time.sleep(0.3)
    

Matheus = turtle.Turtle()
Matheus.color("blue")
Matheus.shape("turtle")
Matheus.goto(0,-100)

Henry = Matheus.clone()
Henry.color("red")
Henry.goto(0,-50)

Diogo = Matheus.clone()
Diogo.color("orange")
Diogo.goto(0,0)

Bruno = Matheus.clone()
Bruno.color("purple")
Bruno.goto(0,50)

turtle.speed(0)
showturtle()

#carrinho1 = Thread(target=carrinho,args=(Matheus, )) # explicar a função

#carrinho2 = Thread(target=carrinho,args=(Henry, ))
#carrinho3 = Thread(target=carrinho,args=(Diogo, ))
#carrinho4 = Thread(target=carrinho,args=(Bruno, ))

print("ready")
time.sleep(1)
print("set")
time.sleep(1)
print("go")
time.sleep(1)
#print(Matheus) #<turtle.Turtle object at 0x0000020D3BF97FD0>
#print(Henry) #<turtle.Turtle object at 0x0000020D3DD15150>
#print(Diogo) #<turtle.Turtle object at 0x0000020D3DD14850>
#print(Bruno) #<turtle.Turtle object at 0x0000020D3DD164A0>

def thread():
    _thread.start_new_thread(carrinho,(Matheus,"Matheus"))
    _thread.start_new_thread(carrinho,(Henry,"Henry"))
    _thread.start_new_thread(carrinho,(Diogo, "Diogo") )
    _thread.start_new_thread(carrinho,(Bruno, "Bruno"))
    turtle.done()

thread()
