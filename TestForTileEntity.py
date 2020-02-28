# Generate TestForTileEntity command
# Created by Acaran (2020)
# acaran101.wordpress.com

from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_String
from pymclevel import TAG_Float
from pymclevel import TAG_Long

displayName = "Generate TestForTileEntity"

inputs = (("Generates testfor command for minecraft 1.7.10 that successfully detects NBT data of tile entities.","label"),
		  ("Commands are generated into console from where they can be copied.","label"),
		  )

def perform(level, box, options):

	for (chunk, slices, point) in level.getChunkSlices(box):
		for e in chunk.TileEntities:
			x = e["x"].value
			y = e["y"].value
			z = e["z"].value
			id = level.blockAt(x, y, z)
			data = level.blockDataAt(x, y, z)
				
			if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
				finalString = '/testforblock ' + str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(id) + ' ' + str(data) + ' '
				finalString += investigateTag(e)
				print(finalString)
				print('')

def investigateTag(tag):
	newString = ''
	if type(tag) is TAG_List:
		newString += '['
		i = 0
		for listItem in tag:
			newString += str(i) + ':' + investigateTag(listItem) + ','
		newString += ']'
	elif type(tag) is TAG_Compound:
		newString += '{'
		for compoundItem in tag:
			newString += compoundItem + ':'
			newString += investigateTag(tag[compoundItem]) + ','
		newString += '}'
	elif type(tag) is TAG_Byte:
		newString += str(tag.value) + 'b'
	elif type(tag) is TAG_Double:
		newString += str(tag.value) + 'd'
	elif type(tag) is TAG_Short:
		newString += str(tag.value) + 's'
	elif type(tag) is TAG_Long:
		newString += str(tag.value) + 'L'
	elif type(tag) is TAG_Float:
		newString += str(tag.value) + 'f'
	elif type(tag) is TAG_String:
		newString += '"' + tag.value + '"'
	else:
		newString += str(tag.value)
	return newString