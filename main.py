import flet as ft
import os

#Função para abrir a pagina
def main(pagina): # def seria uma função, main é a definição de principal, (pagina) seria o nome da pagina
    titulo = ft.Text('RENT Zap') # Título da Pagina
    titulo_janela = ft.Text('Welcomidos!')
    
    def enviar_msg_tunel(mensagem):
        texto_msg = ft.Text(mensagem)
        chat.controls.append(texto_msg)
        pagina.update()

    pagina.pubsub.subscribe(enviar_msg_tunel)

    def enviar_msg(evento3):
        mensagem = ('{} : {}'.format(campo_nome.value,campo_msg.value))
        pagina.pubsub.send_all(mensagem)
        campo_msg.value = ''
        pagina.update()


    campo_msg = ft.TextField(label='Digite sua mensagem:', on_submit= enviar_msg)
    botao_enviarmsg = ft.ElevatedButton('Enviar', on_click=enviar_msg)
    chat = ft.Column()
    linha_msg = ft.Row([botao_enviarmsg, campo_msg])

    def entrar_chat(evento2):
        janela.open = False
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        pagina.pubsub.send_all('{} Entrou'.format(campo_nome.value))
        pagina.add(chat)
        pagina.add(linha_msg)
        pagina.update()

    campo_nome = ft.TextField(label='Digite seu nome:', on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton('Entrar',on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome,
        actions=[botao_entrar]
    )



    def abrir_janela(evento1):
        pagina.dialog = janela
        pagina.open(janela)
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Fala Comigo', on_click=abrir_janela)

    pagina.add(titulo)
    pagina.add(botao_iniciar)


ft.app(target=main, port=int(os.environ.get("PORT", 8000)), view=ft.WEB_BROWSER)