
from mcpi.minecraft import Minecraft
import time
ll=Minecraft.create()

x=200
y=200
z=100

ll.player.setTilePos(x,y,z)
time.sleep(2)

x=x-50
y=y-50

ll.player.setTilePos(x,y,z)
time.sleep(2)

x=x-50
y=y-50

ll.player.setTilePos(x,y,z)