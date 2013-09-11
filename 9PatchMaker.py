from PIL.Image import Image
import os

import Image
from argparse import ArgumentParser

__author__ = 'jen'


#sizes indicate width of final 9 patch image. Format "directory name:width"
sizes = {"drawable-ldpi": 200,
         "drawable-mdpi": 320,
         "drawable-hdpi": 480,
         "drawable-xhdpi": 720,
         "drawable-xxhdpi": 1080,
         "drawable": 320}

class NinePatchMaker():
    def __init__(self, path):
        self.path = path
        self.pathToFile, self.basename = os.path.split(self.path)
        self.filename, self.extension = os.path.splitext(self.basename)
        if self.pathToFile == '':
            self.pathToFile = './'
        self.out = os.path.join(self.pathToFile+"/res/android_resources/")
        return


    def createFiles(self):
        for directory, width in sizes.items():
            image = Image.open(self.path)
            startingWidth, startingHeight = image.size
            resizedHeight = int(round(startingHeight * (float(width-2)/startingWidth))) #height based on resized width before border applied

            if startingWidth < sizes["drawable-xxhdpi"]:
                print "WARNING! This image is too small and might look bad at higher resolutions. It's "+str(startingWidth)+" wide."

            print "Final image dimensions for "+directory+": "+str(width)+"x"+str(resizedHeight+2)

            os.system("convert "+self.path+" +antialias -blur 0 -resize "+str(width-2)+"x"+str(resizedHeight)+
                      "\! -bordercolor 'transparent' -border 1x1 -fill black -draw 'point 1,0' -draw 'point 0,1' -draw 'point "
                      +str(width-2)+",0' -draw 'point 0,"+str(resizedHeight)+"' "+self.out+directory+"/"+self.filename+".9.png")

    def makeDirectories(self):
        for directory, size in sizes.items():
            if not os.path.exists(self.out+directory):
                print "Creating "+self.out+directory
                os.makedirs(self.out+directory)
        return

    def makeMyFiles(self):
        print "****************** \nGenerating output at: " + self.out + "\n******************"
        self.makeDirectories()
        self.createFiles()


parser = ArgumentParser(
    description = "Quick script to make 9 patch files for splash screens.",
    epilog="For best results, use with a cropped image at or exceeding the largest desired 9 patch width (currently 720px wide). " \
           "There should be no rounded corners and there should be some padding around the image for the 9 patch stretching action. " \
           "Completely transparent backgrounds are fine, too. The resulting 9-patch file will stretch to maintain being centered.")

parser.add_argument('path', help="Path to the image to be used for the splash screen.")
args=parser.parse_args()


if( __name__ == '__main__'):
    print (args.path)
    patch = NinePatchMaker(args.path)
    patch.makeMyFiles()
