#Objetivo: criar um protótipo utilizando a metodologia RAD.
'''
Aluno: Daniel Lopes da Costa // matrícula: 202108093785
Estácio maracanã noite
'''
#importando bibliotecas utilizadas no projeto
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3 as conector #apelido
from tkinter import messagebox
from time import sleep

#Tela principal menu
janela = tk.Tk()
janela.title('Registro de Alunos')
janela.geometry('800x500+280+100')
janela.iconbitmap(default="icones\\icon.ico")
janela.rowconfigure([0,1,2,3], weight=1)
janela.columnconfigure([0, 1], weight=1)
janela.resizable(False, False)

#importando as imagens do projeto
img_fundo_menu = PhotoImage(file='imagens\\fundo menu (1).png')
img_botao_reg = PhotoImage(file='imagens\\BOTAO REGISTRAR.png')
img_botao_cons = PhotoImage(file='imagens\\BOTAO CONSULTAR.png')
img_botao_listar = PhotoImage(file='imagens\\BOTAO LISTAR.png')
img_fundo_reg = PhotoImage(file='imagens\\fundo registro (1).png')
img_botao_reg2 = PhotoImage(file='imagens\\BOTAO REGISTRAR 2.png')
img_fundo_busca = PhotoImage(file='imagens\\fundo Consulta de alunos.png')
img_fundo_lista = PhotoImage(file='imagens\\fundo lista de alunos.png')
img_botao_cons2 = PhotoImage(file='imagens\\botao de busca2.png')

#Criação de Labels menu (carregando a imagem)
lab_fundo_menu = Label(janela, image=img_fundo_menu)
lab_fundo_menu.pack()
#lab_criador = Label(janela, text='Criado por Daniel Lopes!')
#lab_criador.place(width=200, height=500)

###FUNÇÕES
'''BANCO DE DADOS AQUI'''
# abertura da conexção
conexao = conector.connect('bd_alunos.db')
cursor = conexao.cursor()
cursor.execute("CREATE TABLE if not exists cadastro(matricula INTEGER PRIMARY KEY NOT NULL," \
        " nome CHAR(40) NOT NULL, email CHAR(40), curso CHAR(40));")
cursor.fetchall()
conexao.commit()
cursor.close()
conexao.close()

#Passo1: exibindo a tela de registrar aluno
def tela_registro():
    #criando a janela de registro
    janela2 = tk.Toplevel()
    janela2.title('Cadastrar aluno')
    janela2.geometry('800x500+280+115')
    janela2.iconbitmap(default="icones\\icon.ico")
    janela2.rowconfigure([0, 1, 2, 3], weight=1)
    janela2.columnconfigure([0, 1], weight=1)
    janela2.resizable(False, False)
    janela2.transient(janela)  #indica que está vindo da primeira janela
    janela2.focus_force()      #independente do que fizer a janela 2 ficará a frente
    janela2.grab_set()    #enquanto janela 2 aberta não é possivel tomar ação na primeira janela

    # Criação de Labels e carregando imagem
    lab_fundo_reg = Label(janela2, image=img_fundo_reg)
    lab_fundo_reg.pack()

    #criando caixas de entrada
    en_nome = Entry(janela2, bd=2, font=("Calibri", 15), justify=CENTER)
    en_nome.place(width=343, height=34, x=228, y=160)

    en_email = Entry(janela2, bd=2, font=("Calibri", 15), justify=CENTER)
    en_email.place(width=343, height=34, x=228, y=233)

    en_matricula = Entry(janela2, bd=2, font=("Calibri", 15), justify=CENTER)
    en_matricula.place(width=343, height=34, x=228, y=309)

    en_curso = Entry(janela2, bd=2, font=("Calibri", 15), justify=CENTER)
    en_curso.place(width=343, height=34, x=228, y=385)

    #Registrando alunos
    def registrar_aluno():
        #guardando as informações de entrada
        matricula_aluno = (en_matricula.get())
        nome_aluno = en_nome.get()
        email_aluno = en_email.get()
        curso_aluno = en_curso.get()

        # condição para caso vazio
        if matricula_aluno == "":
            msg = "Para Registrar um novo aluno é necessário \n"
            msg += "preencher todos os campos corretamente!"
            messagebox.showinfo("Registrar aluno - Alerta!", msg)
        elif nome_aluno == "":
            msg = "Para Registrar um novo aluno é necessário \n"
            msg += "preencher todos os campos corretamente!"
            messagebox.showinfo("Registrar aluno - Alerta!", msg)
        elif email_aluno == "":
            msg = "Para Registrar um novo aluno é necessário \n"
            msg += "preencher todos os campos corretamente!"
            messagebox.showinfo("Registrar aluno - Alerta!", msg)
        elif curso_aluno == "":
            msg = "Para Registrar um novo aluno é necessário \n"
            msg += "preencher todos os campos corretamente!"
            messagebox.showinfo("Registrar aluno - Alerta!", msg)

        else:
            #conectando ao banco
            conexao = conector.connect('bd_alunos.db')
            cursor = conexao.cursor()
            #inserindo as informações
            cursor.execute("""INSERT INTO cadastro(matricula, nome, email, curso)
                VALUES(?,?,?,?)""", (matricula_aluno, nome_aluno, email_aluno, curso_aluno))
            conexao.commit()
            #desconectando banco
            cursor.close()
            conexao.close()

            #limpando caixas de entrada
            def limpa_campos():
                en_nome.delete(0, END)
                en_email.delete(0, END)
                en_matricula.delete(0, END)
                en_curso.delete(0, END)
            limpa_campos()

            #mensagem de cadastrado com sucesso
            msg = "Aluno cadastrado com sucesso!"
            messagebox.showinfo("Registrar aluno - Alerta!", msg)

    #botão Registrar
    botao_reg2 = Button(janela2, image=img_botao_reg2, command=registrar_aluno)
    botao_reg2.place(width=90, height=40, x=360, y=441)


#Passo2: exibindo a tela de buscar aluno
def tela_busca():
    janela3 = tk.Toplevel()
    janela3.title('Buscar aluno')
    janela3.geometry('800x500+280+115')
    janela3.iconbitmap(default="icones\\icon.ico")
    janela3.rowconfigure([0, 1, 2, 3], weight=1)
    janela3.columnconfigure([0, 1], weight=1)
    janela3.resizable(False, False)
    janela3.transient(janela) #indica que está vindo da primeira janela
    janela3.focus_force()     #independente do que fizer a janela3 ficará a frente
    janela3.grab_set()  # enquanto janela 2 aberta não é possivel tomar ação na primeira janela

    # Criação de Labels e carregando imagem
    lab_fundo_busca = Label(janela3, image=img_fundo_busca)
    lab_fundo_busca.pack()

    # criando caixas de entrada
    en_nome_busca = Entry(janela3, bd=2, font=("Calibri", 15), justify=CENTER)
    en_nome_busca.place(width=343, height=48, x=228, y=157)

    # criando a caixa de exibição
    caixa = ttk.Treeview(janela3,height=8, columns=("matricula", "nome", "email", "curso"))
    caixa.place(width=787, x=6, y=308)
    caixa.heading("#0", text="")
    caixa.heading("#1", text="Matrícula")   #cabeça de cada coluna
    caixa.heading("#2", text="Nome")
    caixa.heading("#3", text="Email")
    caixa.heading("#4", text="Curso")
    caixa.column("#0", width=0)    #largura da coluna
    caixa.column("#1", width=120)  #largura da coluna
    caixa.column("#2", width=260)  #largura da coluna

        #configurando o scroll da caixa
    '''scroll_vertical = Scrollbar(janela3, orient='vertical')
    caixa.configure(yscroll= scroll_vertical.set)
    scroll_vertical.place(height=185,x=775, y=308)'''

    '''scroll_horizontal = Scrollbar(janela3, orient='horizontal')
    caixa.configure(yscroll=scroll_horizontal.set)
    scroll_horizontal.place(width=782, x=2, y=475)'''

    #buscando aluno no banco de dados
    def busca_aluno():
        #conectando ao banco
        conexao = conector.connect('bd_alunos.db')
        cursor = conexao.cursor()

        #buscando aluno
        caixa.delete(*caixa.get_children())   #limpando a caixa de exibição
        sleep(0.2)
        en_nome_busca.insert(END, '%')  #a porcentagem é um caracter coringa que irá pegar a informação completa (tudo que vier depois do que eu digitar)
        #guardando a informação na variável
        nome_get = en_nome_busca.get()
        #executando sql
        cursor.execute(
            """ SELECT matricula, nome, email, curso FROM cadastro
            WHERE nome LIKE '%s' ORDER BY nome ASC""" % nome_get)   #o LIKE indica onde ele pesquisará as informações
        busca_nome_caixa = cursor.fetchall()

        #percorrendo a lista
        for i in busca_nome_caixa:
            caixa.insert("", END, values=i)

        #desconectando banco
        cursor.close()
        conexao.close()

        #limpando a Entry
        en_nome_busca.delete(0, END)

    # criando o botao
    botao_cons2 = Button(janela3, image=img_botao_cons2, command=busca_aluno)
    botao_cons2.place(width=50, height=48, x=576, y=157)


#passo3: exibindo a tela de listar alunos cadastrados
def tela_listar():
    janela4 = tk.Toplevel()
    janela4.title('Todos os alunos')
    janela4.geometry('800x500+280+115')
    janela4.iconbitmap(default="icones\\icon.ico")
    janela4.rowconfigure([0, 1, 2, 3], weight=1)
    janela4.columnconfigure([0, 1], weight=1)
    janela4.resizable(False, False)
    janela4.transient(janela)   #indica que está vindo da primeira janela
    janela4.focus_force()   #independente do que fizer a janel4 ficará a frente
    janela4.grab_set()  # enquanto janela 2 aberta não é possivel tomar ação na primeira janela

    # Criação de Labels e carregando imagem
    lab_fundo_reg = Label(janela4, image=img_fundo_lista)
    lab_fundo_reg.pack()

    # criando a caixa de exibição
    caixa2 = ttk.Treeview(janela4, height=19, columns=("matricula", "nome", "email", "curso"))
    caixa2.place(width=770, x=6, y=90)
    caixa2.heading("#0", text="")
    caixa2.heading("#1", text="Matrícula")
    caixa2.heading("#2", text="Nome")
    caixa2.heading("#3", text="Email")
    caixa2.heading("#4", text="Curso")
    caixa2.column("#0", width=0)
    caixa2.column("#1", width=105)
    caixa2.column("#2", width=230)
    caixa2.column("#4", width=230)

    # configurando o scroll da caixa
    scroll_vertical = Scrollbar(janela4, orient='vertical')
    caixa2.configure(yscroll=scroll_vertical.set)
    scroll_vertical.place(height=404, x=776, y=91)

    """scroll_horizontal = Scrollbar(janela4, orient='horizontal')
    caixa2.configure(yscroll=scroll_horizontal.set)
    scroll_horizontal.place(width=769, x=6, y=476)"""

    def exibir_lista():
        #conectando ao banco
        conexao = conector.connect('bd_alunos.db')
        cursor = conexao.cursor()
        lista = cursor.execute("""SELECT matricula, nome, email, curso FROM cadastro
            ORDER BY nome ASC; """)  #através da coluna nome ele ira exibir em ordem alfabética #ASC é para exibir em ordem ascendente

        #percorrendo a lista e inserindo
        for i in lista:
            caixa2.insert("", END, values=i)

        #desconectando banco de dados
        cursor.close()
        conexao.close()

    exibir_lista()


#criando os botoes do Menu
botao_reg = Button(janela, image=img_botao_reg, command=tela_registro)
botao_reg.place(width=208, height=47, x=298, y=216)

botao_cons = Button(janela, image=img_botao_cons, command=tela_busca)
botao_cons.place(width=208, height=47, x=298, y=310)

botao_listar = Button(janela, image=img_botao_listar, command=tela_listar)
botao_listar.place(width=208, height=47, x=298, y=403)

#mantendo a janela principal em loop e executando funções
janela.mainloop()
