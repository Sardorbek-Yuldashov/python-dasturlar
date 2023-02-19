from datetime import date, timedelta
class Sana:
    def __init__(self, day, moth, year):
        self.day=day
        self.moth=moth
        self.year=year
    def check_kabisa(self):
        if self.year%4==0 and self.year%400==0 or self.year %100!=0:
            return True
        return False
    def add_five_days(self):
        return self.get_date()+timedelta(days=5)
    def get_date(self):
        return date(self.year, self.moth, self.day)
date1=Sana(5, 2, 2020)
print(date1.check_kabisa())