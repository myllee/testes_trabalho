import unittest
class Calculadora_cientifica:

    def __init__(self):
        self.ultimo_resultado = None

    def soma(self,a,b):
        self.ultimo_resultado = a + b 
        return self.ultimo_resultado

    def subtracao(self,a,b) :
        self.ultimo_resultado = a - b
        return self.ultimo_resultado

    def multiplicacao(self,a,b) :
        self.ultimo_resultado = a * b
        return self.ultimo_resultado

    def divisao(self,a,b) :
        if a == 0 :
         raise ValueError("Divisão por zero não é permitida.")
        else :
         self.ultimo_resultado = a / b
        return self.ultimo_resultado




    
    