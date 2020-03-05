#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QHBoxLayout,QVBoxLayout,QLineEdit,QAction,QLabel,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import socket
from PyQt5.QtWidgets import QListWidget
import icon
class Ui(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):
        #self.setGeometry(300,300,400,300)
        #self.resize(400,300)
        self.setFixedSize(400,300)
        self.setWindowTitle('远程唤醒')
        self.setWindowIcon(QIcon(':/wor.ico'))
        #self.setStyleSheet('QWidget{background-color:aqua}')


        bt1 = QPushButton('唤醒',self)
        bt2 = QPushButton('保存', self)

        self.lst = QListWidget(self)


        try:
            f=open('info','r')
            for i in f:
                #print(i[:-1])
                self.lst.addItem(i[:-1])
        except:
            pass

        self.lst.itemDoubleClicked.connect(self.Wake)

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(bt1)
        hbox.addWidget(bt2)
        hbox.addWidget(self.lst)

        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)



        #action=QAction(self)
        #action.triggered.connect()
        #self.line.addAction(action,QLineEdit.TrailingPosition)
        self.lb1 = QLabel('IP地址/域名',self)
        self.lb2 = QLabel('MAC地址',self)
        self.lb3 = QLabel('端口号',self)
        self.line1=QLineEdit(self)
        self.line2=QLineEdit(self)
        self.line3=QLineEdit(self)

        self.line1.resize(150, 30)
        self.line2.resize(140, 30)
        self.line3.resize(50, 30)
        self.line1.move(100,20)

        #self.line1.setAlignment()
        self.lb1.move(20,20)
        self.line2.move(100,60)
        self.lb2.move(20,60)
        self.line3.move(100,100)
        self.lb3.move(20,100)

        #line.editingFinished.connect(self.Action)
        self.line2.setInputMask('>HH:HH:HH:HH:HH:HH;_')

        bt1.clicked.connect(self.Action)
        bt2.clicked.connect(self.Save)
        self.show()

    def Action(self):
        if len(self.line1.text())!=0 :
            if len(self.line2.text())==17:
                if len(self.line3.text())!=0:
                    context = self.line1.text() + " " + self.line2.text() + " " + self.line3.text() + "\n"
                    try:
                        f = open('info', 'r+')
                        if context not in f.readlines():
                            f.write(context)
                    except:
                        f = open('info', 'a')
                        f.write(context)
                        pass
                    f.close()
                    mac="".join(self.line2.text().split(":"))
                    data=b"\xFF\xFF\xFF\xFF\xFF\xFF"+bytes().fromhex(mac)*16
                    #print(self.line1.text())
                    #print(self.line2.text())
                    #print(self.line3.text())
                    #print(data,len(data))
                    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                    s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
                    try:
                        s.sendto(data,(self.line1.text(),int(self.line3.text())))
                        QMessageBox.information(self, '成功', '已唤醒!')
                    except:
                        QMessageBox.information(self, '失败', '请检查IP地址或域名！')
                    s.close()
                else:
                    QMessageBox.information(self, '失败', '请填写端口！')
            else:
                QMessageBox.information(self, '失败', 'MAC填写有误！')
        else:
            QMessageBox.information(self, '失败', '请填写IP或域名！')

        self.lst.clear()

        try:
            f = open('info', 'r')
            for i in f:
                self.lst.addItem(i[:-1])
            f.close()
        except:
            pass

    def Save(self):
        f=open('info','a')
        f.write(self.line1.text()+" "+self.line2.text()+" "+self.line3.text()+"\n")
        f.close()
        QMessageBox.information(self, '成功', '已保存!')

    def Wake(self,item):
        info=item.text().split(' ')
        mac="".join(info[1].split(':'))
        data = b"\xFF\xFF\xFF\xFF\xFF\xFF" + bytes().fromhex(mac) * 16
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
        try:
            s.sendto(data,(info[0],int(info[2])))
            QMessageBox.information(self, '成功', '已唤醒!')
        except:
            QMessageBox.information(self, '失败', '请检查IP地址或域名！')
        s.close()



if __name__=='__main__':
    app=QApplication(sys.argv)
    ui=Ui()

    app.exit(app.exec_())
