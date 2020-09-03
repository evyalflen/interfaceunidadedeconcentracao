from tkinter import *
from decimal import Decimal
  
class Application:
    def __init__(self, master=None):

        #Elementos - GUI
        self.fontePadrao = ("Arial", "12")

        self.zeroContainer = Frame(master)
        self.zeroContainer["pady"] = 20
        self.zeroContainer.pack()
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.espaco0Container = Frame(master)
        self.espaco0Container["pady"] = 20
        self.espaco0Container.pack()
        
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 40
        self.segundoContainer.pack()

        self.espaco1Container = Frame(master)
        self.espaco1Container["pady"] = 20
        self.espaco1Container.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 40
        self.terceiroContainer.pack()

        self.espaco2Container = Frame(master)
        self.espaco2Container["pady"] = 20
        self.espaco2Container.pack()
        
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 40
        self.quartoContainer.pack()

        self.espaco3Container = Frame(master)
        self.espaco3Container["pady"] = 20
        self.espaco3Container.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.espaco4Container = Frame(master)
        self.espaco4Container["pady"] = 20
        self.espaco4Container.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 30
        self.sextoContainer.pack()

        self.setimoContainer = Frame(master)
        self.setimoContainer["pady"] = 30
        self.setimoContainer.pack()

        self.oitavoContainer = Frame(master)
        self.oitavoContainer["pady"] = 30
        self.oitavoContainer.pack()

        #Organização - GUI
        self.titulo = Label(self.zeroContainer, text = "Cálculos de Unidades de Concentração de Soluções")
        self.titulo["font"] = ("Arial", "14", "bold")
        self.titulo.pack()
  
        self.titulo2 = Label(self.primeiroContainer, text = "Concentração Comum")
        self.titulo2["font"] = ("Arial", "14")
        self.titulo2.pack()
  
        self.massaLabel = Label(self.segundoContainer,text="Massa(g)", font = self.fontePadrao)
        self.massaLabel.pack(side = LEFT)
  
        self.massa = Entry(self.segundoContainer)
        self.massa["width"] = 30
        self.massa["font"] = self.fontePadrao
        self.massa.pack(side = LEFT)
  
        self.volumeLabel = Label(self.terceiroContainer, text = "Volume(L)", font = self.fontePadrao)
        self.volumeLabel.pack(side = LEFT)
  
        self.volume = Entry(self.terceiroContainer)
        self.volume["width"] = 30
        self.volume["font"] = self.fontePadrao
        self.volume.pack(side = LEFT)

        self.comumLabel = Label(self.quartoContainer, text = "Comum(g/L)", font = self.fontePadrao)
        self.comumLabel.pack(side = LEFT)
  
        self.comum = Entry(self.quartoContainer)
        self.comum["width"] = 30
        self.comum["font"] = self.fontePadrao
        self.comum["text"] = "Digite 'x' para a incógnita"
        self.comum.pack(side = LEFT)
        
  
        self.calcular = Button(self.quintoContainer)
        self.calcular["text"] = "Calcular"
        self.calcular["font"] = ("Arial", "10")
        self.calcular["width"] = 20
        self.calcular["command"] = self.calcula_comum
        self.calcular.pack()
  
        self.mensagem = Label(self.sextoContainer, text = "Resultado", font = self.fontePadrao)
        self.mensagem.pack()

        self.mensagem2 = Label(self.setimoContainer, text = "", font = self.fontePadrao)
        self.mensagem2.pack()

    #Método calcular
    def calcula_comum(self):
        massa = self.massa.get()
        volume = self.volume.get()
        comum = self.comum.get()
        resultado = 0
        if massa == "":
            resultado = Decimal(comum) * Decimal(volume)
            self.mensagem2["text"] = "Massa = " + str(volume) + " L x " + str(comum) + " g/L = " + str(resultado)
        elif volume == "":
            resultado = Decimal(massa) / Decimal(comum)
            self.mensagem2["text"] = "Volume = "+ str(massa) + " g ÷ " + str(comum) + " g/L = "+ str(resultado)
        elif comum == "":
            resultado = Decimal(massa) / Decimal(volume)
            self.mensagem2["text"] = "Concentração Comum = " + str(massa) + " g ÷ "+ str(volume)+ " L = "+ str(resultado)

root = Tk()
Application(root)
root.mainloop()
