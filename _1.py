from collections import Counter

a = "02452002556212556"


c = Counter(a)
#сортируем, хотя автоматически модуль уже отсортировал
c_sorted = {k: c[k] for k in sorted(c, key=c.get, reverse=True)}
print(c_sorted)







