import random

class WUQI :
    def __init__(self,name,agg):
        self.name=name
        self.agg=agg

    def shiyong(self,person):
        person.agg+=self.agg
class PERSON:
    def __init__(self,name,life,su_du,agg):
        self.name=name
        self.life=life
        self.su_du=su_du
        self.agg=agg
    def attack(self,dog):
        print(P1.name,"对",D1.name,"造成了",P1.agg,"点伤害")
        dog.life-=self.agg


class DOG:
    def __init__(self,name,life,su_du,agg):
        self.name=name
        self.life=life
        self.su_du=su_du
        self.agg=agg
    def bite (self,person):
        print(D1.name,"咬了",P1.name,"造成了",D1.agg,"点伤害")
        person.life-=self.agg
life_n1=random.randint(100,200)#N级人类血量
life_n2=random.randint(20,150)#N级兽类血量
agg_n1=random.randint(5,50)#N级人类李量
agg_n2=random.randint(2,100)#N级兽类李量
agg_n3=random.randint(10,15)#N级兽类李量
sudu_n1=random.randint(5,10)#N级人类速度
sudu_n2=random.randint(2,15)#N级人类速度

P1=PERSON('A',life_n1,sudu_n1,agg_n1)

D1=DOG('wo;f',life_n2,sudu_n2,agg_n2)

W1=WUQI('fangtianhuaji',agg_n1)
W2=WUQI('牛比剑',agg_n3)
