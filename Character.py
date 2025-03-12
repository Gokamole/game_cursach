import random

class Character:
    
    def __init__(self, name, health_points, defense_points, mana_points, level):
        self.name = name
        self.health_points = health_points
        self.max_health_points = health_points
        self.defense_points = defense_points
        self.mana_points = mana_points
        self.max_mana_points = mana_points
        self.level = level

    def take_damage(self, damage_amount):
        self.health_points -= max(damage_amount - self.defense_points, 0)
        if self.health_points < 0:
            self.health_points = 0
        print(f"{self.name} получил {max(damage_amount - self.defense_points, 0)} урона. Осталось здоровья: {self.health_points}")
    
    def heal(self, heal_amount):
        if self.health_points > 0:
            self.health_points += heal_amount
            self.health_points = min(self.health_points, self.max_health_points)
            print(f"{self.name} восстановил {heal_amount} здоровья и сейчас имеет {self.health_points}.")
        else:
            print(f"{self.name} не может восстановить здоровье, так как он мертв.")

    

class Mage(Character):
    
    def __init__(self, name, health_points, defense_points, mana_points, level, spell_power):
        super().__init__(name, health_points, defense_points, mana_points, level)
        self.spell_power = spell_power
    def cast_spell(self, target):
        if self.mana_points >= 10:
            target.take_damage(random.randint(10,self.spell_power))
            self.mana_points -= 10
            print(f"{self.name} наложил заклинание на {target.name}. {self.mana_points} очков маны осталось")
        else:
            print(f"{self.name} недостаточно маны для заклинания.")

    def mana(self):
        self.mana_points += (self.max_mana_points / 10)
        print(f"{self.name} восстановил {self.max_mana_points / 10} очков маны, теперь {self.mana_points} очков маны")
    
    def level_up_mage(self):
        self.level += 1
        self.max_health_points += 10
        self.health_points = self.max_health_points
        self.defense_points += 1
        self.max_mana_points += 10
        self.mana_points = self.max_mana_points
        self.spell_power += 5
        print(f"{self.name} достиг {self.level} уровня! Здоровье и мана восстановлены!")

mage = Mage("Маг", 70, 7, 50, 1, 15)

mage.cast_spell(mage)
mage.mana()
mage.take_damage(20)
mage.heal(5)
mage.level_up_mage()