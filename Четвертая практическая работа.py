class Pizzeria:

    def __init__(self, numb): # init - инициализация при создании объекта
        self.numb = numb

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self): # итератор
        if self.index >= len(range(self.numb)): #проверка - range преобразовывает в список
            raise StopIteration # вызов исключения StopIteration
        numbers = range(self.numb)[self.index] #обходим каждый элемент, и делаем досчет
        self.index += 1
        return numbers

class PizzaM(Pizzeria):
    @staticmethod
    def cooking():
        print('Margarita is cooking!')


class PizzaP(Pizzeria):
    @staticmethod
    def cooking():
        print('Pepperoni is cooking!')


print('How many pizza you want to order ?')
a = int(input())
p1 = Pizzeria(a)# создаем объект класса и передаем а в класс
for i in p1:# цикл идет по классу класса
    print('Order which pizza you want?')
    type_of_pizza = input()  # выбор типа пиццы
    while type_of_pizza != 'Margarita' and type_of_pizza != 'Pepperoni': #бесконечный цикл пока не будет выбран правильный тип
        print('No such pizza in restaurant')
        type_of_pizza = input()
    if type_of_pizza == 'Margarita':
        PizzaM.cooking() #вызов метода cooking для дочернего класса PizzaM
    elif type_of_pizza == 'Pepperoni':
        PizzaP.cooking()  # вызов метода cooking для дочернего класса PizzaP

    print('Finish!')
