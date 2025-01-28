import unittest
import math
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4

class TestCalculadora(unittest.TestCase):

    def teste_operacoes_basicas(self):
    # Teste operações básicas + - * / % ^
        self.assertEqual(calculadora(2, 3, '+'), 5)
        self.assertEqual(calculadora(7, 4, '-'), 3)
        self.assertEqual(calculadora(2, 4, '*'), 8)
        self.assertEqual(calculadora(6, 12, '/'), 0.5)
        self.assertEqual(calculadora(5, 4, '%'), 1)
        self.assertEqual(calculadora(5, 2, '^'), 25)

    def teste_operacoes_diversas(self):
        # Teste divisão por zero / %
        self.assertTrue(math.isnan(calculadora(5, 0, '/')))
        self.assertTrue(math.isnan(calculadora(3, 0, '%')))

        # Teste operador inválido - fazer três testes
        self.assertTrue(math.isnan(calculadora(2, 3, '$')))
        self.assertTrue(math.isnan(calculadora(2, 5, '#')))
        self.assertTrue(math.isnan(calculadora(0, 2, 'qwe')))

        # Teste números de virgula flutuante - fazer três testes
        self.assertAlmostEqual(calculadora(2.5, 1.5, '+'), 4.0)
        self.assertAlmostEqual(calculadora(4.5, 1.5, '-'), 3.0)
        self.assertAlmostEqual(calculadora(5.5, 1.5, '*'), 8.25)

        # Teste números negativos - fazer 3 testes
        self.assertEqual(calculadora(-2, 3, '*'), -6)
        self.assertEqual(calculadora(-3, -2, '-'), -1)
        self.assertEqual(calculadora(-3, -3, '*'), 9)

    def teste_v2_operacoes(self):
        # Teste operações básicas + - * / % ^
        self.assertEqual(calculadora_v2(2, 7, '+'), 9)
        self.assertEqual(calculadora_v2(1, 3, '-'), -2)
        self.assertEqual(calculadora_v2(2, 7, '*'), 14)
        self.assertEqual(calculadora_v2(3, 3, '/'), 1)
        self.assertEqual(calculadora_v2(2, 3, '%'), 2)
        self.assertEqual(calculadora_v2(2, 4, '^'), 16)

    def teste_v3_operacoes(self):
        # Teste operações básicas + - * / % ^
        self.assertEqual(calculadora_v3(2, 3, '+'), 5)
        self.assertEqual(calculadora_v3(2, 5, '-'), -3)
        self.assertEqual(calculadora_v3(2, 6, '*'), 12)
        self.assertEqual(calculadora_v3(3, 3, '/'), 1)
        self.assertEqual(calculadora_v3(2, 3, '%'), 2)
        self.assertEqual(calculadora_v3(2, 3, '^'), 8)

    def teste_v4_operacoes(self):
        # Teste operações básicas + - * / % ^
        self.assertEqual(calculadora_v4(2, 3, '+'), 5)
        self.assertEqual(calculadora_v4(2, 1, '-'), 1)
        self.assertEqual(calculadora_v4(2, 4, '*'), 8)
        self.assertEqual(calculadora_v4(6, 12, '/'), 0.5)
        self.assertEqual(calculadora_v4(6, 4, '%'), 2)
        self.assertEqual(calculadora_v4(2, 2, '^'), 4)


if __name__ == '__main__':
    unittest.main()

# para correr os testes: python -m unittest -v testes_main_alunos.py
