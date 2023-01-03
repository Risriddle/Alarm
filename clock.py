from os import system
from time import sleep
import time
from playsound import playsound


print("set the clock at current time:")
a=int(input("enter the hour: "))
b=int(input("enter the minutes: "))
c=int(input("enter the seconds: "))

print("enter the time for which you wish to set the alarm: ")
a1=int(input("enter the hour: "))
b1=int(input("enter the minutes: "))
c1=int(input("enter the seconds: "))  

while(1):

 
  print(a,":",b,":",c)
  sleep(0.5)
  system("clear")
  if(b==59 and c==59):
   b=0
   c=0
   a=0
  if(c==59):
   c=0
   b=b+1
  if(a==a1 and b==b1 and c==c1):
        print("ALARM!!!")
        playsound("alarm.mp3")
        a=a1
        b=b1
        c=c1+27
  print(a,":",b,":",c)
  sleep(0.5)
  system("clear") 
  c=c+1
  if(b==59):
   a=a+1
   b=0
  if(a==24):
   a=0
   b=0
  
      

      

  
