import random
class Cat:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.hunger = 0
        self.alive = True

    def to_eat(self):
        print("Time to eat")
        self.hunger += 5
        self.gladness += 10

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.hunger -= 3

    def is_alive(self):
        if self.hunger < 3:
            print("I am hungry(")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.hunger > 5:
            print("My belly is full")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"hunger = {round(self.hunger, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Cat(name="Nick")
kate = Cat(name="Kate")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
    if kate.alive == False:
        break
    kate.live(day)

#
#
#
#


# class Student:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         print(self)
#
# first_student = Student()
# print(first_student.height)