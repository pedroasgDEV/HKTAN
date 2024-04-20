from tkinter import *
from verifyInput import Input
from tkinter import messagebox


def ANcaptcha(): 
    # Criando a janela
    root = Tk()
    root.title("ANcaptcha")
    
    # Carregando a imagem
    image = PhotoImage(file="img.png")
    
    # Exibindo a imagem
    label_image = Label(root, image=image)
    label_image.pack()

    # Descrevendo o que é para fazer
    label = Label(root, text="Descreva essa imagem em 5 palavras:")
    label.pack()

    # Campo de entrada
    entry = Entry(root, width=50)
    entry.pack()
    
    # Botão de submissão
    submit_button = Button(root, text="Submit", command=lambda: submit_text(entry.get(), root))
    submit_button.pack()
    
    # Rodando a aplicação
    root.mainloop()
    
def submit_text(txt, root):
    #processa a entrada
    text = Input(txt)
    
    #Verifica se a Quantidade de palavras é valida
    if len(text.str) < 5: 
        messagebox.showerror("Erro", "Qunatidade de palavras invalidas")
        return
    
    #Verifica se tem alguma palavra que se repete
    for n in text.str:
        contador = -1
        for m in text.str:
            if n == m:
                contador += 1
        if contador > 0:
            messagebox.showerror("Erro", "A palavra " + n + " está se repetindo")
            return
    
    #Valida as palavras
    erros = text.verifyInput()
    
    #Mostra as palavras erradas
    if len(erros) > 0:
        msg = "As palvras: "
        for str in erros:
            msg += str + " "    
        msg += "são invalidas"
        messagebox.showerror("Erro", msg)
        return
        
    #Se tiver tudo certo grava as informações em um txt e finaliza o captcha
    if len(text.str) >= 5 and len(erros) == 0:
        
        #abre o arquivo e grava
        with open("img.txt", "a") as arquivo:
            for item in text.str:
                arquivo.write(item + "\n")
        
        #finaliza o captcha
        root.quit()

ANcaptcha()