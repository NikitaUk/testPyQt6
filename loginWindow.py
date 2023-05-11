from PyQt6 import QtWidgets, QtGui, QtCore
import sys

style = ("""
            #title_lbl {
                font-size: 40px;
                font-family: 'Open Sans';
                color: #deb37e;
            }
            #subtitle_lbl {
                font-size: 20px;
                font-family: 'Open Sans';
                color: #54524f;
            }
            #edit {
                height: 30px;
                font-size: 25px;
                border: 2px solid grey;
            }
            #btn {
                height: 40px;
                width: 100px;
                font-size: 20px;
                font-family: 'Open Sans';
                background-color: #e2a355;
                color: #ffffff;
                border-radius: 10px;
                border: none;
            }
            #correct {
                color: red;
            }
        """)

class RegistrationWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 500)
        #настройки окна
        vbox = QtWidgets.QVBoxLayout()
        #компоненты
        title_lbl = QtWidgets.QLabel("<center>Регистрация</center>")
        mail_lbl = QtWidgets.QLabel("<center>Введите почту: </center>")
        mail_edit = QtWidgets.QLineEdit()
        correct_mail_lbl = QtWidgets.QLabel("<center>Введите корректные значения</center>")
        nik_lbl = QtWidgets.QLabel("<center>Введите ник: </center>")
        nik_edit = QtWidgets.QLineEdit()
        correct_nik_lbl = QtWidgets.QLabel("<center>Ваш ник должен быть больше 3 символов</center>")
        password_lbl = QtWidgets.QLabel("<center>Введите пароль: </center>")
        password_edit = QtWidgets.QLineEdit()
        correct_psw_lbl = QtWidgets.QLabel("<center>Ваш пароль должен быть больше 4 символов</center>")
        confirmPassword_lbl = QtWidgets.QLabel("<center>Подтвердите пароль: </center>")
        confirmPassword_edit = QtWidgets.QLineEdit()
        correct_confirmPsw_lbl = QtWidgets.QLabel("<center>Ваш пароль не совпадает</center>")
        enter_btn = QtWidgets.QPushButton("Регистрация")
        #styles
        title_lbl.setObjectName('title_lbl')
        mail_lbl.setObjectName('subtitle_lbl')
        nik_lbl.setObjectName('subtitle_lbl')
        password_lbl.setObjectName('subtitle_lbl')
        confirmPassword_lbl.setObjectName('subtitle_lbl')
        mail_edit.setObjectName('edit')
        nik_edit.setObjectName('edit')
        password_edit.setObjectName('edit')
        confirmPassword_edit.setObjectName('edit')
        enter_btn.setObjectName('btn')
        enter_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        correct_mail_lbl.setObjectName('correct')
        correct_nik_lbl.setObjectName('correct')
        correct_psw_lbl.setObjectName('correct')
        correct_confirmPsw_lbl.setObjectName('correct')
        #layout
        vbox.addWidget(title_lbl)
        vbox.addWidget(mail_lbl)
        vbox.addWidget(mail_edit)
        vbox.addWidget(correct_mail_lbl)
        vbox.addWidget(nik_lbl)
        vbox.addWidget(nik_edit)
        vbox.addWidget(correct_nik_lbl)
        vbox.addWidget(password_lbl)
        vbox.addWidget(password_edit)
        vbox.addWidget(correct_psw_lbl)
        vbox.addWidget(confirmPassword_lbl)
        vbox.addWidget(confirmPassword_edit)
        vbox.addWidget(correct_confirmPsw_lbl)
        vbox.addWidget(enter_btn)
        self.setLayout(vbox)
        self.setStyleSheet(style)

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #настройки окна
        self.setWindowTitle("Post")
        vbox = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 350)
        #компоненты
        title_lbl = QtWidgets.QLabel("<center>Войдите</center>")
        login_lbl = QtWidgets.QLabel("<center>Введите почту:</center>")
        login_edit = QtWidgets.QLineEdit()
        password_lbl = QtWidgets.QLabel("<center>Введите пароль:</center>")
        correct_lbl = QtWidgets.QLabel("<center>Неверно</center>")
        password_edit = QtWidgets.QLineEdit()
        password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        enter_btn = QtWidgets.QPushButton("Войти")
        #стили
        title_lbl.setObjectName('title_lbl')
        login_lbl.setObjectName('subtitle_lbl')
        password_lbl.setObjectName('subtitle_lbl')
        login_edit.setObjectName('edit')
        password_edit.setObjectName('edit')
        correct_lbl.setObjectName('correct')
        enter_btn.setObjectName('btn')
        enter_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        #layout
        vbox.addWidget(title_lbl)
        vbox.addWidget(login_lbl)
        vbox.addWidget(login_edit)
        vbox.addWidget(password_lbl)
        vbox.addWidget(password_edit)
        vbox.addWidget(correct_lbl)
        vbox.addWidget(enter_btn)
        self.setLayout(vbox)
        self.setStyleSheet(style)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = RegistrationWindow()
    login.show()
    app.exec()