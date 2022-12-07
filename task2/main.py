# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]

def averageAge(input):
  usersAgeList = [d['age'] for d in input]
  usersAgeListLength = len(usersAgeList)
  suma = sum(usersAgeList)
  averageAge = suma / usersAgeListLength
  averageAgeInt = int(averageAge)
  print ("Vartotojų amžiaus vidurkis yra:", averageAgeInt, "metų")

averageAge(users)

usersNamesList = []
def getUsersNames(input):
  for x in  ([d['name'] for d in input]):
    usersNamesList.append(x)

  print ("Vartotojų vardų sąrašas :" , usersNamesList)

getUsersNames(users)