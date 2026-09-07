from abc import ABC, abstractmethod

# =====================================================================
# KODING GABUNGAN LATIHAN 1 SAMPAI 6 (SISTEM GAME RPG)
# =====================================================================

# Latihan 5: Abstraction (Blueprint Utama)
class GameUnit(ABC):
    @abstractmethod
    def serang(self, lawan):
        pass

    @abstractmethod
    def info(self):
        pass

# Latihan 1, 2, & 4: Parent Class dengan Enkapsulasi
class Hero(GameUnit):
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.__hp = hp # Latihan 4: Atribut Private

    # Latihan 4: Getter & Setter untuk mengamankan data
    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        else:
            self.__hp = nilai_baru

    # Latihan 2: Method Interaksi
    def diserang(self, damage):
        print(f"{self.name} menerima kerusakan sebesar {damage}!")
        self.set_hp(self.get_hp() - damage)

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def info(self):
        print(f"Hero: {self.name} | HP: {self.get_hp()} | ATK: {self.attack_power}")

# Latihan 3 & 6: Inheritance (Pewarisan) & Polymorphism
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power) # Latihan 3: Fungsi super()
        self.mana = mana

    # Latihan 6: Polimorfisme (Perilaku Serang yang Berbeda)
    def serang(self, lawan):
        print(f"{self.name} (Mage) melemparkan sihir ke {lawan.name}!")
        lawan.diserang(self.attack_power + 20)

class Fighter(Hero):
    def serang(self, lawan):
        print(f"{self.name} (Fighter) menebas {lawan.name} dengan pedang!")
        lawan.diserang(self.attack_power)

# Latihan 6: Menambahkan class baru untuk membuktikan skalabilitas
class Healer(Hero):
    def serang(self, lawan):
        print(f"{self.name} tidak menyerang, tapi menyembuhkan teman!")

# Jalannya Program
if __name__ == "__main__":
    hero1 = Mage("Eudora", 100, 30, 50)
    hero2 = Fighter("Alucard", 150, 40)
    hero3 = Healer("Estes", 120, 10)

    # Polimorfisme dalam perulangan
    pasukan = [hero1, hero2, hero3]
    print("=== SIMULASI PERTARUNGAN RPG ===")
    for pahlawan in pasukan:
        pahlawan.info()
        print("-" * 30)