class MyError(Exception):
    def __init__(self, value):
        if value:
            self.value = value
        else:
            self.value = None

    def __str__(self):
        if self.value:
            return f"MyError, {self.value}"
        else:
            return "MyError has been raised"


class MyClass:
    def __init__(self, age, name, sex):
        self.age = age
        self.name = name
        self.sex = sex

    def over_age_check(self):
        if self.age > 111:
            raise MyError(f"Можлива помилка: введений вік ({self.age}) більший за 111")
        else:
            print("Все корректно!")


first_char = MyClass(age=98, name="Natali", sex="Female")
first_char.over_age_check()

#second_char = MyClass(age=122, name="Oksana", sex="Female")
#second_char.over_age_check()
