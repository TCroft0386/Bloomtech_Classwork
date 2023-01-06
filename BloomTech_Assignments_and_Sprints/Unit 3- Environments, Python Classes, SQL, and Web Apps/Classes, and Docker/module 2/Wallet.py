class Wallet:
    '''doc'''
    # Class Constructor
    # Initializes the Function
    # whenever we make a new wallet
    # an initial_amount *MUST* be provided
    def __init__(self, initial_amount=0):
        '''doc'''
        self.balance = initial_amount

    # this is not a method
    def spend_cash(self, amount):
        '''doc'''
        if self.balance < amount:
            return "you can't afford it!"
        else:
            self.balance -= amount
            return f'''You can afford it, it cost ${amount}. Current balance is now ${self.balance}'''

    def add_cash(self, amount):
        '''doc'''
        self.balance += amount
        return f"Added ${amount} to the wallet."

    def __repr__(self):
        '''doc'''
        return f"<Wallet with balance of ${self.balance}>"


if __name__ == '__main__':
    wallet1 = Wallet()
    print(wallet1)
    print(wallet1.balance)
    print(wallet1.spend_cash(30))
    print(wallet1.add_cash(120))
    print(wallet1.spend_cash(500))
    print(wallet1.balance)









