
from mcpi.minecraft import Minecraft
import time
ll=Minecraft.create()

p=0
while True:
    p=p+1
    ll.postToChat("第"+str(p)+"次")
    time.sleep(2)