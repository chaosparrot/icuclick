from PIL import ImageOps, Image
import os

# Configurations
RAW_DIR = 'data/raw/'
PROCESSED_DIR = 'data/processed/'
size = 128
halfsize = 128 / 2

for fileindex, file in enumerate(os.listdir( RAW_DIR )):
	img = Image.open(RAW_DIR + file)
	print( "Processing " + file + "..." )
	totalSize = img.size
	
	values = file.split('--')
	positions = values[1].split('-')
	centerx = int(positions[0])
	centery = int(positions[1])

	bounds = ( centerx - halfsize, centery - halfsize, totalSize[0] - halfsize - centerx, totalSize[1] - halfsize - centery )
	croppedImg = ImageOps.crop(img, bounds)
	croppedImg.save( PROCESSED_DIR + values[0] + '-' + values[2] )
	
print( "Done! " )