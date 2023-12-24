class Date:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __int__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
    def __init__(self, string_date: str):
        date_arr = list(map(int, string_date.split('.')))
        if 0 <= date_arr[0] <= 31 and 0 <= date_arr[1] <= 12:
            self.day = date_arr[0]
            self.month = date_arr[1]
            self.year = date_arr[2]
        else:
            raise ValueError("Input is not valid")

    def getTotalDays(self) -> int:
        return self.day + sum(self.days_in_month[:self.month + 1]) + self.year * 365


    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __sub__(self, date) -> int:
        return abs(self.getTotalDays() - date.getTotalDays())

    def __add__(self, arg):

        days_to_add = 0

        if isinstance(arg, Date):
            days_to_add = self.getTotalDays()
        elif isinstance(arg, int):
            days_to_add = arg
        else:
            raise TypeError("type is not valid")
        new_days = self.day + days_to_add
        new_month = self.month
        new_year = self.year
        while new_days > self.days_in_month[new_month]:
            new_days -= self.days_in_month[new_month]
            new_month += 1
            if (new_month == 12):
                new_month = 0
                new_year += 1
        return Date(f"{new_days}.{new_month}.{new_year}")

    def __eq__(self, date):
        return self.getTotalDays() == date.getTotalDays()

    def __gt__(self, date):
        return date.getTotalDays() - self.getTotalDays() > 0

    def __ge__(self, date):
        return date.getTotalDays() - self.getTotalDays() >= 0

    def __lt__(self, date):
        return date.getTotalDays() - self.getTotalDays() < 0

    def __le__(self, date):
        return date.getTotalDays() - self.getTotalDays() <= 0






def main():
    a = Date("11.00.11")
    b = Date("11.00.11")
    print(a >= b)
