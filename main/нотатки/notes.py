from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json
app = QApplication([])
window = QWidget()
main_layout = QHBoxLayout()
window.setLayout(main_layout)
window.show()
window.resize(800, 600)


note_text = QTextEdit()
main_layout.addWidget(note_text, stretch=2)

function_line = QVBoxLayout()
main_layout.addLayout(function_line)

# function line
note_list_label = QLabel("Список заміток")
function_line.addWidget(note_list_label)

note_list = QListWidget()
function_line.addWidget(note_list)

create_note_button = QPushButton("Створити замітку")
delete_note_button = QPushButton("Видалити замітку")

create_delete_note_layout = QHBoxLayout()
create_delete_note_layout.addWidget(create_note_button)
create_delete_note_layout.addWidget(delete_note_button)
function_line.addLayout(create_delete_note_layout)

save_note_button = QPushButton("зберегти замітку")
function_line.addWidget(save_note_button)


note_tag_label = QLabel("Список тегів")
function_line.addWidget(note_tag_label)

tag_list = QListWidget()
function_line.addWidget(tag_list)
find_line = QLineEdit()
function_line.addWidget(find_line)
create_tag_button = QPushButton("Створити тег")
delete_tag_button = QPushButton("Видалити тег")

create_delete_tag_layout = QHBoxLayout()
create_delete_tag_layout.addWidget(create_tag_button)
create_delete_tag_layout.addWidget(delete_tag_button)
function_line.addLayout(create_delete_tag_layout)

save_tag_button = QPushButton("зберегти тег")
function_line.addWidget(save_tag_button)

with open("нотатки\data.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

note_list.addItems(data)


def show_note():
    title = note_list.selectedItems()[0].text()
    note_text.setText(data[title]["текст"])
    tag_list.clear()
    tag_list.addItems(data[title]["теги"])
    
# текст
def add_note():
    new_note_name, ok = QInputDialog.getText(window, "додати замітку", "назва замітки ")
    if ok and new_note_name != "":
        note_list.addItem(new_note_name)
        data[new_note_name] = {"текст": "", "теги":[]}
    elif new_note_name == "":
            qm = QMessageBox()
            qm.setText("Пуста замітка")
            qm.exec_()


def save_note():
    title = note_list.selectedItems()[0].text()
    cur_note_text = note_text.toPlainText()
    cur_note_tags = data[title]["теги"]
    data[title] = {
        "текст": cur_note_text,
        "теги": cur_note_tags
    }


def del_note():
    qm = QMessageBox()
    confirm = qm.question(qm, "Видалити", "Ти хочешь видалити замітку?", qm.Yes | qm.No)
    if len(note_list.selectedItems()) != 0 and qm.Yes == confirm:
        title = note_list.selectedItems()[0].text()
        del data[title]
        note_list.clear()
        note_list.addItems(data)
        tag_list.clear()
        note_text.setText("")



# теги
def add_tag():
    title = note_list.selectedItems()[0].text()  # отримати назву замітки, яку вибрав користувач
    cur_tag_list = []
    for tag in data[title]["теги"]:
        cur_tag_list.append(tag)
    new_tile, ok = QInputDialog().getText(window, "створення тега", "введи назву:")
    if ok and new_tile != '':
        cur_tag_list.append(new_tile)
        data[title]["теги"] = tag_list
        tag_list.addItem(new_tile)
    elif new_tile == '':
        qm = QMessageBox()
        qm.setText("Empty title. Note wasn't saved")
        qm.exec_()


def del_tag():
    qm = QMessageBox()
    confirm = qm.question(qm, "Видалити", "Ти хочешь видалити тег?", qm.Yes | qm.No)
    if len(tag_list.selectedItems()) != 0 and qm.Yes == confirm:
        title = tag_list.selectedItems()[0].text()
        del data[title]
        tag_list.clear()
        tag_list.addItems(data)
        tag_list.clear()

delete_tag_button.clicked.connect(del_tag)

delete_note_button.clicked.connect(del_note)

create_tag_button.clicked.connect(add_tag)

save_note_button.clicked.connect(save_note)

create_note_button.clicked.connect(add_note)

note_list.itemClicked.connect(show_note)

app.exec_()
with open("нотатки\data.json", "w", encoding="UTF-8") as file:
    json.dump(data, file)