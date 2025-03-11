class Character:
    def __init__(self, name, health_points, defense_points, mana_points,):
        self.name = name
        self.health_points = health_points
        self.max_health_points = health_points
        self.defense_points = defense_points
        self.mana_points = mana_points

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
    def __init__(self, name, health_points, defense_points, mana_points, spell_power):
        super().__init__(name, health_points, defense_points, mana_points)


character = Character("1")

character.take_damage(60)
character.heal(10)