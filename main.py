from p_Class import p
from SE_Class import StatusE


player = p('Luk', 100, 100, 20, 10, 1, 1)
enemy = p('Enemy1', 100, 100, 20, 1, 1, 1)
effect1 = StatusE('Burn', 3)

print("P's HP: ", player.current_hp)
print("E's HP: ", enemy.current_hp)
print("E's HP: ", enemy.applied_effects)
effect1.applyEffect(enemy)
print("E's HP: ", enemy.applied_effects)



