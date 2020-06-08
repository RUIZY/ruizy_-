from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(931, 665)
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(15, 50, 261, 601))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(240, 10, 32, 31))
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 40, 551, 31))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(300, 70, 611, 571))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        self.treeWidget.objectNameChanged['QString'].connect(self.label.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "HANBADA"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "AUX.BOILER"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Dialog", "BURNER"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Dialog", "INCINERATOR"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Dialog", "BURNER"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.toolButton.setText(_translate("Dialog", "..."))
        self.label.setText(_translate("Dialog", "MACHINERY NAME"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
