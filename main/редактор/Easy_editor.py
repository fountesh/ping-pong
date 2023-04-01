from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PIL import Image, ImageFilter, ImageEnhance
import os
app = QApplication([])
window = QWidget()
main_layput = QHBoxLayout()
window.setLayout(main_layput)
window.resize(700, 500)

#папки та список картинок
folder_picture_list_line = QVBoxLayout()
folder_button = QPushButton("обрати папку")
picture_list = QListWidget()
folder_picture_list_line.addWidget(folder_button)
folder_picture_list_line.addWidget(picture_list)
main_layput.addLayout(folder_picture_list_line)

#картина та кнопкі
picture_button_line = QVBoxLayout()
button_line = QHBoxLayout()
picture = QLabel("картина")
left_button = QPushButton("вліво")
right_button = QPushButton("вправо")
miror_button = QPushButton("дзеркало")
sharpness_button = QPushButton("різкість")
b_w_button = QPushButton("ч/б")
button_line.addWidget(left_button)
button_line.addWidget(right_button)
button_line.addWidget(miror_button)
button_line.addWidget(sharpness_button)
button_line.addWidget(b_w_button)
picture_button_line.addWidget(picture)
picture_button_line.addLayout(button_line)
main_layput.addLayout(picture_button_line, stretch=5)

#обрати папку
    
def filter_files(file_list, extensions):
    result = []
    for file in file_list:
        for extension in extensions:
            if file.endswith(extension):
                result.append(file)
    return result

path_dir_address = ""
def choose_folder():
    global path_dir_address
    path_dir_address = QFileDialog.getExistingDirectory()
    try:
        files = os.listdir(path_dir_address)
        extensions = ["png", "svg", "jpeg", "jpg" ]
        program_files = filter_files(files, extensions)
        picture_list.clear()
        picture_list.addItems(program_files)
    except:
        print("Порожня папка")


class ImageProcessor:
    def __init__(self, image, originalName, saveFolderName):
        self.image = image
        self.original_name = originalName
        self.saveFolderName = saveFolderName
    
    def load_image(self, filename):
        global path_dir_address
        file_path = os.path.join(path_dir_address, filename)
        self.original_name = file_path
        self.image = Image.open(file_path)

    def show_image(self, path):
        picture.hide()
        pixmapimage = QPixmap(path)
        picture_w, picture_h = picture.width(), picture.height()
        pixmapimage = pixmapimage.scaled(picture_w,  picture_h, Qt.KeepAspectRatio)
        picture.setPixmap(pixmapimage)
        picture.show()
    
    
    def save_image(self):
        global path_dir_address
        save_address = os.path.join(path_dir_address, "Processed")
        if not os.path.exists(save_address):
            os.mkdir(save_address)
        saved_image = os.path.join(save_address, self.original_name)
        self.image.save(saved_image)
        self.file_path = saved_image

    def do_bw(self):
        self.image = self.image.convert("L")
        self.save_image()
        self.show_image(self.file_path)
    
    def do_right(self):
        self.image = self.image.transpose(Image.Transpose.ROTATE_90)
        self.save_image()
        self.show_image(self.file_path)

    def do_left(self):
        self.image = self.image.transpose(Image.Transpose.ROTATE_270)
        self.save_image()
        self.show_image(self.file_path)
    
    def do_miror(self):
        self.image = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.save_image()
        self.show_image(self.file_path)
    
    def do_con(self):
        pic_contrast = ImageEnhance.Contrast(picture)
        pic_contrast = pic_contrast.enhance(1.5)
        self.save_image()
        self.show_image(self.file_path)

folder_button.clicked.connect(choose_folder)

workPicture = ImageProcessor('', '', '')

b_w_button.clicked.connect(workPicture.do_bw)
right_button.clicked.connect(workPicture.do_right)
left_button.clicked.connect(workPicture.do_left)
miror_button.clicked.connect(workPicture.do_miror)
sharpness_button.clicked.connect(workPicture.do_con)

def change_image():
    filename = picture_list.selectedItems()[0].text()
    workPicture.load_image(filename)
    workPicture.show_image(workPicture.original_name)




picture_list.itemClicked.connect(change_image)




window.show()
app.exec_()