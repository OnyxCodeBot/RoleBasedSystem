from p_Class import p
from SE_Class import StatusE
from ControlSystem_Class import ControlSystem


session = ControlSystem()
player = p('Luk', 100, 100, 20, 10, 1, 1)
enemy = p('Enemy1', 100, 100, 20, 1, 1, 1)

player.debufEntity("effect_rand", enemy)


session.updateEffects(enemy)

print(enemy.applied_effects)




