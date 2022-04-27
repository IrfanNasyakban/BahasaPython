### Polymorphism dengan function ###
print("~~~ Polymorphis Function : ~~~")
def tambah(x, y, z = 0):                          # Menentukan fungsi tambah dengan argumen x, y, z
    return x + y + z                              # Mengembalikan hasil dari x+y+z untuk tipe data integer
                                                  # dan string

print(tambah(2, 3, 1))                            # Menampilkan hasil tambah integer ke terminal
print(tambah(2, 3))                               # Menampilkan hasil tambah integer ke terminal
print(tambah("makan ", "nasi", " putih"))         # Menampilkan hasil tambah string ke terminal

### Polymorphism dengan class ###
print(" ")
print("~~~ Polymorphis Class : ~~~")

class Medan():                                    # Menentukan class Medan
	def khas(self):                                 # Menentukan method khas untuk class Medan
		print("Bika Ambon makanan khas Medan")        # Mencetak ke terminal

class Padang():                                   # Menentukan class Padang
	def khas(self):                                 # Menentukan method khas untuk class Padang
		print("Sate Padang makanan khas Padang")      # Mencetak ke terminal

Medan = Medan()                                   # Membuat variable Medan dari class Medan
Padang = Padang()                                 # Membuat variable Padang dari class Padang
for makanan in (Medan, Padang):                   # Melakukan Perulangan di variable Medan dan Padang
	makanan.khas()                                  # Menampilkan hasil perulangan dari method ke terminal

### Polymorphism dengan inheritance ###
print(" ")
print("~~~ Polymorphis Inheritance : ~~~")

class Laptop:                                     # Menentukan class Laptop
  def intro(self):                                # Menentukan method intro
    print("ada banyak beberapa merek laptop")     # Mencetak ke terminal
     
  def spek(self):                                       # Menentukan method spek
    print("setiap laptop memiliki spek yang berbeda")   # Mencetak ke terminal
   
class intel(Laptop):                                    # Menentukan class intel turunan dari class Laptop
  def spek(self):                                       # Menentukan method spek
    print("laptop ini memakai processor intel")         # Mencetak ke terminal
     
class amd(Laptop):                                      # Menentukan class amd turunan dari class Laptop
  def spek(self):                                       # Menentukan method spek
    print("laptop ini memakai processor amd")           # Mencetak ke terminal
     
Laptop = Laptop()                       # Membuat variable Laptop dari class Laptop
intel = intel()                         # Membuat variable Intel dari class Intel
amd = amd()                             # Membuat variable Amd dari class Amd
Laptop.intro()                          # Menampilkan variable laptop method intro ke terminal
Laptop.spek()                           # Menampilkan variable laptop method spek ke terminal
intel.intro()                           # Menampilkan variable intel dari method intro ke terminal
intel.spek()                            # Menampilkan variable intel dari method spek ke terminal
amd.intro()                             # Menampilkan variable amd dari method intro ke terminal
amd.spek()                              # Menampilkan variable amd dari method spek ke terminal