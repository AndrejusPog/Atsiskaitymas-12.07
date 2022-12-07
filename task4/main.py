# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 


class Movie:
    def __init__(self,title:str,director:str,budget:int):
        self.title = title
        self.director = director
        self.budget = budget
        
    def wasExpensive(self):
        if self.budget > 100000000:
            return True
        else:
            return False


        

filmas1 = Movie("Alien","Tarantino",200000000)
        
filmas2 = Movie("Rambo","Velyvis",300000)


print(filmas1.wasExpensive())
print(filmas2.wasExpensive())