#Define biblioteca da GPIO
import RPi.GPIO as GPIO

#Define biblioteca de tempo
import time                           
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

lista_botoes = [16, 11]
#canais = {1:18}
 

def inicializa_controle():
	for pino in lista_botoes:
		GPIO.output(pino, 1)
	GPIO.output(12, 1)
	return
	
def finaliza_controle():
	GPIO.output(12, 0)
	for pino in lista_botoes:
		GPIO.output(pino, 0)
	return

def aperta_botao(pino, tempo):
	GPIO.output(pino, 0)
	time.sleep(tempo)
	GPIO.output(pino, 1)
	return


#def comando(canal, botao):
#	aperta_botao(canais[canal], 0.3)
#	time.sleep(0.5)
#	aperta_botao(botao, 0.3)
#
#def aprende_comando(canal, botao):
#	aperta_botao(canais[canal], 2)
#	time.sleep(1)


for pino in lista_botoes:
	GPIO.setup(pino, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
