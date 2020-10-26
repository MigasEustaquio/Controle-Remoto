from flask import Flask
from flask_ask import Ask, statement
from funcoes.py import *
 
app = Flask(__name__)
ask = Ask(app, '/')

statusTela = 'off'
statusTV = 'off'

inicializa_controle()
  
@ask.intent('LigarLuz')
def ligarLuz():
    #inicializa_controle()
    
    aperta_botao(16, 0.5)
    
    #finaliza_controle()

    return statement('Turning tv on')
    

@ask.intent('LigarTela')
def ligarTela(status):
    if status == 'on':
      if statusTela == 'off':
        aperta_botao(16, 0.5) #para fins de teste está apontando para o botão da tv
        statusTela = 'on'
        return statement('Turning screen on')
      else:
        return statement('Screen is already turned on')

    if status == 'off':
      if statusTela == 'on':
        aperta_botao(16, 0.5) #para fins de teste está apontando para o botão da tv
        statusTela = 'off'
        return statement('Turning screen off')
      else:
        return statement('Screen is already turned off')


@ask.intent('MudarVolume') #Alterar essa função para mudar quantidades maiores de volume por vez
def mudarVolume(volume):
    if volume == 'up':
      aperta_botao(0, 0.5) #mandar pino correto
      return statement('Turning the volume {}'.format(volume))
    else:
      comando(0, 0.5) #mandar pino correto
      return statement('Turning the volume {}'.format(volume))

 
if __name__ == '__main__':
  app.run(debug=True,port=6200)
  try:
    app.run(debug=True)
  finally:
    finaliza_controle()
    GPIO.cleanup()
