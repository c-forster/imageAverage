#!/usr/bin/python

import sys, os
from PIL import Image, ImageStat

def main(imageFilename):

    image = Image.open(imageFilename)

    outfilename = os.path.splitext(imageFilename)[0] + '_sorted.png'

# Change this line to image = imageSort(image) for a non-column based sort.
    image = columnSort(image)

    image.save(outfilename)
    print imagFilename " outputted to " outfilename "; average brightness ", brightnessAverage(image)


def columnSort(image):
    pixels = list(image.getdata())
    (width, height) = image.size

    # Loop through each column.
    for column in range(0,width):
        print "Sorting column ", column, " of ", height, "."
        pixelColumn = []

        for x in range(0,height):
            pixelColumn.append(pixelList[x*width + column])

        pixelColumn = sorted(pixelColumn,reverse=True)


        for x in range(0,height):
            pixelList[x*width + column] = pixelColumn[x]

    
    image.putdata(pixelList)
    return image

def imageSort(image):
    pixelList = list(image.getdata())
    (width, height) = image.size

    pixelList = sorted(pixelList) # Sort as a single list
    
    image.putdata(pixelList)
    return image


def brightnessAverage(image):
    greyImage = image.convert('L')
    stat = ImageStat.Stat(greyImage)

    return stat.mean[0]

if __name__ == "__main__":
    main(sys.argv[1])
