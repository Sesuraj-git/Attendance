from PyQt5 import QtCore, QtGui, QtWidgets

global updated_names
global name_id
global file
file = open('freequent.txt', 'w')


class Ui_Dialog(object):
    def setupUi(self, Dialog, name):
        # print(name)
        self.name = name
        self.Dialog = Dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(501, 299)
        self.Dialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Dialog.setAcceptDrops(False)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(236, 80, 211, 20))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("!!!! leave blank to ignore")
        self.label.setStyleSheet("color: red")
        self.label.show()

        self.inputBox = QtWidgets.QLineEdit(Dialog)
        self.inputBox.setGeometry(QtCore.QRect(260, 110, 161, 31))
        self.inputBox.setMaxLength(6)
        self.inputBox.setClearButtonEnabled(False)
        self.inputBox.setObjectName("inputBox")

        self.nameLabel = QtWidgets.QLabel(Dialog)
        self.nameLabel.setGeometry(QtCore.QRect(20, 115, 221, 20))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.nameLabel.setFont(font)
        txt = self.name + ' :'
        self.nameLabel.setText(txt)

        self.nameLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName("nameLabel")

        self.nextButton = QtWidgets.QPushButton(Dialog)
        self.nextButton.setGeometry(QtCore.QRect(370, 160, 89, 25))
        self.nextButton.setObjectName("nextButton")

        self.headLabel = QtWidgets.QLabel(Dialog)
        self.headLabel.setGeometry(QtCore.QRect(60, 90, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setBold(True)
        font.setWeight(75)
        self.headLabel.setFont(font)
        self.headLabel.setObjectName("headLabel")

        self.prevButton = QtWidgets.QPushButton(Dialog)
        self.prevButton.setGeometry(QtCore.QRect(110, 160, 89, 25))
        self.prevButton.setObjectName("prevButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.nextButton.clicked.connect(self.next_clicked)
        self.prevButton.clicked.connect(self.prev_clicked)

    def next_clicked(self):
        self.roll_number = self.inputBox.text()
        # print(self.roll_number)
        rr = [self.roll_number, self.name]
        global  file
        file.writelines(rr)
        global updated_names
        updated_names.append(rr)
        self.Dialog.close()

    def prev_clicked(self):
        global name_id
        if name_id <= 0:
            pass
        else:
            name_id = name_id - 2
            self.Dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.inputBox.setPlaceholderText(_translate("Dialog", "EG: B19286"))
        self.nextButton.setText(_translate("Dialog", "Next"))
        self.headLabel.setText(_translate("Dialog", "Enter Roll Number For"))
        self.prevButton.setText(_translate("Dialog", "Prev"))


def show_dialog(names_to_update):
    global updated_names
    global file
    file = open('freequent.txt', 'w+')
    updated_names = []
    print(names_to_update)
    global name_id
    name_id = 0
    while True:

        if name_id == len(names_to_update):
            break
        else:
            dialog = QtWidgets.QDialog()
            dialog.ui = Ui_Dialog()
            dialog.ui.setupUi(dialog, names_to_update[name_id])
            dialog.exec_()
            name_id = name_id + 1
        # dialog.show()
    # print(updated_names)
    return updated_names
