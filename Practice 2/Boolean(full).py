#Примеры операторов, < , > == и тд
print(10 > 9)
print(10 == 9)
print(10 < 9)
print(not(x > 5))         # False
print(not(x < 5))         # True

#Проверка пустое ли или нет
print(bool("Hello")) #true
print(bool(15)) #true
bool("")        # False (пустой)
bool(0)         # False (0)
bool(None)      # False
bool([])        # False (пустой лист)
bool({})        # False (пустой)

#Проверяет размер, если равно 0, то retern 0
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Проверка самого значения, и типа данных, если совпадают, то true, если нет, то false
x = 200
print(isinstance(x, int))    #True
print(isinstance(x, int))     # True
print(isinstance(x, float))   # False
print(isinstance(x, str))     # False
