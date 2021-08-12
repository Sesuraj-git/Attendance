import sys
from PyQt5.QtGui import QImage, QPalette, QBrush
import write_to_file
from entry_widget import show_dialog
import fetch_attendance as ext
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        # MainWindow.setStyleSheet("background:#44475A")
        MainWindow.resize(730, 436)

        bg = QImage("main_bg.jpg")
        # sImage = bg.scaled(QSize(730, 436))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(bg))
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 80, 351, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: #CDB1AD")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 120, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #CDB1AD")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.on_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select a .txt File for Attendance Markup"))
        self.pushButton.setText(_translate("MainWindow", "Select File"))
        # self.label_2.setText(_translate("MainWindow", "Selected file is not a .txt file"))
        # self.pushButton_2.setText(_translate("MainWindow", "proceed"))

    def on_click(self):
        print('on click')
        self.dir_path = QFileDialog.getOpenFileName()
        print(self.dir_path)

        self.file_name = str(self.dir_path[0]).split('/')
        print(self.file_name)
        self.file_name = self.file_name[-1]
        print(self.file_name,'fn')
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 170, 351, 17))

        if self.file_name.split('.')[1] == 'txt':
            text = (self.file_name + ' is selected for attendance')
            self.label_2.setText(text)
            self.label_2.setStyleSheet("background-color: #30B309;border: 1px solid black;")
            self.label_2.show()
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setBold(True)
            font.setWeight(75)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label_2")
            self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_2.setGeometry(QtCore.QRect(310, 230, 89, 25))
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_2.setText("proceed")
            self.pushButton_2.show()
            self.pushButton_2.clicked.connect(self.butt2_click)


        else:
            self.label_2.setText("Selected file is not a .txt file")
            self.label_2.show()
            self.label_2.setStyleSheet("background-color: red;border: 1px solid black;")
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setBold(True)
            font.setWeight(75)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label_2")

    def butt2_click(self):
        self.pushButton.close()
        self.label.close()

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 230, 89, 25))
        self.pushButton_3.setObjectName("pushButton_2")
        self.pushButton_3.setText("Select")
        self.pushButton_3.show()

        self.pushButton_2.close()
        self.label_2.close()
        self.label_2.setText('Select An Output Directory')
        self.label_2.show()
        self.pushButton_3.clicked.connect(self.cl3)


    def cl3(self):

        self.out_dir_path = QFileDialog.getExistingDirectory()
        print(self.out_dir_path)
        retext = ext.ececute_file(self.dir_path)
        names_to_update = retext[0]
        per_names = retext[1]

        r_names = show_dialog(names_to_update)
        write_to_file.write_file(r_names, per_names, self.out_dir_path)
        # for name in names_to_update:
        #     ret = self.show_dialog(name)
        #     print('jdfsf', ret)

    '''def show_dialog(self, data):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form()
        dialog.ui.setupUi(dialog, data)
        dialog.exec_()
        dialog.show()'''

    # QMessageBox.about(MainWindow, "Title", "Get to Terminal for Further Works")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
