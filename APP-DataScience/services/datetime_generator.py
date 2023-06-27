import random
import datetime

def random_datetime():
    year = random.randint(2023, 2023)
    month = random.randint(4, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime.datetime(year, month, day, hour, minute, second)