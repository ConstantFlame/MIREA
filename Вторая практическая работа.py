class Pizzeria:
    def which_pizza(self, type_):
        if type_ == 'Margarita':
            return PizzaM()
        elif type_ == 'Pepperoni':
            return PizzaP()



class PizzaM(Pizzeria):
    def cooking(self):
        print('Margarita is cooking!')


class PizzaP(Pizzeria):
    def cooking(self):
        print('Pepperoni is cooking!')


p1 = Pizzeria() # атрибут
a = p1.which_pizza('Margarita')
a.cooking()
b = p1.which_pizza('Pepperoni')
b.cooking