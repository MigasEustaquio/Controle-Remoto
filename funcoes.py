#Define biblioteca da GPIO
import RPi.GPIO as GPIO
 
#Define biblioteca de tempo
import time                           
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

lista_botoes = [16]
 

def inicializa_controle():
	
	for pino in lista_botoes:
		GPIO.setup(pino, GPIO.OUT)
		GPIO.output(pino, 1)
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, 1)
	
def finaliza_controle():
	
	GPIO.output(12, 0)
	for pino in lista_botoes:
		GPIO.output(pino, 0)
	 
def aperta_botao(pino):
	GPIO.output(pino, 0)
	time.sleep(0.5)
	GPIO.output(pino, 1)


