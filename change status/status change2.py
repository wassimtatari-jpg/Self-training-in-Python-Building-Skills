class Order:
    def __init__(self,quantity,price):
        self.quantity=quantity
        self.price=price
        self.status=None
    def process_order(self):
        if self.quantity>20:
            self.status="too many"
            return self.status
        elif self.quantity>0 and self.price>0:
            self.status="order processed"
            return self.status
        else:
            self.status= "order failed"
            return self.status
    def check_status(self):
        if self.status is None:
            return"order pending"
        elif self.status=='order processed':
            return"order processed"
        elif self.status=='too many':
            return"too many"
        else:
            return"order failed"
my_order=Order(0,34)
print(my_order.check_status())
print(my_order.process_order())
