import sys, xlrd
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QGridLayout, QPushButton, QInputDialog, QLineEdit, QDialog, QScrollArea
from selenium import webdriver

class ZSelenium():
    def __init__(self, username, passwords, phones, emails, storenames, addressDetails):
        driver = webdriver.Chrome()
        driver.get("http://beta12.pospal.cn/account/register")

        shop_name = driver.find_element_by_id('username')
        shop_name.send_keys(username)

        password = driver.find_element_by_id('password')
        password.send_keys(passwords)

        passwordRepeat = driver.find_element_by_id('passwordRepeat')
        passwordRepeat.send_keys(passwords)

        phone = driver.find_element_by_id('phone')
        phone.send_keys(phones)

        email = driver.find_element_by_id('email')
        email.send_keys(emails)

        storename = driver.find_element_by_id('storename')
        storename.send_keys(storenames)

        addressDetail = driver.find_element_by_id('addressDetail')
        addressDetail.send_keys(addressDetails)

class MsgWindow(QWidget):
    def __init__(self, zexcel):
        super(MsgWindow, self).__init__()

        self.resize(1024, 600)
        self.setWindowTitle('批量注册银豹账号')

        self.datas = zexcel.main()
        self.main()

    def main(self):
        self.mainlayout = QGridLayout()

        self.content = QWidget()
        self.content.resize(1024, 600)

        self.wlayout = QGridLayout()
        self.content.setLayout(self.wlayout)

        scroll = QScrollArea()
        scroll.setWidget(self.content)
        scroll.setAutoFillBackground(True)
        scroll.setWidgetResizable(True)

        self.mainlayout.addWidget(scroll)

        shopname = QLabel('店铺名称')
        phone = QLabel('手机号')
        username = QLabel('账号')
        password = QLabel('密码')
        email = QLabel('邮箱')
        address = QLabel('地址')
        action = QLabel('操作')

        self.wlayout.addWidget(shopname, 0, 1)
        self.wlayout.addWidget(phone, 0, 2)
        self.wlayout.addWidget(username, 0, 3)
        self.wlayout.addWidget(password, 0, 4)
        self.wlayout.addWidget(email, 0, 5)
        self.wlayout.addWidget(address, 0, 6)
        self.wlayout.addWidget(action, 0, 7)

        self.setLayout(self.mainlayout)

        i = 1
        tbutton = {}
        for data in self.datas:
            tshopname = QLabel(data['shopname'])
            tphone = QLabel(data['phone'])
            tusername = QLabel(data['username'])
            tpassword = QLabel(data['password'])
            temail = QLabel(data['email'])
            taddress = QLabel(data['address'])
            tbutton[i] = QPushButton('填充')
            tbutton[i].clicked.connect(lambda: self.register({
                'username': data['username'],
                'password': data['password'],
                'phone': data['phone'],
                'email': data['email'],
                'shopname': data['shopname'],
                'address': data['address'],
            }))

            self.wlayout.addWidget(tshopname, i, 1)
            self.wlayout.addWidget(tphone, i, 2)
            self.wlayout.addWidget(tusername, i, 3)
            self.wlayout.addWidget(tpassword, i, 4)
            self.wlayout.addWidget(temail, i, 5)
            self.wlayout.addWidget(taddress, i, 6)
            self.wlayout.addWidget(tbutton[i], i, 7)

            i = i + 1

    def register(self, a):
        ZSelenium(a['username'], a['password'], a['phone'], a['email'], a['shopname'], a['address'])

class ZExcel():
    def __init__(self, filepath, sheet, username, password, shopname, address, email, phone):
        self.filepath = filepath
        self.sheet = sheet
        self.username = int(username)
        self.password = int(password)
        self.shopname = int(shopname)
        self.address = int(address)
        self.email = email
        self.phone = phone

        self.datas = []

    def main(self):
        data = xlrd.open_workbook(self.filepath)
        table = data.sheet_by_name(self.sheet)

        nrows = table.nrows
        for i in range(nrows):
            row_data = table.row_values(i)
            temp_data_ex = {
                'username' : row_data[self.username],
                'password': row_data[self.password],
                'phone' : self.phone,
                'email' : self.email,
                'shopname': row_data[self.shopname],
                'address' : row_data[self.address],
            }
            self.datas.append(temp_data_ex)
        return self.datas


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        
        self.resize(500, 600)
        self.setWindowTitle('批量注册银豹账号')

        self.main()

    def main(self):
        #初始化页面布局

        excel_button = QPushButton("选择excel文件")
        excel_button.clicked.connect(self.select_excel_button)

        sheet_name = QPushButton("输入工作表")
        sheet_name.clicked.connect(self.select_sheet_name)

        username = QPushButton("输入账号列数")
        username.clicked.connect(self.select_username)

        password = QPushButton("输入密码列数")
        password.clicked.connect(self.select_password)

        shopname = QPushButton("输入店铺名称列数")
        shopname.clicked.connect(self.select_shopname)

        address = QPushButton("输入店铺地址列数")
        address.clicked.connect(self.select_address)

        email = QPushButton('请输入邮箱')
        email.clicked.connect(self.select_email)

        phone = QPushButton('请输入手机号')
        phone.clicked.connect(self.select_phone)


        self.excel_label = QLabel()
        self.sheet_name_label = QLabel()
        self.username_label = QLabel()
        self.password_label = QLabel()
        self.shopname_label = QLabel()
        self.address_label = QLabel()
        self.email_label = QLabel()
        self.phone_label = QLabel()

        self.mainlayout = QGridLayout()

        self.mainlayout.addWidget(excel_button, 0 , 1)
        self.mainlayout.addWidget(sheet_name, 1, 1)
        self.mainlayout.addWidget(username, 2, 1)
        self.mainlayout.addWidget(password, 3, 1)
        self.mainlayout.addWidget(shopname, 4, 1)
        self.mainlayout.addWidget(address, 5, 1)
        self.mainlayout.addWidget(email, 6, 1)
        self.mainlayout.addWidget(phone, 7, 1)

        self.mainlayout.addWidget(self.excel_label, 0, 2)
        self.mainlayout.addWidget(self.sheet_name_label, 1, 2)
        self.mainlayout.addWidget(self.username_label, 2, 2)
        self.mainlayout.addWidget(self.password_label, 3, 2)
        self.mainlayout.addWidget(self.shopname_label, 4, 2)
        self.mainlayout.addWidget(self.address_label, 5, 2)
        self.mainlayout.addWidget(self.email_label, 6, 2)
        self.mainlayout.addWidget(self.phone_label, 7, 2)

        #开始按钮
        start_go = QPushButton('开始执行')
        start_go.clicked.connect(self.start_go_c)

        self.mainlayout.addWidget(start_go, 8,2)

        self.setLayout(self.mainlayout)

    def start_go_c(self):
        zexcel = ZExcel(self.filename_value, self.sheet_value, self.username_value, self.password_value, self.shopname_value, self.address_value, self.email_value, self.phone_value)

        self.msg = MsgWindow(zexcel)
        self.msg.show()

    def select_address(self):
        name, ok = QInputDialog.getText(self, "手机号", "输入手机号:", QLineEdit.Normal, self.address_label.text())
        self.address_value = name
        if ok and (len(name) != 0):
            self.address_label.setText(name)

    def select_shopname(self):
        name, ok = QInputDialog.getText(self, "手机号", "输入手机号:", QLineEdit.Normal, self.shopname_label.text())
        self.shopname_value = name
        if ok and (len(name) != 0):
            self.shopname_label.setText(name)

    def select_phone(self):
        name, ok = QInputDialog.getText(self, "手机号", "输入手机号:", QLineEdit.Normal, self.phone_label.text())
        self.phone_value = name
        if ok and (len(name) != 0):
            self.phone_label.setText(name)

    def select_email(self):
        name, ok = QInputDialog.getText(self, "邮箱名称", "输入邮箱名称:", QLineEdit.Normal, self.email_label.text())
        self.email_value = name
        if ok and (len(name) != 0):
            self.email_label.setText(name)

    def select_sheet_name(self):
        name, ok = QInputDialog.getText(self, "工作表名称", "输入工作表名称:", QLineEdit.Normal, self.sheet_name_label.text())
        self.sheet_value = name
        if ok and (len(name) != 0):
            self.sheet_name_label.setText(name)

    def select_username(self):
        name, ok = QInputDialog.getText(self, "账号列数", "输入账号列数（从0开始）:", QLineEdit.Normal, self.username_label.text())
        self.username_value = name
        if ok and (len(name) != 0):
            self.username_label.setText(name)

    def select_password(self):
        name, ok = QInputDialog.getText(self, "密码列数", "输入密码列数（从0开始）:", QLineEdit.Normal, self.password_label.text())
        self.password_value = name
        if ok and (len(name) != 0):
            self.password_label.setText(name)

    def select_excel_button(self):
        # 设置文件扩展名过滤,注意用双分号间隔
        fileName1, filetype = QFileDialog.getOpenFileName(self,"选取文件","C:/","All Files (*);;Text Files (*.txt)")
        self.filename_value = fileName1
        self.excel_label.setText(fileName1)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())

    # w = QWidget()
    # w.resize(800, 600)
    # w.move(300, 150)
    # w.setWindowTitle('批量注册银豹账号')
    # w.show()

    # sys.exit(app.exec_())
