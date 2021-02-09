# Автомат принимает накопительные скидочные карты и при своем расчете учитывает количество баллов,
# по которому начисляет процент скидки: От 0 до 100 баллов - скидка 1% От 100 до 200 баллов - скидка 3 % От 200 
# до 500 баллов - скидка 5% От 500 баллов - скидка 10%

# Задание: Составить такой набор тестовых данных для автомата, при котором мы гарантированно будем знать, 
# что в соответствии со своими накопленными баллами покупатель получит верную скидку.

# Результат: Выложить отдельным файлом с названием TaskTestData.md

import unittest
from payment_machine import PaymentMachine
from card import Card


class TestPaymentMachine(unittest.TestCase):
    def setUp(self):
        self.machine = PaymentMachine()
        
    def test_get_discount(self):
        cases = [
            {
                'card': Card(points=0),
                'expected_discount': 1,
            },
            {
                'card': Card(points=1),
                'expected_discount': 1,
            },
            {
                'card': Card(points=52),
                'expected_discount': 1,
            },
            {
                'card': Card(points=99),
                'expected_discount': 1,
            },
            {
                'card': Card(points=100),
                'expected_discount': 3,
            },
            {
                'card': Card(points=101),
                'expected_discount': 3,
            },
            {
                'card': Card(points=162),
                'expected_discount': 3,
            },
            {
                'card': Card(points=199),
                'expected_discount': 3,
            },
            {
                'card': Card(points=200),
                'expected_discount': 5,
            },
            {
                'card': Card(points=201),
                'expected_discount': 5,
            },
            {
                'card': Card(points=350),
                'expected_discount': 5,
            },
            {
                'card': Card(points=500),
                'expected_discount': 10,
            },
            {
                'card': Card(points=650),
                'expected_discount': 10,
            },
            {
                'card': Card(points=1000000),
                'expected_discount': 10,
            },
            {
                'card': None,
                'expected_discount': 0,
            },
        ]
        
        for case in cases:
            card = case['card']
            expected_discount = case['expected_discount']
            self.assertEqual(expected_discount, PaymentMachine.get_discount(card))

    def test_buy(self):
        cases = [
            {
                'card': Card(points=180),
                'amount': 500,
                'expected_amount': 485,
            },
            {
                'card': Card(points=70),
                'amount': 900,
                'expected_amount': 891,
            },
            {
                'card': Card(points=350),
                'amount': 750,
                'expected_amount': 712.5,
            },
            {
                'card': Card(points=600),
                'amount': 1500,
                'expected_amount': 1350,
            },
            {
                'card': Card(points=0),
                'amount': 20000,
                'expected_amount': 19800,
            },
             {
                'card': Card(points=100),
                'amount': 200,
                'expected_amount': 194,
            },
            {
                'card': Card(points=200),
                'amount': 400,
                'expected_amount': 380,
            },
            {
                'card': Card(points=500),
                'amount': 800,
                'expected_amount': 720,
            },
        ]
            
        for case in cases:
            card = case['card']
            self.machine.apply_card(card)
            amount = case['amount']
            expected_amount = case['expected_amount']
            self.assertEqual(expected_amount, self.machine.buy(amount))
            
    def test_by_without_card(self):
        cases = [
            {
                'amount': 20000,
                'expected_amount': 20000,
            },
            {
                'amount': 0,
                'expected_amount': 0,
            },
            {
                'amount': 150,
                'expected_amount': 150,
            },
        ]
        
        for case in cases:
            amount = case['amount']
            expected_amount = case['expected_amount']
            self.assertEqual(expected_amount, self.machine.buy(amount))
            
            
if __name__ == '__main__':
    unittest.main()