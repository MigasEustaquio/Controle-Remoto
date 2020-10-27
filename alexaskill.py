from flask import Flask
from flask_ask import Ask, statement
from funcoes import *

inicializa_controle()
statusTela = 'off'
statusTV = 'off'
 
app = Flask(__name__)
ask = Ask(app, '/')
    

@ask.intent('LigarTela') #Liga a TV ou a tela
def ligarTela(status, device):
  global statusTela
  global statusTV
    
  if device == 'screen':
    estado = statusTela
  else:
    estado = statusTV
      
  if status == 'on':
    if estado == 'off':
      if device == 'screen':
        aperta_botao(15, 0.5)
        statusTela = 'on'
      else:
        aperta_botao(16, 0.5)
        statusTV = 'on'
      return statement('Turning on the {}'.format(device))
    else:
      return statement('The {} is already turned on'.format(device))
  else:
    if estado == 'on':
      if device == 'screen':
        aperta_botao(15, 0.5)
        statusTela = 'off'
      else:
        aperta_botao(16, 0.5)
        statusTV = 'off'
      return statement('Turning off the {}'.format(device))
    else:
      return statement('The {} is already turned off'.format(device))


@ask.intent('ConfirmarTela')
def ligarTela(device, status):
    
  if device == 'screen':
    aperta_botao(15, 0.5)
    return statement("I'm sorry. Trying to turn {} the screen again".format(status))
  else:
    aperta_botao(16, 0.5)
    return statement("I'm sorry. Trying to turn {} the TV again".format(status))


@ask.intent('MudarVolume') #Alterar essa funcao para mudar quantidades maiores de volume por vez
def mudarVolume(volume):
  i=0
  if volume == 'up':
    for i < 5:
      aperta_botao(11, 0.5) #mandar pino correto
      time.sleep(0.5)
      i+=1
    return statement('Turning the volume {}'.format(volume))
   else:
     for i < 5:
       aperta_botao(11, 0.5) #mandar pino correto
       time.sleep(0.5)
       i+=1
     return statement('Turning the volume {}'.format(volume))

 
if __name__ == '__main__':
  app.run(debug=True,port=6100)
  try:
    app.run(debug=True)
  finally:
    finaliza_controle()
    GPIO.cleanup()
