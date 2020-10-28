from flask import Flask
from flask_ask import Ask, statement
from funcoes import *

inicializa_controle()
statusTela = 'off'
statusTV = 'off'
repetirStatus = ''
repetirDevice = ''
 
app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
    speech_text = 'Welcome to the Raspberry Pi alexa automation.'
    return statement(speech_text)

@ask.intent('HelloWorldIntent')
def helloWorldIntent(device, status):
  return statement("Hello")

@ask.intent('AMAZON.CancelIntent')
def helloWorldIntent(device, status):
  return statement("Cancel")
  
@ask.intent('AMAZON.StopIntent')
def helloWorldIntent(device, status):
  return statement("stop")
  
@ask.intent('AMAZON.NavigateHomeIntent')
def helloWorldIntent(device, status):
  return statement("navigation")

@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return statement(speech_text)


@ask.intent('TurnScreen') #Liga a TV ou a tela
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
      

@ask.intent('LigarTela') #Liga a TV ou a tela
def ligarTela(status, device):
  global statusTela
  global statusTV
  global repetirDevice
  global repetirStatus
    
  if device == 'tela':
    estado = statusTela
  else:
    estado = statusTV
    
  repetirDevice = device
      
  if status == 'ligar':
    repetirStatus = 'ligar'
    if estado == 'off':
      if device == 'tela':
        aperta_botao(15, 0.5)
        statusTela = 'on'
      else:
        aperta_botao(16, 0.5)
        statusTV = 'on'
      return statement('Ligando a {}'.format(device))
    else:
      return statement('A {} já está ligada'.format(device))
  else:
    repetirStatus = 'desligar'
    if estado == 'on':
      if device == 'tela':
        aperta_botao(15, 0.5)
        statusTela = 'off'
      else:
        aperta_botao(16, 0.5)
        statusTV = 'off'
      return statement('Desligando a {}'.format(device))
    else:
      return statement('A {} já está desligada'.format(device))


@ask.intent('ConfirmScreen')
def ligarTela(device, status):
    
  if device == 'screen':
    aperta_botao(15, 0.5)
    return statement("I'm sorry. Trying to turn {} the screen again".format(status))
  else:
    aperta_botao(16, 0.5)
    return statement("I'm sorry. Trying to turn {} the TV again".format(status))
    
    
@ask.intent('ConfirmarTela')
def ligarTela(device, status):
    
  if device == 'tela':
    aperta_botao(15, 0.5)
    if status == 'ligar':
      return statement("Me desculpe por isso. Tentando ligar a tela novamente")
    else:
      return statement("Me desculpe por isso. Tentando desligar a tela novamente")
  else:
    aperta_botao(16, 0.5)
    if status == 'ligar' or status == 'ligada' or status == 'ligou':
      return statement("Me desculpe por isso. Tentando ligar a tv novamente")
    else:
      return statement("Me desculpe por isso. Tentando desligar a tv novamente")
      
      
@ask.intent('Repetir')
def repetir():
    
  global repetirStatus
  global repetirDevice
    
  if repetirDevice == '' or repetirStatus == '':
    return statement("Eu ainda não realizei nenhuma ação")
    
  if repetirDevice == 'tela':
    aperta_botao(15, 0.5)
    if repetirStatus == 'ligar':
      return statement("tudo bem. Tentando ligar a tela novamente")
    else:
      return statement("Tudo bem. Tentando desligar a tela novamente")
  else:
    aperta_botao(16, 0.5)
    if repetirStatus == 'ligar':
      return statement("Tudo bem. Tentando ligar a tv novamente")
    else:
      return statement("Tudo bem. Tentando desligar a tv novamente")


@ask.intent('MudarVolume') #Alterar essa funcao para mudar quantidades maiores de volume por vez
def mudarVolume(volume):
  i=0
  if volume == 'up':
    while i < 5:
      aperta_botao(11, 0.5) #mandar pino correto
      time.sleep(0.5)
      i+=1
    return statement('Turning the volume {}'.format(volume))
  else:
     while i < 5:
       aperta_botao(11, 0.5) #mandar pino correto
       time.sleep(0.5)
       i+=1
     return statement('Turning the volume {}'.format(volume))

 
if __name__ == '__main__':
  app.run(debug=True,port=6200)
  try:
    app.run(debug=True)
  finally:
    finaliza_controle()
    GPIO.cleanup()
