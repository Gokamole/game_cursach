class Person:
    def __init__(self, name, health_points, attack_points, defense_power, mana_points):
        self.name = name
        self.hp = health_points
        self.ap = attack_points
        self.defense = defense_power
        self.mana = mana_points
        self.heal_amount = health_points / 10
    
    def attack(self, target):
        damage = self.ap
        target.take_damage(damage)
        print(f"{self.name} атаковал {target.name} и нанёс {damage} урона.")

character1 = Person("Виктор", 50, 10, 5, 20)
character2 = Person("Петр", 50, 10, 5, 20)

character1.attack(character2)