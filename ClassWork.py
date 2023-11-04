import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def to_repair(self):
        if self.car:
            self.car.strength = brands_of_car[self.car.brand]["strength"]

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def chill(self):
        self.gladness += 10
        self.home.mess += 10

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.home.food > 0:
                self.home.food -= 5
                self.satiety += 100

    def work(self):
        if self.job:
            self.money += self.job.salary

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print("i bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")

    def live(self, day):
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("ill go eat!")
        elif self.gladness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                print(f"{self.name}'s chill")
        elif self.money < 0:
            self.work()
        elif self.car.strength < 15:
            self.to_repair()
        elif dice == 1:
            self.chill()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.clean_home()
        elif dice == 4:
            self.shopping("delicacies")


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move!")


class Job:
    def __init__(self, joblist):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 60, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 15},
}


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 80, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}

nick = Human("Nick", Job(job_list), House(), Auto(brands_of_car))
for i in range(1, 356):
    nick.live(i)
