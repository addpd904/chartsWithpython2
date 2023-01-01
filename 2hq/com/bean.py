class itemOb:
    def __init__(self,data:str,order:str,money:int,province:str):
        self.data=data
        self.order=order
        self.money=money
        self.province=province
    def __str__(self):
        return f'{self.data},{self.order},{self.money},{self.province}'