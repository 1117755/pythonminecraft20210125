
from mcpi.minecraft import Minecraft
ll=Minecraft.create()

ll.postToChat("I'am watching you")

while True:
    x,y,z=ll.player.getTilePos()
    ll.postToChat("x:"+str(x)+"y:"+str(y)+"z:"+str(z))