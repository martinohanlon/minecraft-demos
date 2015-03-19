#import the minecraft.py module from the minecraft directory
import mcpi.minecraft as minecraft
#import minecraft block module
import mcpi.block as block
#import time, so delays can be used
import time

#Connect to minecraft by creating the minecraft object
# - minecraft needs to be running and in a game
mc = minecraft.Minecraft.create()

#get the players position
pos = mc.player.getTilePos()

time.sleep(3)

#change block in front of player
mc.setBlock(pos.x, pos.y, pos.z + 1, block.STONE.id)

time.sleep(10)

for count in range(1,4):
    #change it to wood and back to stone
    mc.setBlock(pos.x, pos.y, pos.z + 1, block.WOOD.id)
    time.sleep(1)
    mc.setBlock(pos.x, pos.y, pos.z + 1, block.STONE.id)
    time.sleep(1)

blockIdsToUse = [2,3,4,5,6,7,8,12,13,14,15,16,17,18,20,21,22,24,30,31,35,41,42,45,46,47,48,49,51,54,56,57,58,61,62,73,78,79,80,81,82,83,89]
for blockId in blockIdsToUse:
    mc.setBlock(pos.x, pos.y, pos.z + 1, blockId)
    time.sleep(0.5)
