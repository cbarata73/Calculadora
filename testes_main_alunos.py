import unittest
import math
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4

class TestCalculadora(unittest.TestCase):

    def teste_operacoes_basicas(self):
    # Teste operações básicas + - * / % ^
        self.assertEqual(calculadora(2, 3, '+'), 5)

    def teste_operacoes_diversas(self):
        # Teste divisão por zero / %
        self.assertTrue(math.isnan(calculadora(5, 0, '/')))

        # Teste operador inválido - fazer três testes
        self.assertTrue(math.isnan(calculadora(2, 3, '$')))

        # Teste números de virgula flutuante - fazer três testes
        self.assertAlmostEqual(calculadora(2.5, 1.5, '+'), 4.0)

        # Teste números negativos - fazer 3 testes
        self.assertEqual(calculadora(-2, 3, '*'), -6)

    def teste_v2_operacoes(self):
        # Teste operações básicas + - * / % ^
        self.assertEqual(calculadora_v2(2, 3, '+'), 5)

    def teste_v3_operacoes(self):
        # Teste operações básicas + - * / % ^
        self.assertEqual(calculadora_v3(2, 3, '+'), 5)

    def teste_v4_operacoes(self):
        # Teste operações básicas + - * / % ^
        self.assertEqual(calculadora_v4(2, 3, '+'), 5)


if __name__ == '__main__':
    unittest.main()

# para correr os testes: python -m unittest -v testes_main_alunos.py
