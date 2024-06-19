from pClass import p



player = p('Luk', 100, 100, 20, 10, 1)
print(player.current_hp)
player.set_hp('reduce', 200)
print(player.current_hp)