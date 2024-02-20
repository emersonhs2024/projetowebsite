from tkinter import *
root =Tk()
class App():
    def __init__(self):
        self.root = root
        self.config()
        self.calculadora()
        root.mainloop()
    def config(self):
        self.root.title("Calculadora muito simples")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
    def calculadora(self):
        self.lbl1 = Label(text='Primeiro número: ')
        self.lbl1.place(relx=0.15,rely=0.1)
        self.numero1 = DoubleVar()
        self.lbl1_enty = Entry(textvariable=self.numero1)
        self.lbl1_enty.place(relx=0.45,rely=0.1)
        self.lbl2 = Label(text='Segundo número: ')
        self.lbl2.place(relx=0.15, rely=0.25)
        self.numero2 = DoubleVar()
        self.lbl2_enty = Entry(textvariable=self.numero2)
        self.lbl2_enty.place(relx=0.45, rely=0.25)
      # Resultado
        self.lbl3 = Label(text='Resultado')
        self.lbl3.place(relx=0.3, rely=0.7)
        self.resultado = StringVar()
        self.l_resultado = Label(textvariable=self.resultado, font=("Helvetica", '8'))
        self.l_resultado.place(relx=0.5, rely=0.7)

       #Botão
        self.btn1 = Button(text='Soma',command=self.soma)
        self.btn1.place(relx=0.15, rely=0.45)
        self.btn2 = Button(text='Subtração',command=self.sub)
        self.btn2.place(relx=0.3, rely=0.45)
        self.btn3 = Button(text='Divisão',command=self.div)
        self.btn3.place(relx=0.5, rely=0.45)
        self.btn4 = Button(text='Multiplicação',command=self.mult)
        self.btn4.place(relx=0.65, rely=0.45)

    def soma(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        resul = num1 + num2
        self.resultado.set(resul)
    def sub(self):
      num1 = self.numero1.get()
      num2 = self.numero2.get()
      resul = num1 - num2
      self.resultado.set(resul)
    def mult(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        resul = num1 * num2
        self.resultado.set(resul)
    def div(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        resul = round((num1 / num2),2)
        self.resultado.set(resul)
App()