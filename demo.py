import pyblock

# Define the block(s) to use
bedrock = pyblock.Block('minecraft', 'bedrock')

# Define the path to the world
path = r"C:\Users\Vicky\Desktop\Repository\PyBlock\examples"

# Initialize the editor
editor = pyblock.MCEditor(path)

# Begin setting blocks
for y in range(250):
	for x in range(500, 1000):
		editor.set_block(bedrock, x, y, 2000)
		editor.set_block(bedrock, x, y, 1500)
	for z in range(1500, 2000):
		editor.set_block(bedrock, 500, y, z)
		editor.set_block(bedrock, 1000, y, z)

# Only here the actual regions are loaded and the changes applied.
editor.done()
