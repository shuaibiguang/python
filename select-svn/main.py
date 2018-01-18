# _*_ coding:utf-8 _*_
import os
import sys
import shutil
import subprocess
import xml.dom.minidom
from threading import Timer
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QMainWindow, QAction, QFileDialog, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
#配置


class C():
    #svn文件配置
    svn_path = "D:\\my-project\\advanced"
    svn_base_path = "D:\\my-project\\"
    copy_file_path = "C:\\Users\\zpc\\Desktop"
    update = "svn update %s" % svn_path
    username = "zhengpengcheng"
    log = "svn log %s -l 1 --search %s -v --xml" % (svn_path, username)
    xml_file_name = "log.xml"
    clean = "svn cleanup %s" % svn_path
    is_run = True
    #配置文件不存在的话 初始化程序
    # def __init__(self):
    #     self.testExistsConfig()

    # def testExistsConfig(self):
    #     if not os.path.exists(os.getcwd() + '\\' + 'jconfig.txt'):
    #         self.initapp = InitApp()

#初始化程序
# class InitApp():
#     def __init__(self):
#         app = QApplication(sys.argv)

#         self.mywin = QWidget()
#         self.mywin.resize(350, 400)
#         self.mywin.setWindowTitle('配置参数')
#         self.mywin.setWindowIcon(QIcon('favicon.ico'))

#         #添加按钮
#         svn_path_btn = QPushButton('项目目录路径')
#         svn_path_btn.clicked.connect(self.select_svn_path)
#         desktop_path_btn = QPushButton('桌面路径')
#         desktop_path_btn.clicked.connect(self.select_desktop_path)
#         username_btn = QPushButton('用户名')
#         username_btn.clicked.connect(self.select_username)

#         self.svn_path_label = QLabel()
#         self.desktop_path_label = QLabel()
#         self.username_label = QLabel()

#         self.mainlayout = QGridLayout()

#         self.mainlayout.addWidget(svn_path_btn, 0, 2)
#         self.mainlayout.addWidget(desktop_path_btn, 1, 2)
#         self.mainlayout.addWidget(username_btn, 2, 2)

#         self.mainlayout.addWidget(self.svn_path_label, 0, 1)
#         self.mainlayout.addWidget(self.desktop_path_label, 1, 1)
#         self.mainlayout.addWidget(self.username_label, 2, 1)

#         self.mywin.setLayout(self.mainlayout)

#         self.mywin.show()
#         sys.exit(app.exec_())

#     def select_username(self):
#         name, ok = QInputDialog.getText(self.mywin, "用户名", "请输入用户名:", QLineEdit.Normal, self.username_label.text())
#         self.username = name
#         if ok and (len(name) != 0):
#             self.username_label.setText(name)

#     def select_desktop_path(self):
#         directory = QFileDialog.getExistingDirectory(self.mywin, "选取svn项目目录", "C:/")
#         self.copy_file_path = directory
#         self.desktop_path_label.setText(directory)

#     def select_svn_path(self):
#         directory = QFileDialog.getExistingDirectory(self.mywin, "选取svn项目目录", "C:/")
#         self.svn_path = directory
#         self.svn_base_path = "/".join(directory.split('/')[:-1])
#         self.svn_path_label.setText(directory)

#ftp 相关操作
class F():
    pass

#窗口提示
class WinQt(QWidget):
    def __init__(self, massage):
        super(WinQt, self).__init__()

        self.resize(500, 120)
        self.setWindowTitle('检测到同步')
        self.setWindowIcon(QIcon('favicon.ico'))

        self.createWin(massage)

    def createWin(self, massage):

        upload = QPushButton("上传")
        upload.clicked.connect(self.close)

        cancel = QPushButton("取消")
        cancel.clicked.connect(self.close)

        lmassage = QLabel(massage)

        mainlayout = QGridLayout()

        mainlayout.addWidget(lmassage, 0, 1, 2, 2)

        mainlayout.addWidget(upload, 1, 1)
        mainlayout.addWidget(cancel, 1, 2)

        self.setLayout(mainlayout)

        self.show()
#svn类
class S():
    def __init__(self):
        self.c = C()

    def main(self):
        result = self.getInfo()
        self.copy_commit_file(result['file_paths'])
        try:
            self.w = WinQt(result['massage'])
        except:
            pass

    #如果检测到有更新， 则将更新文件 下载到本地
    def copy_commit_file(self, files):
        #首先删除桌面文件夹
        # shutil.rmtree(self.copy_file_path + "\\advanced")
        os.system('rd /S /Q %s'% self.c.copy_file_path + "\\advanced")
        for path in files:
            if not os.path.exists( self.c.copy_file_path + "/".join(path.split('/')[:-1])):
                os.makedirs(self.c.copy_file_path + "/".join(path.split('/')[:-1]))

            if len(path.split('.')) > 1:
                #将文件拷贝进来
                shutil.copyfile(self.c.svn_base_path + path, self.c.copy_file_path + path)

        #激活窗口提示是否上传ftp
    #清楚svn锁
    def cleanup(self):
        os.system(self.c.clean)

    def getInfo(self):
        os.system(self.c.update)
        out_bytes = subprocess.check_output(self.c.log)
        out_text = out_bytes.decode('utf-8')
        with open(self.c.xml_file_name, 'w', encoding='utf-8') as f:
            f.write(out_text)

        return self.xml()

    #解析xml
    def xml(self):
        dom = xml.dom.minidom.parse(self.c.xml_file_name)
        root = dom.documentElement

        #拿取版本号
        revision_node = root.getElementsByTagName('logentry')[0]
        revision = revision_node.getAttribute('revision')
        #拿取文件路径
        file_paths_node = root.getElementsByTagName('path')
        file_paths = [f.firstChild.data for f in file_paths_node]

        #拿取更新消息
        massage_node = root.getElementsByTagName('msg')[0]
        massage = massage_node.firstChild.data

        return {'revision': revision, 'file_paths': file_paths, 'massage': massage}

#主体类
class M():
    def __init__(self):
        self.c = C()
        if (self.c.is_run):
            self.s = S()
            self.myWin()

    def myWin(self):
        app = QApplication(sys.argv)

        myshow = QMainWindow()
        myshow.resize(1024, 576)

        myshow.setWindowIcon(QIcon('favicon.ico'))

        myshow.setWindowTitle('代码发布')

        myshow.setStyleSheet("background-image:url(background2.jpg)")
        
        #开启状态栏 和 菜单栏
        myshow.statusBar()

        #退出
        exitAction = QAction('退出程序')
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出程序')
        exitAction.triggered.connect(myshow.close)

        #检测更新
        updateAction = QAction('检测更新')
        updateAction.setShortcut('Ctrl+U')
        updateAction.setStatusTip('检测更新 : 在桌面生成发布文件夹')
        updateAction.triggered.connect(self.testUpdate)

        menubar = myshow.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(exitAction)

        release = menubar.addMenu('&发布')
        release.addAction(updateAction)

        myshow.show()

        sys.exit(app.exec_())

    def testUpdate(self):
        self.s.main()



if __name__ == '__main__':
    m = M()
