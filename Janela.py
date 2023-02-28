import customtkinter #Biblioteca que constrói telas

def clique():
    print("Fazer Login")



janela = customtkinter.CTk() #Cria uma janela
janela.geometry("800x500") #Define tamanho da janela

texto = customtkinter.CTkLabel(janela, text="Fazer Login") #Cria variavel Texto
texto.pack(padx=10, pady=10)#Mostrar na tela e dar espaçamento

email = customtkinter.CTkEntry(janela, placeholder_text="Seu E-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()