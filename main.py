
class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.hapiness = 100
        self.money = 500
        self.mess = 0
        self.auto_status = 0

    def chill(self):
        self.hapiness += 10
        self.mess += 10

    def clean_home(self):
        self.hapiness -= 5
        self.mess = 0

    def fix_auto(self):
        self.auto_status = 100
        self.money -= 50

    def output_info(self):
        print(f"info for {self.name}: \nHappiness: {self.hapiness} \nMoney: {self.money} \nMess in flat: {self.mess}"
              f" \nAuto Status: {self.auto_status}%\n\n")


human = Human("Timur")
human.output_info()
human.chill()
human.output_info()
human.clean_home()
human.output_info()
human.fix_auto()
human.output_info()
