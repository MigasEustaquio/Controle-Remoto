#Define biblioteca da GPIO
import RPi.GPIO as GPIO
 
#Define biblioteca de tempo
import time                           
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
#Define os pinos da placa como saida
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
 
#rotina para acender o led
def liga_pino(pino_led):
    GPIO.output(pino_led, 1)
    return
 
#rotina para apagar o led
def desliga_pino(pino_led):
    GPIO.output(pino_led, 0)
    return
      
#liga_pino(16)
#liga_pino(12)
#time.sleep(0.5)

#Apertar o botao TV antes

desliga_pino(16)
time.sleep(0.5)
liga_pino(16)

#time.sleep(0.5)
#desliga_pino(12)
#desliga_pino(16)
