from turtle import *
import colorsys
bgcolor("black")
tracer(400)
pensize(3)
h=0
goto(-300,200)

for i in range(700):
   c =colorsys.hsv_to_rgb(h,1,1)  
   fillcolor(c)
   begin_fill()
   left(122)
   forward(i*0.5)
   circle(5+i+0.3,90)
   circle(5+i*0.3,180)
   circle(5+i*0.3,90)
   left(5)
   backward(600-1*0.7) 
   end_fill()
   h+=0.005
done() 