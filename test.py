import unittest
from calc import Calculadora_cientifica

class Teste(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculadora_cientifica()
    
    def teste_soma(self):
        self.assertEqual(self.calc.soma(20,13), 33)
        self.assertEqual(self.calc.soma(100,400), 500)

    def teste_subtracao(self):
        self.assertEqual(self.calc.subtracao(10,5), 5)
        self.assertEqual(self.calc.subtracao(20,10), 10)

    def teste_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(10,5), 50)
        self.assertEqual(self.calc.multiplicacao(5,5), 25)

    def teste_divisao(self):
        self.assertEqual(self.calc.divisao(10,2), 5)
        self.assertEqual(self.calc.divisao(20,5), 4)

if __name__ == '__main__' :
    unittest.main()