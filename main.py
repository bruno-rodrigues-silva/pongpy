#Pong Game
# Screen
import turtle

wn = turtle.Screen() #->wn is for windows
wn.title('Pong by Bruno Silva')
wn.bgcolor('black')
wn.setup(width=800,lenght=600)
wn.tracer(0)



#Main game loop
while True:
    wn.update()