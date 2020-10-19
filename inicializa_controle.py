#Define biblioteca da GPIO
import RPi.GPIO as GPIO                     
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
#Define os pinos da placa como saida
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
 
#rotina para acender o led
def liga_pino(pino_led):
    GPIO.output(pino_led, 1)
    return
 
liga_pino(16)
liga_pino(12)
