from abc import ABC, abstractmethod
from unittest import TestCase, main

class Calculadora:
    def calcular(self,valor1,valor2,operador):
        validaOperador = OperacaoFabrica()
        operacao = validaOperador.criar(operador)
        if (operador == None):
            return 0
        else: 
            resultado = operacao.executar(valor1,valor2)
            return resultado

class OperacaoFabrica:
    def criar(self,operador):
        if (operador == "soma"):
            return Soma()
        elif (operador == "subtracao"):
            return Subtracao()
        elif (operador == "divisao"):
            return Divisao()
        elif (operador == "multiplicacao"):
            return Multiplicacao()       
            
class Operacao(ABC):
    @abstractmethod
    def executar(self,valor1,valor2):
        pass

class Soma(Operacao):
    def executar(self,valor1,valor2):
        resultado = valor1 + valor2
        return resultado

class Subtracao(Operacao):
    def executar(self,valor1,valor2):
        resultado = valor1 - valor2
        return resultado

class Divisao(Operacao):
    def executar(self,valor1,valor2):
        resultado = valor1 / valor2
        return resultado

class Multiplicacao(Operacao):
    def executar(self,valor1,valor2):
        resultado = valor1 * valor2
        return resultado

class Testes(TestCase):
    def test_soma(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(3,3,"soma"),6)

    def test_soma2(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(80,100,"soma"),180)

    def test_subtracao(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(10,5,"subtracao"),5)
    
    def test_subtracao2(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(7,200,"subtracao"),-193)

    def test_divisao(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(30,5,"divisao"),6)
    
    def test_divisao2(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(5,2,"divisao"),2.5)

    def test_multiplicacao(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(9,9,"multiplicacao"),81)

    def test_multiplicacao2(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(-50,2,"multiplicacao"),-100)

    def test_valor_invalido(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(8,10,None),0)
    
if __name__ == "__main__":
    main()
