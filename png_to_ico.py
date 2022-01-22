import os
from PIL import Image
import shutil
import time

"""
The purpose of this script is to quickly convert a large number of image
files and convert them into .ico files. I've done my best to make it as
adaptable as possible to accomodate furture expansions.

As you can see, it's currently being used to convert images into .ico icons
"""

# Gets the directory of the file the script is in
universal_directory = os.getcwd()
print(universal_directory)


def folder_nav(repository):

	"""Combines project directory and any folder within it into a single path"""

	universal_folder = os.path.join(universal_directory, repository)
	print(universal_folder)

	return universal_folder


def file_nav(repository, file):

	"""Combines any folder with a file inside it into a single path"""

	universal_file = os.path.join(repository, file)
	print(universal_file)

	return universal_file


def build(repository, input_file, ext):

	"""Builds filename from components and combines it with the folder it's in"""

	# Adds a timestamp to outgoing files to avoid conflicts
	if (repository != input_repository):
		filename = f"{file_name}_{timestamp}"
		print(filename)

	build_parts = (f"{filename}.{ext}")
	print(build_parts)

	# Get it? Like compile but it's comp *file*. I'm hilarious.
	# 11/28/21: I've left this variable abbreviation for the sake of the joke
	comp_file = os.path.join(repository, build_parts)
	print(comp_file)

	return comp_file


# Variables with the names of files in the directory
input_repository = "input"
output_repository = "output"
processed_repository = "processed"

# File extension and, in this case, a resolution variable
output_extension = "ico"
output_resolution = [(100, 100)]

input_extensions = ["png", "jpg", "jpeg"]

timestamp = str(time.time())[5:10]

# The input/output folders used to load from/save to via the folder_nav def
input_path = folder_nav(input_repository)
output_path = folder_nav(output_repository)
processed_path = folder_nav(processed_repository)

# Creates a list of all files in the input folder
inputs = os.listdir(input_path)

# For loop that runs through the files in the directory
for input_ in inputs:

	# Checks if any of the listed extensions exist within the file names
	if any(x in input_ for x in input_extensions):

		# Splits the input filename and retrieves the name
		parts = input_.split(".")
		file_name = str(parts[0])
		print(file_name)

		# Builds the path of the output folder via the build def
		save_path = build(output_repository, file_name, output_extension)
		print(save_path)

		# Gets the path of the current file in the loop and loads it into memory
		source_path = file_nav(input_repository, input_)
		print(source_path)
		source = Image.open(source_path, "r")
		print(source)

		# Converts the loaded file to the output form and saves it to file
		source.save(save_path, format=output_extension, sizes=output_resolution)

		# Moves the inital files into another file
		input_ = shutil.move(source_path, processed_path)
