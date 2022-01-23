import os
from PIL import Image
import shutil
import time
import imghdr


"""
The purpose of this script is to quickly convert a large number of image
files and convert them into .ico files. I've done my best to make it as
adaptable as possible to accomodate furture expansions.

As you can see, it's currently being used to convert images into .ico icons
"""

# Gets the directory of the file the script is in
univ_dir = os.getcwd()
# print(univ_dir)


def folder_nav(location):

	"""Combines project directory and any folder within it into a single path"""

	univ_folder = os.path.join(univ_dir, location)
	# print(univ_folder)

	return univ_folder


def file_nav(location, file):

	"""Combines any folder with a file inside it into a single path"""

	univ_file = os.path.join(location, file)
	# print(univ_file)

	return univ_file


def build(location, in_file, ext):

	"""Construct filenames from components"""

	if (location != in_location):
		file_name = f"{file_name}_{ts}"

	build_parts = (f"{file_name}.{ext}")

	# Get it? Like compile but it's comp *file*. I'm hilarious.
	comp_file = os.path.join(location, build_parts)

	return comp_file


# Define the name of each folder used
in_location = "input"
out_location = "output"
proc_location = "processed"

out_extension = "ico"
out_resolution = []

in_extensions = ["png", "jpg", "jpeg", "gif", "tiff"]

# Generate time stamp to avoid name conflicts
ts = str(time.time())[5:10]

# Create full file path for each folder
in_path = folder_nav(in_location)
out_path = folder_nav(out_location)
proc_path = folder_nav(proc_location)

# List all files in the input folder
inputs = os.listdir(in_path)
print(inputs)

for in_ in inputs:

	# Check if the file has a valid image extension
	if any(x in in_ for x in in_extensions):

		parts = in_.split(".")
		file_name = str(parts[0])

		# Build output path for shutl
		save_path = build(out_location, file_name, out_extension)

		# Load source image and convert it
		source_path = file_nav(in_location, in_)
		print(source_path)
		source = Image.open(source_path, "r")

		# Find source image dimensions
		res = source.size
		out_resolution.append(res)

		source.save(save_path, format=out_extension, sizes=out_resolution)

		# Move source file to archive
		# in_ = shutil.move(source_path, proc_path)
