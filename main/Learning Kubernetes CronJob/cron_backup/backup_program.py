import os
import shutil

FILES_PATH = '/home/aishwarya/Documents/CC_027_052_062_739/main/app/backupfiles'
OUT_PATH = '/home/aishwarya/Documents/CC_027_052_062_739/main/app/output_folder'

for file in os.listdir(FILES_PATH):
	shutil.copy(os.path.join(FILES_PATH, file), os.path.join(OUT_PATH, file))

