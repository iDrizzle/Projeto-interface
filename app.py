import customtkinter as ctk
# Configurar aparencia

ctk.set_appearance_mode('dark')


# Criação das funcionalidades
def validar_login(): 
     
    usuario      = campo_usuario.get()
    senha        = campo_senha.get()
    if usuario == "Erik" and senha =="123456":
     resultado_login.configure(text ="Login feito com sucesso!" ,text_color="green")
    else:
     resultado_login.configure(text ="Login incorreto" ,text_color="red")

# Criação da janela principal

app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x300")

#labal - USUÁRIO
Label_usuario = ctk.CTkLabel(app, text="Usuario")
Label_usuario.pack(pady=10)

#entry - USUÁRIO
campo_usuario = ctk.CTkEntry(app, placeholder_text=" digite seu usuário")
campo_usuario.pack(pady=10)

#labal - SENHA
Label_senha = ctk.CTkLabel(app, text="Senha")
Label_senha.pack(pady=10)

#entry - SENHA
campo_senha = ctk.CTkEntry(app, placeholder_text=" digite sua senha")
campo_senha.pack(pady=10)

#button

botao_login = ctk.CTkButton(app, text="Login",command=validar_login)
botao_login.pack(pady=10)

#campo de feedback

resultado_login = ctk.CTkLabel(app,text="")
resultado_login.pack(pady=10)

# Iniciar a aplicação
app.mainloop()