import random
import time

from bao.shujuk import P1,D1,W1,W2



s=random.randint(0,10)
def zhuangbei(select,P):
    if (select==0):
        print('装备了', W1.name, '伤害翻倍')
        W1.shiyong(P),
    elif(select==1):
        print('装备了', W2.name, '附加额外伤害')
        W2.shiyong(P)
    else:print('装备失败')
print('开始战斗')
print(P1.name,P1.life,P1.agg,P1.su_du)

print(D1.name,D1.life,D1.agg,D1.su_du)
time.sleep(3)
zhuangbei(s,P1)
time.sleep(1)
while P1.life and D1.life >0:
    if(P1.su_du>D1.su_du):
        P1.attack(D1)
        print(D1.name,'还剩',D1.life,'点血')
        time.sleep(2)
        if P1.life>0 and D1.life > 0:
            pass
        elif(P1.life>0 and D1.life<0):
            print(P1.name, '获胜')
            break
        elif(P1.life<0 and D1.life>0):
            print(D1.name, '获胜')
            break
        D1.bite(P1)
        print(P1.name, '还剩', P1.life, '点血')
        time.sleep(3)

        if P1.life > 0 and D1.life > 0:
            pass
        elif (P1.life > 0 and D1.life < 0):
            print(P1.name, '获胜')
            break
        elif (P1.life < 0 and D1.life > 0):
            print(D1.name, '获胜')
            break
    elif(P1.su_du<D1.su_du):
        D1.bite(P1)
        print(P1.name,'还剩',P1.life,'点血')
        time.sleep(3)
        if P1.life>0 and D1.life > 0:
            pass
        elif(P1.life>0 and D1.life<0):
            print(P1.name, '获胜')
            break
        elif(P1.life<0 and D1.life>0):
            print(D1.name, '获胜')
            break
        P1.attack(D1)
        print(D1.name, '还剩', D1.life, '点血')
        time.sleep(2)
        if P1.life > 0 and D1.life > 0:
            pass
        elif (P1.life > 0 and D1.life < 0):
            print(P1.name, '获胜')
            break
        elif (P1.life < 0 and D1.life > 0):
            print(D1.name, '获胜')
            break