import os,sys

class ListDir():
    def __init__(self):
        #如果没指定路径使用当前路径
        self.file_path = []
        self.bash_path = "C:\\Users\\zpc\\Desktop\\advanced"
        self.path1 = [self.bash_path]
        self.target_path = "D:\\my-project\\advanced"

    def getListDir(self, dir):
        return os.listdir(dir)  # 获取目标路径下面所有的文件和文件夹

    def isDirAndFile(self, listdirs, pdir):
        for i in listdirs:
            tpath = pdir + '\\' + i
            if os.path.isfile(tpath):
                self.file_path.append(tpath.split(self.bash_path)[-1])  # 如果是文件的话记录文件当前位置
            elif os.path.isdir(tpath):
                self.path1.append(tpath)

    def main(self):
        temp_path = self.path1.pop()
        while temp_path:
            file_and_dir = self.getListDir(temp_path)
            self.isDirAndFile(file_and_dir, temp_path)
            temp_path = self.path1.pop() if len(self.path1) > 0 else False  # 循环拿取所有路径
        for i in self.file_path:
            print (i)

if __name__ == '__main__':
    l = ListDir()
    l.main()
