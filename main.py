from tkinter import *
from os import listdir

"""
ficheiros txt
formato
nome do ficheiro : <nome do aluno.txt>
dentro do ficheiro:
<curso>
Cadeira1 Nota1 Ects1
.....
Cadeirax Notax Ectsx

"""


class ficheiros:


    def lerCurso(nomeAluno):
        url_ficheiro = "data/alunos/"+nomeAluno
        file = open(url_ficheiro,"r", encoding='utf-8')
        curso = file.readline()
        file.close()
        return curso

    def lerAlunos():
        url_ficheiro="data/alunos/"
        alunos = listdir(url_ficheiro)
        return alunos

    def calcularMedia(nomeAluno):
        url_ficheiro = "data/alunos/"+nomeAluno
        ects = 0
        soma = 0
        media = 0
        file = open(url_ficheiro,"r", encoding='utf-8')
        conteudo = file.readlines()
        conteudo = conteudo[1:]

        #print(conteudo)
        if (len(conteudo) > 0):
            for x in range(0, len(conteudo)):
                ects += int(conteudo[x][-2])
                soma += int(conteudo[x][-5:-3]) * int(conteudo[x][-2])

            media = soma/ects
            media = round(media,2)
        file.close()
        return media


    def adicionarnovoAluno(nomeAluno,curso):
        url_ficheiro = "data/alunos/"+nomeAluno+".txt"

        file = open(url_ficheiro, "w", encoding='utf-8')
        file.write(f"{curso}\n")
        file.close()

    def escreverFicheiro(nomeAluno, Cadeira, Nota, ECTS):
        url_ficheiro = "data/alunos/"+nomeAluno+".txt"
        file = open(url_ficheiro, "a", encoding='utf-8')
        conteudo = f"{Cadeira} {Nota} {ECTS}\n"
        file.write(conteudo)
        file.close()

        #print("Ficheiro Escrito!")

class Aluno:

    def adicionarAluno(nomeAluno):
        url_ficheiro = "data/alunos/"+nomeAluno+".txt"
        file = open(url_ficheiro, "w", encoding='utf-8')
        file.close()
        #print("Aluno adicionado!")

#    def editarAluno():


    def verAluno(nomeAluno):
        url_ficheiro = "data/alunos/"+nomeAluno+".txt"

        file = open(url_ficheiro, "r", encoding='utf-8')

        cadeiras = file.readline()




class Notas:

    def adicionarcadeiraFunction(aluno_om, cadeira_e, nota_e, ects_e):

        nomealuno = aluno_om.get()
        cadeira = cadeira_e.get()
        nota = nota_e.get()
        ects = ects_e.get()

        ficheiros.escreverFicheiro(nomealuno,cadeira,nota,ects)

    def editarAluno(frame):
        editarAlunoFRAME = Frame(frame,width=1280, height=720, bg="gray")
        editarAlunoFRAME.place(x=0,y=0)


#       opção do aluno
        alunos = ficheiros.lerAlunos()
        alunosn = [x[:-4] for x in alunos]
        nomeAlunoOpt = StringVar()
        nomeAlunoOpt.set(alunosn[0])

        nomealunoLabelEditar = Label(editarAlunoFRAME,text="Aluno", font="Arial 15")
        nomealunoLabelEditar.place(x=200,y=100)

        selectAlunoOption = OptionMenu(editarAlunoFRAME, nomeAlunoOpt, *alunosn)
        selectAlunoOption.place(x=200, y=200)

#       cadeiras

        nomecadeiraLabelEditar = Label(editarAlunoFRAME,text="Cadeira", font="Arial 15")
        nomecadeiraLabelEditar.place(x=450,y=100)

        editarCadeiraEntry = Entry(editarAlunoFRAME,width=20)
        editarCadeiraEntry.place(x=450,y=200)

#       Notas
        notaLabelEditar = Label(editarAlunoFRAME,text="Nota", font="Arial 15")
        notaLabelEditar.place(x=650,y=100)

        editarnotaEntry = Entry(editarAlunoFRAME,width=10)
        editarnotaEntry.place(x=650,y=200)

#       ECTS
        ectsLabelEditar = Label(editarAlunoFRAME,text="ECTS", font="Arial 15")
        ectsLabelEditar.place(x=800,y=100)

        editarectsEntry = Entry(editarAlunoFRAME,width=10)
        editarectsEntry.place(x=800,y=200)

        adicionarcadeiraBTN = Button(editarAlunoFRAME, text="Adicionar Cadeira", font="Arial 15", command=lambda: Notas.adicionarcadeiraFunction(nomeAlunoOpt,editarCadeiraEntry, editarnotaEntry, editarectsEntry))
        adicionarcadeiraBTN.place(x=500,y=400)

        VoltarAtrasBTN = Button(editarAlunoFRAME,text="Voltar", font="Arial 15",command=lambda:editarAlunoFRAME.destroy())
        VoltarAtrasBTN.place(x=1000, y=400)

    def adicionarAlunofunctio(EntryNome, EntryCurso, frame):
        name = EntryNome.get()
        curso = EntryCurso.get()

        ficheiros.adicionarnovoAluno(name,curso)

        frame.destroy()


    def adicinarALUNO(frame):
        AddAlunoFRAME = Frame(frame, width=1280, height=720, bg="gray")
        AddAlunoFRAME.place(x=0,y=0)

        AddAlunoTituloLabel = Label(AddAlunoFRAME, text="Adicionar Novo Aluno", font="Arial 20 bold")
        AddAlunoTituloLabel.place(x=525,y=100)

        AddNomeAlunoLabel = Label(AddAlunoFRAME,text="Nome do Aluno",font="Arial 15")
        AddNomeAlunoLabel.place(x=600,y=200)

        nomeAlunoEntry = Entry(AddAlunoFRAME,width=40)
        nomeAlunoEntry.place(x=550,y=250)

        AddCursoLabel = Label(AddAlunoFRAME,text="Curso do Aluno",font="Arial 15")
        AddCursoLabel.place(x=600,y=300)

        cursoAlunoEntry = Entry(AddAlunoFRAME,width=40)
        cursoAlunoEntry.place(x=550,y=350)

        adicionarAlunoEntryBTN = Button(AddAlunoFRAME, text="Adicionar Aluno", font="Arial 15", command=lambda: Notas.adicionarAlunofunctio(nomeAlunoEntry, cursoAlunoEntry, AddAlunoFRAME))
        adicionarAlunoEntryBTN.place(x=600,y=400)

        VoltarAtrasBTN = Button(AddAlunoFRAME,text="Voltar", font="Arial 15",command=lambda:AddAlunoFRAME.destroy())
        VoltarAtrasBTN.place(x=1000, y=400)


    def verNotas(window):
        verNotasFRAME = Frame(window,bg="gray",width=1280,height=720)
        verNotasFRAME.place(x=0,y=0)


        tituloVerNOTAS = Label(verNotasFRAME,text= "Notas",width=5,height=1,font="Arial 30 bold", bg="gray").place(x=500,y=50)

        labelNomeAlunos = Label(verNotasFRAME,text="Aluno",font="Arial 15", bg="gray").place(x=150, y=200)

        labelCursoAlunos = Label(verNotasFRAME,text="Curso",font="Arial 15", bg="gray").place(x=400, y=200)

        labelMediaAlunos = Label(verNotasFRAME,text="Média",font="Arial 15", bg="gray").place(x=600, y=200)



        listaAlunos = Listbox(verNotasFRAME,width=30)
        listaAlunos.place(x=150,y=250)
        listaCursos = Listbox(verNotasFRAME,width=30)
        listaCursos.place(x=400,y=250)
        listaMedias = Listbox(verNotasFRAME,width=30)
        listaMedias.place(x=600,y=250)
        alunos = ficheiros.lerAlunos()

        for x in alunos:
            curso = ficheiros.lerCurso(x)
            media = ficheiros.calcularMedia(x)
            listaAlunos.insert(END, x[:-4])
            listaCursos.insert(END, curso)
            listaMedias.insert(END, media)


        adicionarAlunoBTN = Button(verNotasFRAME,text="Adicionar Aluno", font="Arial 15", command=lambda:Notas.adicinarALUNO(verNotasFRAME))
        adicionarAlunoBTN.place(x=1000, y=200)

        editarAlunoBTN = Button(verNotasFRAME,text="Editar Aluno", font="Arial 15", command=lambda: Notas.editarAluno(verNotasFRAME))
        editarAlunoBTN.place(x=1000, y=300)

        VoltarAtrasBTN = Button(verNotasFRAME,text="Voltar", font="Arial 15",command=lambda:verNotasFRAME.destroy())
        VoltarAtrasBTN.place(x=1000, y=400)

class Janela:

    def paginaInicial(window):


        tituloLabel = Label(window,
                            text = "Gestor de Curso",
                            width=20,
                            height=1,
                            bg="gray",
                            font="Arial 20 bold").pack(pady=50)

        verNotasBTN = Button(window,
                            text = "Consultar Notas",
                            width=16,
                            height=1,
                            font="Arial 20",
                            command=lambda: Notas.verNotas(window)
                            ).pack(pady=150)



window = Tk()
window.title("Gestor de Curso")
window.geometry("1280x720+100+60")
window.resizable(False, False)
window.iconbitmap("data/img/icon.ico")
window["bg"] = "gray"
Janela.paginaInicial(window)

window.mainloop()
