import flet as ft

def main(pagina):
    titulo = ft.Text("Hashzap")
    
    # websocket - Túnel de comunicação
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = (f"{nome_usuario}: {texto_campo_mensagem}")
        pagina.pubsub.send_all(mensagem)
        
        # Limpa a caixa de enviar mensagem:
        campo_enviar_mensagem.value = ""
        pagina.update()
    
    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    chat = ft.Column() # Textos aparecerão um abaixo do outro
    
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar]) # Coloca ambos na mesma linha
    
    def entrar_chat(evento):
        # Sumir o Popup
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        
        # Carregar o chat
        pagina.add(chat)
        pagina.add(linha_enviar)
        
        # Info que usuário entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat!"
        pagina.pubsub.send_all(mensagem)
        
        pagina.update()
    
    titulo_popup = ft.Text("Bem vindo ao Hashzap!")
    caixa_nome = ft.TextField(label="Insira o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, 
                           content=caixa_nome, 
                           actions=[botao_popup])
    
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    pagina.add(titulo)
    pagina.add(botao)
    
ft.app(main, view=ft.WEB_BROWSER)