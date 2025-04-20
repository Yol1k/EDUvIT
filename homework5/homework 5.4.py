import random
from datetime import datetime, timedelta

dates = []
today = datetime.now()
for i in range(10):
    days_ago = random.randint(0, 5*365)
    date = today - timedelta(days=days_ago)
    dates.append(date)

for i in range(1, len(dates)):
    delta = dates[i] - dates[i-1]
    print(f"Разница между датами: {dates[i-1].date()} и {dates[i].date()}: {abs(delta.days)} дней")


