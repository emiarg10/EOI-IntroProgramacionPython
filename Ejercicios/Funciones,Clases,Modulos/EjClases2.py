class partner:
    def __init__(self):
        self._age = 0

    def get_age(self):
        return self._age

    def set_age(self,a):
        if (a<10):
            raise ValueError('Edad no permitida')
        self._age=a

    def del_age(self):
        del self._age

    age = property(get_age,set_age,del_age)
mark = partner()
mark.age=44

mark.set_age(10)
print(mark.age)
