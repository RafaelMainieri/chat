import flet as ft

def main(pagina):
    def enviar_mensagem_tunel(mensagem):
        # adicionar mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem) 
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        pagina.pubsub.send_all(f'{nome_usuario.value}: {campo_mensagem.value}')
        campo_mensagem.value = '' # limpe o campo mensagem
        pagina.update()

    def entrar_chat(evento):
        popup.open = False #fechar o popup
        pagina.remove(botao_iniciar) #remover o botao de iniciar do chat
        pagina.remove(texto) #remover o titulo
        pagina.add(chat) #criar o chat
        pagina.pubsub.send_all(f'{nome_usuario.value} entrou no chat')
        pagina.add(linha_enviar) #criar o botao de enviar
        pagina.update()

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    texto = ft.Text('Hashzap')
    
    chat = ft.Column()
    
    #campo de enviar mensagem
    campo_mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    
    #popup
    titulo_popup = ft.Text('Bem vindo ao Hashzap')
    nome_usuario = ft.TextField(label='Escreva seu nome no chat')
    botao_entrar = ft.ElevatedButton('Entrar no Chat', on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False, #pra nao começar o chat com o popup aberto
        modal=True, #centralizar o popup
        title = titulo_popup, #titulo do popup
        content = nome_usuario, #oq vai ta escrito pro usuario
        actions=[botao_entrar], #botao pra entrar no chat
    )

    botao_iniciar = ft.ElevatedButton(text='Iniciar Chat', on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)
    