import sys
import sqlite3
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem, QLineEdit, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel

from PyQt5 import QtCore

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("git Капучино")
        Form.resize(400, 300)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(28, 30, 156, 23))
        self.pushButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(27, 65, 331, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 30, 156, 23))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", "Изменить фильм"))
        self.pushButton_6.setText(_translate("Form", "Добавить фильм"))
        self.pushButton_6.clicked.connect(self.clickedbutton6)
        self.pushButton_5.clicked.connect(self.clickedbutton5)
        self.tableWidget.itemSelectionChanged.connect(self.clickedbt5)
        self.connection = sqlite3.connect("coffee.sqlite")
        res = self.connection.cursor().execute('SELECT * FROM Info').fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.name = self.connection.execute('SELECT * FROM Info')
        self.names = list(map(lambda x: x[0], self.name.description))
        self.res1 = self.connection.cursor().execute('SELECT Id, [Название сорта] FROM Info').fetchall()

        self.tableWidget.setHorizontalHeaderLabels(self.names)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.connection.close()
        self.sl = {}
        for i, k in enumerate(self.res1):
            self.sl.update({k[1]: i + 1})
        
    def clickedbutton6(self):
        self.w1 = Window1(self.sl)
        self.w1.show()
        
    def clickedbt5(self):
        self.sp = []
        for it in self.tableWidget.selectedItems():
            self.sp.append([self.tableWidget.item(it.row(), x).text() for x in range(7)])
            
    def clickedbutton5(self):
        try:
            self.w2 = Window2(self.sp, self.sl)
            self.w2.show()
        except AttributeError:
            pass
        
class Window2(QWidget):
    def __init__(self, sp, sl):
        super().__init__()
        self.setWindowTitle('Изменить информацию')
        self.setGeometry(900, 400, 345, 350)
        self.sp = sp
        self.sl = sl
        for i in sp:
            sp = i
            self.sp = sp
        
        self.connection1 = sqlite3.connect("coffee.sqlite")
        self.cur = self.connection1.cursor()
        self.res2 = self.connection1.cursor().execute('SELECT Id, [Название сорта] FROM Info').fetchall()
        
        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.setText(*sp[1:2])
        self.lineEdit1.resize(200, 20)
        self.lineEdit1.move(130, 10)
        self.label = QLabel('Название сорта', self)
        self.label.resize(100, 20)
        self.label.move(20, 15)
        self.move(900, 400)
        
        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.setText(*sp[2:3])
        self.lineEdit2.resize(200, 20)
        self.lineEdit2.move(130, 60)
        self.label = QLabel('Степень обжарки', self)
        self.label.resize(100, 20)
        self.label.move(20, 65)

        self.lineEdit4 = QLineEdit(self)
        self.lineEdit4.setText(*sp[4:5])
        self.lineEdit4.resize(200, 20)
        self.lineEdit4.move(130, 110)
        self.label = QLabel('Молотый/в зернах', self)
        self.label.resize(100, 30)
        self.label.move(20, 105)
        
        self.lineEdit3 = QLineEdit(self)
        self.lineEdit3.setText(*sp[3:4])
        self.lineEdit3.resize(200, 20)
        self.lineEdit3.move(130, 160)
        self.label = QLabel('Описание вкуса', self)
        self.label.resize(100, 20)
        self.label.move(20, 160)
        
        self.lineEdit5 = QLineEdit(self)
        self.lineEdit5.setText(*sp[5:6])
        self.lineEdit5.resize(200, 20)
        self.lineEdit5.move(130, 210)
        self.label = QLabel('Цена', self)
        self.label.resize(100, 20)
        self.label.move(20, 210)
        
        self.lineEdit6 = QLineEdit(self)
        self.lineEdit6.setText(*sp[6:7])
        self.lineEdit6.resize(200, 20)
        self.lineEdit6.move(130, 260)
        self.label = QLabel('Объём упаковки', self)
        self.label.resize(100, 20)
        self.label.move(20, 260)
        
        self.pushButton = QPushButton('Изменить', self)
        self.pushButton.resize(70, 30)
        self.pushButton.move(245, 300)
        self.pushButton.clicked.connect(self.clickedbutton)
        
    def clickedbutton(self, text):
        self.id = str(*self.sp[0:1])
        self.cur.execute("UPDATE Info SET [Название сорта] = " + '"' + self.lineEdit1.text() + '"' + ', ' + 
                         '[Степень обжарки] = ' + '"' + self.lineEdit2.text() + '"' + ', '
                         '[Молотый/в зернах] = ' + '"' + self.lineEdit4.text() + '"' + ', ' 
                         'Цена = ' + '"' + self.lineEdit5.text() + '"' + ', '
                         '[Объём упаковки] = ' + '"' + self.lineEdit6.text() + '"' + ', '
                         '[Описание вкуса] = ' + '"' + self.lineEdit3.text() + '"' + " WHERE id = " + self.id)
        self.connection1.commit()
        self.connection1.close()
        self.close()
        

class Window1(QWidget):
    def __init__(self, sl):
        super(Window1, self).__init__()
        self.setWindowTitle('Добавить информацию')
        self.setGeometry(900, 400, 345, 350)
        self.sl = sl
        
        self.connection1 = sqlite3.connect("coffee.sqlite")
        self.cur = self.connection1.cursor()
        
        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.resize(200, 20)
        self.lineEdit1.move(130, 10)
        self.label = QLabel('Название сорта', self)
        self.label.resize(100, 20)
        self.label.move(20, 15)
        self.move(900, 400)
        
        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.resize(200, 20)
        self.lineEdit2.move(130, 60)
        self.label = QLabel('Степень обжарки', self)
        self.label.resize(100, 20)
        self.label.move(20, 65)

        self.lineEdit4 = QLineEdit(self)
        self.lineEdit4.resize(200, 20)
        self.lineEdit4.move(130, 110)
        self.label = QLabel('Молотый/в зернах', self)
        self.label.resize(100, 30)
        self.label.move(20, 105)
        
        self.lineEdit3 = QLineEdit(self)
        self.lineEdit3.resize(200, 20)
        self.lineEdit3.move(130, 160)
        self.label = QLabel('Описание вкуса', self)
        self.label.resize(100, 20)
        self.label.move(20, 160)
        
        self.lineEdit5 = QLineEdit(self)
        self.lineEdit5.resize(200, 20)
        self.lineEdit5.move(130, 210)
        self.label = QLabel('Цена', self)
        self.label.resize(100, 20)
        self.label.move(20, 210)
        
        self.lineEdit6 = QLineEdit(self)
        self.lineEdit6.resize(200, 20)
        self.lineEdit6.move(130, 260)
        self.label = QLabel('Объём упаковки', self)
        self.label.resize(100, 20)
        self.label.move(20, 260)
        
        self.pushButton = QPushButton('Сохранить', self)
        self.pushButton.resize(70, 30)
        self.pushButton.move(245, 300)
        self.pushButton.clicked.connect(self.clickedbutton)
    
    def clickedbutton(self, text):
        st = [self.lineEdit1.text(), self.lineEdit2.text(), self.lineEdit4.text(), self.lineEdit3.text(), self.lineEdit5.text(), self.lineEdit6.text()]
        self.cur.execute("INSERT INTO Info ([Название сорта], [Степень обжарки], [Молотый/в зернах], [Описание вкуса], Цена, [Объём упаковки]) VALUES (?, ?, ?, ?, ?, ?)", st)
        self.connection1.commit()
        self.connection1.close()
        self.close()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())