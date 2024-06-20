from p_Class import p
from SE_Class import StatusE
from ControlSystem_Class import ControlSystem



session = ControlSystem()
enemy = p('Enemy1', 100, 100, 20, 1, 1, 1)

myteam = {session.createPEntity("Unit1"), session.createPEntity("Unit2")}
myEnemy = {}
session.add_team(myteam)


print(session.team)








