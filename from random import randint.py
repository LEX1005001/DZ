from random import randint
class School:
    def __init__(self,name,students):
        self.name=name
        self.students=students
        self.journal=[]
        for i in range(self.students):
            row=[]
            self.journal.append(row)
    def add_mark(self,num_stud):
        self.journal[num_stud-1].append(randint(0,5))
    def sred_mark(self,num_stud):
        a=sum(self.journal[num_stud-1])/len(self.journal[num_stud-1])
        print(f"Средняя успеваемость ученика <{num_stud}> -> {a}")
    def info(self):
        print(f"Название школы <{self.name}>\nКол-во учащихся<{self.students}>\nЖурнал успеваемости->{self.journal} ")
sc=School("39",4)
sc.add_mark(2)
sc.add_mark(2)
sc.add_mark(2)
sc.sred_mark(2)
sc.info()
        
