class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def checkbalance(self):
        print("Your balance is $5000")

    def cashWithdrawel(self):
        print('You withdrew $100')

    def BalanceEnquiry(self):
        print('Your questions can range from cash withdrawel to check your balance')

new_user = Atm(cardnumber, pin)