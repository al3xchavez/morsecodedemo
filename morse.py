from machine import Pin;
import time;

#Name: Alex Chavez
#Link: https://github.com/al3xchavez/morsecodedemo

pinled=Pin(25, Pin.OUT)

def dot():
    pinled.on()
    time.sleep(1)
    pinled.off()
    time.sleep(1)
def dash():
    pinled.on()
    time.sleep(3)
    pinled.off()
    time.sleep(1)
def l_space():
    time.sleep(2)
def w_space():
    time.sleep(4)
def A():
    dot()
    dash()
    l_space()
def L():
    dot()
    dash()
    dot()
    dot()
    l_space()
def E():
    dot()
    l_space()
def X():
    dash()
    dot()
    dot()
    dash()
    l_space()
def C():
    dash()
    dot()
    dash()
    dot()
    l_space()
def H():
    dot()
    dot()
    dot()
    dot()
    l_space()
def V():
    dot()
    dot()
    dot()
    dash()
    l_space()
def Z():
    dash()
    dash()
    dot()
    dot()
    l_space()


while True:
  A()
  L()
  E()
  X()
  w_space()
  C()
  H()
  A()
  V()
  E()
  Z()
  break

