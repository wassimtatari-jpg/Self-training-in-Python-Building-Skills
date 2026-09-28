class Product:
    def __init__(self,stock,price,request):
        self.stock=stock
        self.price=price
        self.request=request
        self.status=None
    def process_sale(self):
        if self.request<=0:
            self.status="invalid quantity"
            return self.status
        elif self.stock==0:
            self.status="out of stock"
            return self.status
        elif self.request>self.stock:
            self.status="not enough stock"
            return self.status
        elif self.price>0 and self.request>0 and self.stock>0 and self.request<=self.stock:
            self.status="sale complete"
            self.stock=self.stock-self.request
            return self.status,self.stock
        else:
            self.status="sale failed"
            return self.status
    def check_sale(self):
        if self.status is None:
            return "sale pending"
        elif self.status=="sale complete":
            return"sale complete"
        elif self.status=="invalid quantity":
            return"invalid quantity"
        elif self.status=="out of stock":
            return "out of stock"
        else:
            return "not enough stock"
sale=Product(10,200,5)
print(sale.check_sale())
print(sale.process_sale())        
        