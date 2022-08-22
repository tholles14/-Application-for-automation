import time
from tkinter import *
from tkinter import ttk
from pynput.keyboard import Key, Listener
from tkinter.filedialog import askopenfilename
import pyautogui
from keyboard import Controle
from tkcalendar import Calendar, DateEntry


# Tela principal
def telaPrincipal():
    global labelSelecione
    global variable
    global w
    # Label orientação
    labelSelecione = Label(win, text="Selecione qual automatização deseja realizar!", font=('Helvetica 13'))
    labelSelecione.pack()
    labelSelecione.place(relx=.02, rely=.13)

    variable = StringVar(win)
    variable.set("Mouse e Teclado")
    w = OptionMenu(win, variable, "Mouse e Teclado", "Em breve mais opções")
    w.pack()
    w.place(relx=.33, rely=.20)

    # Confirmação de registro
    buttonProsseguir.config(text='Prosseguir')

# Tela da seleção mouse e teclado
def mouseTeclado():
    global labelTamanho
    global labelRTamanho
    global labelPonteiro
    global labelPonteiroAtual
    global labelPonteiroDica
    global buttonOnOff
    global labelDocumento
    global labelDocumentoSelecionado
    global buttonAnexador
    global buttonExecutar
    global labelTutorial
    global checkLoop
    global chkValue
    # TAMANHO DA TELA
    labelTamanho = Label(win, text="Tamanho da sua tela: ", font=('Helvetica 13'))
    labelTamanho.pack()
    labelTamanho.place(relx=.01, rely=.01)

    labelRTamanho = Label(win,
                          text=f'{str(pyautogui.size()).replace("Size(width=", " ").replace("height=", "").replace(")", "").replace(" ", "")}',
                          font=('Helvetica 13'))
    labelRTamanho.pack()
    labelRTamanho.place(relx=.46, rely=.01)

    # Ponteiro do mouse
    labelPonteiro = Label(win, text="Pegar posição do ponteiro:", font=('Helvetica 13'))
    labelPonteiro.pack()
    labelPonteiro.place(relx=.01, rely=.06)

    # Ponteiro atual
    labelPonteiroAtual = Label(win, text="-", font=('Helvetica 13'))
    labelPonteiroAtual.pack()
    labelPonteiroAtual.place(relx=.60, rely=.06)

    # Dica de pegar posição
    labelPonteiroDica = Label(win, text="(Ative a opção, e aguarde 5 segundos\n"
                                        "que irá informar a posição do ponteiro!)", font=('Helvetica 8'))
    labelPonteiroDica.pack()
    labelPonteiroDica.place(relx=.01, rely=.12)

    # Botão desligado e ligado
    buttonOnOff = Button(text="ATIVAR", width=10, command=ligadoDesligado)
    buttonOnOff.pack(pady=10)
    buttonOnOff.place(relx=.6, rely=.13)

    # Selecione o documento
    labelDocumento = Label(win, text="Selecione o documento:", font=('Helvetica 13'))
    labelDocumento.pack()
    labelDocumento.place(relx=.01, rely=.2)

    # Documento selecionado
    labelDocumentoSelecionado = Label(win, text="-", font=('Helvetica 13'))
    labelDocumentoSelecionado.pack()
    labelDocumentoSelecionado.place(relx=.01, rely=.26)

    # Anexador de documentos
    buttonAnexador = Button(text="Anexar", width=10, command=anex)
    buttonAnexador.pack(pady=10)
    buttonAnexador.place(relx=.01, rely=.32)

    # Anexador de documentos
    buttonExecutar = Button(text="Executar", width=10, command=executarMT)
    buttonExecutar.pack(pady=10)
    buttonExecutar.place(relx=.01, rely=.40)

    # CheckLoop
    chkValue = BooleanVar()
    chkValue.set(True)
    checkLoop = Checkbutton(win, text='Loop', var=chkValue)
    checkLoop.place(relx=.70, rely=.40)

    # Documento selecionado
    labelTutorial = Label(win, text="""
Obs: Os comandos devem se escritos um por linha!
Comandos:
- moverpara(x,y)
- clicar
- escrever(texto)
- pressionar(tecla)
- atalho2(tecla1,tecla2)
- atalho3(tecla1,tecla2,tecla3)
Coloque esse comandos caso esteja muito rápido,\n ele causa um atraso em segundos:
- espere(1)
    """, font=('Helvetica 8'))
    labelTutorial.pack(pady=0)
    labelTutorial.place(relx=.15, rely=.48)

# Função de verificar a seleção e prosseguir
def prosseguir():
    if buttonProsseguir.config('text')[-1] == 'Prosseguir':
        buttonProsseguir.config(text='Voltar')
        labelSelecione.destroy()
        w.destroy()
        if variable.get() == "Mouse e Teclado":
            mouseTeclado()

    else:
        buttonProsseguir.config(text='Prosseguir')
        # apaga a guia atual
        # Mouse Teclado
        try:
            labelTamanho.destroy()
            labelRTamanho.destroy()
            labelPonteiro.destroy()
            labelPonteiroAtual.destroy()
            labelPonteiroDica.destroy()
            buttonOnOff.destroy()
            labelDocumentoSelecionado.destroy()
            buttonAnexador.destroy()
            labelDocumento.destroy()
            checkLoop.destroy()
            telaPrincipal()
            buttonExecutar.destroy()
            labelTutorial.destroy()
        except:
            pass

def ligadoDesligado():
    if buttonOnOff.config('text')[-1] == 'ON':
        buttonOnOff.config(text='ATIVAR')
    else:
        buttonOnOff.config(text='ON')
        for i in range(5):
            time.sleep(1)

        labelPonteiroAtual.config(
            text=f"{str(pyautogui.position()).replace('Point(x=', '').replace('y=', '').replace(')', '')}",
            font=('Helvetica 10'))
        buttonOnOff.config(text='ATIVAR')

def anex():
    global filename
    filename = askopenfilename()  # Isto te permite selecionar um arquivo
    labelDocumentoSelecionado.config(text=f"{filename}", font=('Helvetica 10'), foreground="blue")

def executarMT():
    tempo = 1
    if chkValue.get() == True:

        while True:
            #with open(f"{filename}", "r") as f:
            f = open(f"{filename}", 'r')
            for line in f:
                if line[:9] == "moverpara":
                    time.sleep(tempo)
                    posx = line[1 + line.find("("):line.find(",")]
                    posy = line[1 + line.find(","):line.find(")")]
                    pyautogui.moveTo(int(posx), int(posy))
                elif line[:6] == "clicar":
                    time.sleep(tempo)
                    pyautogui.click()
                elif line[:8] == "escrever":
                    time.sleep(tempo)
                    esq = line[1 + line.find("("):line.find(")")]
                    pyautogui.write(esq)
                elif line[:10] == "pressionar":
                    time.sleep(tempo)
                    esq = line[1 + line.find("("):line.find(")")]
                    pyautogui.press(esq)
                elif line[:7] == "atalho2":
                    time.sleep(tempo)
                    line = line.replace(' ','')
                    posx = line[1 + line.find("("):line.find(",")]
                    posy = line[1 + line.find(","):line.find(")")]
                    pyautogui.hotkey(posx, posy)
                elif line[:7] == "atalho3":
                    time.sleep(tempo)
                    line = line.replace(' ', '')
                    posx = line[1 + line.find("("):line.find(",")]
                    posxE = line[line.find("("):line.find(",")+1]
                    line = line.replace(f"{posxE}", "")
                    posy = line[1 + line.find("3"):line.find(",")]
                    posyE = line[line.find("3"):line.find(",")]
                    line = line.replace(f"{posyE}", "")
                    posz = line[1 + line.find(","):line.find(")")]
                    pyautogui.hotkey(posx, posy, posz)
    else:
        # with open(f"{filename}", "r") as f:
        f = open(f"{filename}", 'r')
        for line in f:
            if line[:9] == "moverpara":
                time.sleep(tempo)
                posx = line[1 + line.find("("):line.find(",")]
                posy = line[1 + line.find(","):line.find(")")]
                pyautogui.moveTo(int(posx), int(posy))
            elif line[:6] == "clicar":
                time.sleep(tempo)
                pyautogui.click()
            elif line[:8] == "escrever":
                time.sleep(tempo)
                esq = line[1 + line.find("("):line.find(")")]
                pyautogui.write(esq)
            elif line[:10] == "pressionar":
                time.sleep(tempo)
                esq = line[1 + line.find("("):line.find(")")]
                pyautogui.press(esq)
            elif line[:7] == "atalho2":
                time.sleep(tempo)
                line = line.replace(' ', '')
                posx = line[1 + line.find("("):line.find(",")]
                posy = line[1 + line.find(","):line.find(")")]
                pyautogui.hotkey(posx, posy)
            elif line[:7] == "atalho3":
                time.sleep(tempo)
                line = line.replace(' ', '')
                posx = line[1 + line.find("("):line.find(",")]
                posxE = line[line.find("("):line.find(",") + 1]
                line = line.replace(f"{posxE}", "")
                posy = line[1 + line.find("3"):line.find(",")]
                posyE = line[line.find("3"):line.find(",")]
                line = line.replace(f"{posyE}", "")
                posz = line[1 + line.find(","):line.find(")")]
                pyautogui.hotkey(posx, posy, posz)

# Criação da janela
win = Tk()
win.geometry("350x450")
win.title("Aplicação do Thalles")
p1 = PhotoImage(file='registrado.png')
win.iconphoto(False, p1)
win.resizable(width=False, height=False)

# Label orientação
labelSelecione = Label(win, text="Selecione qual automatização deseja realizar!", font=('Helvetica 13'))
labelSelecione.pack()
labelSelecione.place(relx=.02, rely=.13)

variable = StringVar(win)
variable.set("Mouse e Teclado")
w = OptionMenu(win, variable, "Mouse e Teclado", "","Em breve mais opções")
w.pack()
w.place(relx=.33, rely=.20)

# Confirmação de registro
buttonProsseguir = Button(text="Prosseguir", width=10, command=prosseguir)
buttonProsseguir.pack(pady=10)
buttonProsseguir.place(relx=.4, rely=.92)

win.mainloop()

