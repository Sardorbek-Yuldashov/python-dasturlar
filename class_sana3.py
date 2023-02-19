from datetime import date, timedelta


class Sana:
    def __init__(self, day, moth, year):
        self.day = day
        self.moth = moth
        self.year = year

    def check(self):
        if self.day == self.moth:
            return True
        return False

    def sana(self):
        self.day += self.moth
        return self.day

    def get_info(self):
        return f"{self.day}-{self.moth}-{self.year}"

    def increase_month(self):
        self.moth += 1


date1 = Sana(6, 2, 2023)
date1.sana()
date1.increase_month()
print(date1.sana())
print(date1.check())
print(date1.get_info())