'''blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#
pblocks = 0
height = 0
next_layer = 0
while True: 
    if blocks > 0:
        blocks -=1
        pblocks +=1
        next_layer = pblocks + 1
        height = next_layer
        
print("The height of the pyramid:", height)
'''

blocks = int(input("Enter the number of blocks: "))

height=0
layer_blocks=1
while blocks>=layer_blocks:
    blocks -=layer_blocks
    layer_blocks+=1
    height+=1

print("The height of the pyramid:", height)
