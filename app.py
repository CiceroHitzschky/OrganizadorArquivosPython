from organizadorFuncoes import *
import pyautogui as pg
from tkinter import *


menu = Tk() # Inicialização
menu.title("Organizador de Arquivos") # Título

# Ação do Botão

def organizar(num_pas, num_nao_mov):

    numero_pastas = num_pas
    numero_nao_movidos = num_nao_mov 
    analisar_pasta()
    obter_ext()
    criar_pastas(numero_pastas)
    organizar_dir(numero_nao_movidos)

# Configurações de Layout do Menu
# Centraliza a GUI
largura = 400
altura = 200
largura_tela = menu.winfo_screenwidth() #Obtém a largura da tela
altura_tela = menu.winfo_screenheight() # obtém altura

posx = (largura_tela - largura)/2 # Define o centro horizontal
posy = (altura_tela - altura)/2 # Define o centro vertical

posx = int(posx)
posy = int(posy)

#menu.minsize(largura, altura)

menu.geometry(f"+{posx}+{posy}")

# Botão 
btn = Button(
            menu,
            text = "Organizar Pasta ",
            font= " Helvetica 20",
            command = lambda: organizar(num_pas = num_dir, num_nao_mov = num_naomov),
            anchor= S,
            justify= CENTER
        ).pack(pady=20, padx=20)

menu.mainloop() # mantém o app aberto