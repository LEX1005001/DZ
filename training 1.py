class Cup:
    def __init__(self,material) :
        self.material=material
        self.amount_liquid=0
    def increase(self,amount:int)->int:
        self.amount_liquid+=amount
    def decrease(self,damount:int):
        self.amount_liquid-=damount
        if self.amount_liquid<0:
            self.amount_liquid=0
    def inf(self):
        print(f"Кружка из {self.material}\nкол-во вещества в кружке<{self.amount_liquid}мл>")
p=Cup("Стекляная")
p.increase(4)
p.decrease(2)
p.inf()