from datetime import date, timedelta
class Sana:
    def __init__(self, day, moth, year):
        self.day=day
        self.moth=moth
        self.year=year

    def update_year(self):
        self.year+=1
        return self.year
    def get_sana(self):
       self.day-=2
       return self.day
    def get_date(self):
        return date(self.year, self.moth, self.day)
    def get_info(self):
        return f"{self.day}-{self.moth}-{self.year}"
year1=Sana(10, 2, 2023)
year1.update_year()
year1.get_sana()
print(year1.update_year())
print(year1.get_sana())
print(year1.get_info())