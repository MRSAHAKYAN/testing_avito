from card import Card

class PaymentMachine:
    
    def __init__(self):
        self.card = None
        
    def apply_card(self, card=None):
        self.card = card
        
    def clear_card(self):
        self.card = None
        
    @staticmethod
    def get_discount(card):
        discount = 0
        if card is not None:
            card_points = card.get_points()
            if card_points >= 0 and card_points < 100:
                discount = 1
            elif card_points >= 100 and card_points < 200:
                discount = 3
            elif card_points >= 200 and card_points < 500:
                discount = 5
            else:
                discount = 10
        return discount
                
                
    def buy(self, amount):
        discount = PaymentMachine.get_discount(self.card)
        final_amount = amount * ((100 - discount) / 100)
        self.clear_card()
        return final_amount
        