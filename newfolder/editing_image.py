from PIL import Image
import os
import glob

def image_edit(img3, i):
    img = Image.open(img3)
    width, height = img.size
    img = img.crop(
        (
            width - 1867,
            height - 971,
            width - 975,
            height - 150
            )
        )
    img.save("img" + str(i) + ".jpg")

def append_image_list(x):
    for file in glob.glob("*.JPG"):
        x.append(file)
    return
def append_image_list_new(x):
    for file in glob.glob(r'*img\d+'):
        x.append(file)
        return
os.chdir(r'C:\Users\D&A\Documents\python folder\newfolder')
all_jpg = list()
new_img_jpg = list()
append_image_list(all_jpg)
i = 0
while i != len(all_jpg):
    image_edit(all_jpg[i], i)
    i += 1
append_image_list_new(new_img_jpg)
'''
print("are these pictures edited?[yes/no]")
response = input()
if response == 'yes' or 'Yes' or 'YES' or 'yES' or 'yeS':
    for i in range(len(all_jpg)-1):
        image_edit(all_jpg[i], i)#where am I going to save it? it should be in a new folder
elif response != 'yes' or 'Yes' or 'YES' or 'yES' or 'yeS':
    print('you have a problem')
'''
print(new_img_jpg)
print(all_jpg)
