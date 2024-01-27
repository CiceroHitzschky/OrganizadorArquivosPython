import os

# Criando arquivo de relatório
with open('relatorio.txt', 'w') as relatorio:
    titulo = " Relatório de Automação "
    relatorio.write(titulo+"\n"+len(titulo)*"-")


#Analisando arquivos
lista_arquivos = os.listdir()

def analisar_pasta():
    texto = f"{len(lista_arquivos)} arquivos ou pastas foram identificados.\n"
    
    with open('relatorio.txt', 'a') as relatorio:
        return relatorio.write('\n'+texto+"\n"+len(titulo)*"-")

# Criando conjunto de extensões
exts = set() # Lista de extensões

def obter_ext():
    for arquivo in lista_arquivos:
        arquivo = arquivo.split('.')
        tamanho_arquivo = len(arquivo)
        ext = arquivo[tamanho_arquivo-1] 
        exts.add(ext)

    with open('relatorio.txt', 'a') as relatorio:
        _mensagem = f"\nNa pasta foram identificadas {len(ext)} novas extensões de arquivo."
        return relatorio.write(_mensagem+"\n"+len(titulo)*"-")

# Criando Pastas 
num_dir = 0
nome_dir = set()

def criar_pastas(num_dir):
    for ext in exts:
        if os.path.isdir(ext):
            pass
        else:
            try:
                os.mkdir(ext)
                nome_dir.add(ext)
                num_dir +=1
            except:
                pass
                #pg.alert(text =f"{extensao} não possui extensão!", title = "Erro ao criar diretório!!")
    
    if num_dir == 0:
        with open('relatorio.txt', 'a') as relatorio:
            _mensagem = f"\nForam criados {num_dir} novas pastas!" +"\n"+"\n".join(nome_dir)
            return relatorio.write(_mensagem+"\n"+len(titulo)*"-")
    else:
        with open('relatorio.txt', 'a') as relatorio:
            _mensagem = f"\nForam criados {num_dir} novas pastas! São elas: " +"\n"+"\n".join(nome_dir)
            return relatorio.write(_mensagem+"\n"+len(titulo)*"-")



# Organizar Arquivos
excessoes = set()
num_naomov = 0

def organizar_dir(num_naomov):
    for arquivo in lista_arquivos:
        for ext in exts:
            if ext in arquivo:
                try:
                    os.rename(f"{arquivo}", f"{ext}/{arquivo}")
                except:
                    excessoes.add(ext)
                    num_naomov +=1
    with open('relatorio.txt','a') as relatorio:
        if excessoes == set():  
                relatorio.write("\n\nTodos os arquivos foram movidos"+"\n"+len(titulo)*"-")
        else:
            relatorio.write(f"\n\nNão foi possível mover os {num_naomov} arquivos a seguir:"+"\n"+"\n".join(excessoes))
            relatorio.write("\nPossivelmente já eram pastas criadas!"+"\n"+len(titulo)*"-")