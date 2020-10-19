from flask import Flask
from flask_ask import Ask, statement
from funcoes.py import *
 
app = Flask(__name__)
ask = Ask(app, '/')
 
@ask.intent('LedIntent')
def led(color, status):
  if color.lower() not in pins.keys():
    return statement("I don't have {} light".format(color)) 
  GPIO.output(pins[color], GPIO.HIGH if status == 'on' else GPIO.LOW)
  return statement('Turning the {} light {}'.format(color, status))
  
@ask.intent('LigarLuz')
def ligarLuz():
    inicializa_controle()    #ainda não pode fazer aqui dentro pq não aperta o botão TV
    
    aperta_botao(16)
    
    finaliza_controle()

    return statement('Turning tv on')
    
@ask.intent('DesligarLuz')
def desligarLuz():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, 0)
    time.sleep(0.5)
    GPIO.output(16, 1)
    return statement('Turning tv off')


@ask.intent('LightIntent')
def desligarLuz(status):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH if status == 'on' else GPIO.LOW)
    return statement('Turning the led {}'.format(status))

 
if __name__ == '__main__':
  app.run(debug=True,port=6200)
  try:
    GPIO.setmode(GPIO.BCM)
    pins = {'red':12, 'yellow':10, 'green':11}
    for pin in pins.values(): 
      GPIO.setup(pin, GPIO.OUT)
    app.run(debug=True)
  finally:
    GPIO.cleanup()
