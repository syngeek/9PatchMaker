9PatchMaker
===========

Simple Python script for making 9 patch files intended for centered Android splash screens. Generates resources in various sizes in the same file structure as you'd expect for your app. 

What it doesn't do (yet anyways):
 
--It doesn't let you specify an offset so if your image has rounded corners you'd like to preserve, this won't work.

--It doesn't let you specify a fill area. Don't use it for background images.

What it does really well:

--Quickly output a bunch of 9 patch files from a simple cropped image such that the content maintains its aspect ratio and only the outermost edges stretch.

To get started: Install Imagemagick and Python's PIL. Then just run it at the command line with the path to the image file it should process. All of the most common image file formats are acceptable (.png, .jpg, etc.). For a full rundown of formats see: http://www.imagemagick.org/script/formats.php

(You can also create other sizes, etc. by just changing the entries in the dict for whatever else you need.) 

No images are harmed in the creation of these 9 patch files. :)
