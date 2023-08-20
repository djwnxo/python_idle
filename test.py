from mcpi.minecraft import Minecraft
import keyboard as kb
import time
import mcpi.block as block
BLOCKDISTANCE = 5
mc = Minecraft.create()

def flash():
    flag = False
    if kb.is_pressed('f'):
        if flag == False:
            direction = mc.player.getDirection()
            pos = mc.player.getPos()
            x = round(pos.x + (direction.x * BLOCKDISTANCE))
            y = pos.y
            z = round(pos.z + (direction.z * BLOCKDISTANCE))
            mc.player.setPos(x,y,z)
            flag = True
            time.sleep(5)
            flag = False
while True:
    flash()
    
    if kb.is_pressed('q'):
        mc.postToChat("끝났습니다.")
        break
