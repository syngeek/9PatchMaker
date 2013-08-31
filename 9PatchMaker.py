import os
import PythonMagick
from argparse import ArgumentParser

__author__ = 'jen'


#sizes indicate width of final 9 patch image. Format "directory name:width"
sizes = {"drawable-ldpi": 240,
         "drawable-mdpi": 240,
         "drawable-hdpi": 320,
         "drawable-xhdpi": 480,
         "drawable-xxhdpi":720,
         "drawable": 320}

class NinePatchMaker():
    def __init__(self, path):
        self.path = path
        self.pathToFile, self.basename = os.path.split(self.path)
        self.filename, self.extension = os.path.splitext(self.basename)

        self.out = self.pathToFile+"/res/android_resources/"

        print "Generating output at: " + self.out
        return


    def createFiles(self):
        for directory, width in sizes.iteritems():
            #Get the image so we can get some measurements the easy way
            image = PythonMagick.Image(self.path)
            #Resize and measure. Will use this to inform the actual Imagemagick command.
            #Convoluted because there was no way to disable anti-aliasing in PythonMagick.
            image.resize(str(width-2)+"x")
            print "Resized image dimensions for "+directory+": "+str(image.size().width()+2)+"x"+str(image.size().height()+2)

            os.system("convert "+self.path+" +antialias -blur 0 -resize "+str(width-2)+
                      " -bordercolor 'transparent' -border 1x1 -fill black -draw 'point 1,0' -draw 'point 0,1' -draw 'point "
                      +str(width-2)+",0' -draw 'point 0,"+str(image.size().height())+"' "+self.out+directory+"/"+self.filename+".9.png")


    def makeDirectories(self):
        for directory, size in sizes.iteritems():
            if not os.path.exists(self.out+directory):
                print "Creating "+self.out+directory
                os.makedirs(self.out+directory)
        return

    def makeMyFiles(self):
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
    patch = NinePatchMaker(args.path)
    patch.makeMyFiles()
