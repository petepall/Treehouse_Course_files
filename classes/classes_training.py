class Person:
    def __init__(self, first: str, last: str, age: int):
        self.first = first
        self.last = last
        self.age = age

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    def __str__(self):
        return f"{self.first}, {self.last} is {self.age} old"

    def __repr__(self):
        return f"Person {self.first}, {self.last}, {self.age}"

    @classmethod
    def from_string(cls, person_str: str):
        first, last, age = person_str.split("-")
        return cls(first, last, int(age))

    def fullname(self):
        return f"{self.first} {self.last}"

    def add_year(self):
        self.age = int(self.age + 1)


class Shooter(Person):
    def __init__(self, first: str, last: str, age: int, weapon_type: str):
        super().__init__(first, last, age)
        self.weapon_type = weapon_type

    def __str__(self):
        return (
            f"{self.first}, {self.last} is {self.age} old and "
            f"shoots {self.weapon_type}"
        )

    def __repr__(self):
        return (
            f"Person {self.first}, {self.last}, {self.age}, "
            f"{self.weapon_type}"
        )


class Trainer(Person):
    def __init__(self, first, last, age, shooters=None):
        super().__init__(first, last, age)
        if shooters is None:
            self.shooters = []
        else:
            self.shooters = shooters

    def __str__(self):
        return (
            f"{self.first}, {self.last} is {self.age} old and "
            f"is trainer for "
            f"{[shooter.fullname() for shooter in self.shooters]}"
        )

    def __repr__(self):
        return (
            f"Person {self.first}, {self.last}, {self.age}, "
            f"{[shooter.fullname() for shooter in self.shooters]}"
        )

    def add_trainer(self, shooter):
        if shooter not in self.shooters:
            self.shooters.append(shooter)

    def remove_trainer(self, shooter):
        if shooter in self.shooters:
            self.shooters.remove(shooter)

    def print_trainer(self):
        for shooter in self.shooters:
            if shooter is not None:
                return f"--> {shooter.fullname()}"
            else:
                break


person1 = Person("Peter", "Pallen", 46)
person2 = Person("Carine", "Pallen", 53)

print(person1)
print(person2)

shooter1 = Shooter("Peter", "Pallen", 46, "Rifle")
shooter2 = Shooter("Bart", "Libens", 43, "Pistol")

print(shooter1)
print(shooter2)
print()
print(shooter1.fullname())
print(shooter2.fullname())

print()
trainer1 = Trainer("Peter", "Demey", 55, [shooter1, shooter2])

print(trainer1.print_trainer())
print(trainer1)
print()

# print(repr(trainer1))
print(trainer1.__repr__())
print()
print(person1.email)
