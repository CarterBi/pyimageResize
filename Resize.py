import PIL
from PIL import Image
def resize_and_save(filename,size):
	im = Image.open(filename)
	new_im = im.resize(size)
	
	name_parts = filename.split(".")
	new_im.save(name_parts[0] + "_resized." + name_parts[1])

filename = raw_input("What file to change?")
print "How would you like to resize?"
print "1) Fixed size"
print "2) Change to a %"
print "3) Set longest edge"
choice = raw_input("")
if (choice == "1"):
	width = int(raw_input("What is new width?"))
	height = int(raw_input("What is new height?"))
	resize_and_save(filename,(width,height))
elif (choice == "2"):
	im = Image.open(filename)
	old_size = im.size
	if (percent[-1] == "%"):
		percent
	percent = raw_input("What % to scale to?")
	scale = int(percent)/100.0
	new_width = int(old_size[0] * scale)
	new_height = int (old_size[1] * scale)
	new_size = (new_width,new_height)

	resize_and_save(filename,new_size)
elif (choice == "3"):
	im = Image.open(filename)
	old_size = im.size
	longest_edge = int(raw_input("What is the longest edge?"))
	x = max(old_size[0],old_size[1])
	longest_edge = float(longest_edge)
	new_scale = longest_edge/x
	new_width = int(old_size[0] * new_scale)
	new_height = int (old_size[1] * new_scale)
	new_size = (new_width, new_height)

	resize_and_save(filename,new_size)
	