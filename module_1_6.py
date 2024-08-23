# Работа со словарями
my_dict = {"Denis": 2001, "Yaroslav": 2005}
print(my_dict)
print(my_dict.get("Denis"), my_dict.get("Anton", "Емае про Антона забыли"))
my_dict.update({"Anton": 2002, "Mihail228": 20228})
del_value = my_dict.pop("Mihail228")
print(del_value)
print(my_dict)

# Работа с множествами
my_set = {1, 1, 1, 1, int(True), bool('12'), "не 1)"}
print(my_set)
my_set.update({52, "SPB"})
my_set.discard(1)
print(my_set)
