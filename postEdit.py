from PyQt6 import QtWidgets, QtCore, QtGui
import sys

style = ("""
            QLineEdit {
                height: 30px;
                font-size: 20px;
                font-family: 'Open Sans';
                border: none;
                border-bottom: 1px solid black;
            }
            QTextEdit {
                font-size: 20px;
                font-family: 'Open Sans';
                border: none;
            }
        """)

class PostTextEdit(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()
        document = QtGui.QTextDocument()
        document.setDefaultFont(QtGui.QFont('Open Sans', pointSize=20))
        self.setDocument(document)
        self.setPlaceholderText("Текст")
        self.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        self.setWordWrapMode(QtGui.QTextOption.WrapMode.WordWrap)

    def insert_from_clipboard(self):
        if self.clipboard.mimeData().hasText():
            print(1)

class PostEdit(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 300)
        #widgets
        nameEdit = QtWidgets.QLineEdit()
        textEdit = PostTextEdit()
        btn = QtWidgets.QPushButton("Отправить")
        #editMenu
        edit_menu_hbox = QtWidgets.QHBoxLayout()
        edit_menu_h1 = QtWidgets.QLabel("h1")
        edit_menu_h2 = QtWidgets.QLabel("h2")
        edit_menu_h3 = QtWidgets.QLabel("h3")
        edit_menu_i = QtWidgets.QLabel("i")
        edit_menu_b = QtWidgets.QLabel("B")
        edit_menu_s = QtWidgets.QLabel("S")
        edit_menu_u = QtWidgets.QLabel("U")
        edit_menu_hbox.addWidget(edit_menu_h1, 0)
        edit_menu_hbox.addWidget(edit_menu_h2, 0)
        edit_menu_hbox.addWidget(edit_menu_h3, 0)
        edit_menu_hbox.addWidget(edit_menu_i, 0)
        edit_menu_hbox.addWidget(edit_menu_b, 0)
        edit_menu_hbox.addWidget(edit_menu_s, 0)
        edit_menu_hbox.addWidget(edit_menu_u, 0)
        edit_menu_hbox.addStretch(stretch=0)
        #textline settings
        nameEdit.setMaxLength(40)
        nameEdit.setDragEnabled(True)
        nameEdit.setPlaceholderText("Заголовок")
        #editMenu settings
        cursor_editMenu = QtCore.Qt.CursorShape.PointingHandCursor
        edit_menu_h1.setCursor(cursor_editMenu)
        edit_menu_h2.setCursor(cursor_editMenu)
        edit_menu_h3.setCursor(cursor_editMenu)
        edit_menu_i.setCursor(cursor_editMenu)
        edit_menu_b.setCursor(cursor_editMenu)
        edit_menu_s.setCursor(cursor_editMenu)
        edit_menu_u.setCursor(cursor_editMenu)

        #layout
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(nameEdit)
        vbox.addWidget(textEdit)
        vbox.addLayout(edit_menu_hbox)
        vbox.addWidget(btn)
        self.setLayout(vbox)
        self.setStyleSheet(style)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = PostEdit()
    login.show()
    app.exec()