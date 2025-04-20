import random
import math
import statistics as stats

a=[random.randint(1,100) for i in range(100)]

a_mean = stats.mean(a)

a_med = stats.median(a)

a_stdev=stats.stdev(a)

b = round(math.sqrt(sum(a)))

print(f"Среднее: {a_mean}, Медиана: {a_med}, Стандартное отклонение: {a_stdev},Корень из суммы : {b}")
