## Controle Remoto Raspberry Pi

Esse é um programa necessário para utilizar uma skill da alexa bem simples com a finalidade de mandar sinais infravermelhos e controlar diversos dispositivos ao alcance.

### Instalação rápida:

1.Execute o instalador.sh

2.Registre-se no site do [ngrok clicando aqui](https://dashboard.ngrok.com/signup) depois copie seu token de autorização e cole no terminal dessa forma: ./ngrok authtoken <TOKEN>

3.Inicie a aplicação alexaskill com o comando: python3 alexaskill.py

4.Em um terminal diferente inicie o serviço do ngrok com o comando: ./ngrok http 6000 (observe que devemos indicar a porta a ser direcionada pelo ngrok, essa porta deve ser a mesma especificada no final do código alexaskill.py e pode ser alterado sem preoblemas. Caso a porta desejada já esteja em uso o código não vai rodar e um aviso indicará o problema.)

5.Com a aplicação do ngrok iniciada o link de direcionamento será indicado no terminal utilizado por ele. Copie o endereço https e cole no local de endpoint de sua aplicação alexa no [console da Amazon clicando aqui](https://developer.amazon.com/alexa/console/ask)
