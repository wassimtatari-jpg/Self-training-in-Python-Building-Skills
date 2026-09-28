class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        self.status=None
    def withdraw(self,amount):
        self.amount=amount
        if self.amount<=0:
            self.status="invalid amount"
            return self.status
        elif self.amount>self.balance:
            self.status="insufficient balance"
            return self.status
        else:
            self.balance=self.balance-self.amount
            self.status="withdrawal complete"
            return self.status,self.balance
    def deposit(self,amount):
        self.amount=amount
        if self.amount<=0:
            self.status="invalid deposit"
            return self.status
        else:
            self.balance=self.amount+self.balance
            self.status="deposit complete"
            return self.status,self.balance
    def check_status(self):
        if self.status is None:
            return"Account pending"
        elif self.status=="invalid amount":
            return"invalid amount"
        elif self.status=="insufficient balance":
            return"insufficient balance"
        elif self.status=="withdrawal complete":
            return"withdrawal complete"
        elif self.status=='invalid deposit':
            return 'invalid deposit'
        else:
            return"deposit complete"
        
        