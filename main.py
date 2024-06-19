from pClass import p


player = p('Luk', 100, 100, 20, 10, 1)
enemy = p('Enemy1', 100, 100, 20, 1, 1)

print("P's HP: ", player.current_hp)
print("E's HP: ", enemy.current_hp)

print("after attack: ", player.ap , " Damage!")
player.engageOtherEntity(enemy)
print("E's HP: ", enemy.current_hp)
