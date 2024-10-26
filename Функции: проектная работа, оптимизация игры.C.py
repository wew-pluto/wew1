import random
def dice(ta=True):
 tc=0
 if ta==True:
  print("Сколько кубиков хотите бросить?")
  ta=float(input())
 if ta>=1 and ta<=3 and ta==ta//1:
  print(int(ta))
  print("Вы бросаете "+str(int(ta))+" кубиков")
  for tq in range(int(ta)):
   tb=random.randint(1,6)
   tc+=tb
   print("Кубик "+str(tq+1)+": "+str(tb))
  print("Суммарный результат: "+str(tc))
 else: 
  print("Нельзя бросить столько кубиков, попробуйте снова")
#  dice(ta)
dice()
