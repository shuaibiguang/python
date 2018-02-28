import pandas as pd
import pymysql.cursors
import os

connection = pymysql.connect(
    host='rdsk6401719a03wwb811o.mysql.rds.aliyuncs.com',
    user='dbuser_bpt40',
    password='Bk+P8KGud^y2h)5B',
    db='bpt40',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
"""
dispatchid = 614

with connection.cursor() as cursor:
    sql = "select dispatchname from bpy_ewei_shop_dispatch where id = %d" % (dispatchid)
    cursor.execute(sql)
    result = cursor.fetchone()
    print (result)
"""

class Handle():
    def __init__(self, filename):
        try:
            self.df = pd.read_csv(filename)
        except:
            self.df = pd.read_csv(filename, encoding="gbk")

        self.filename = filename
        #商品名称
        self.title = self.df['title']
        #拿取配送方式
        self.dispatchid = self.df['dispatchid']
        #拿取商品代码
        self.goodssn = self.df['goodssn']
        #sku
        self.productsn = self.df['productsn']
        #豹品淘的sku
        self.sn = ['AB.0001','AB.0008','AB.0009','AB.0005','AB.0012','AB.0007','LEO.1008','LEO.1009','SFO.0001','SFO.0002','SFO.0003','SFO.0004','SFO.0005','TL.1004','FR.L5402','FR.L5400','FR.L5500','FR.L5501','WM.0005','WM.0001','WM.0002','WM.0003','WM.0004','WM.0006','WM.0007','WM.0008','WM.0009','WM.0010','LD.0010','LD.0012','LD.0009','LD.0011','LD.0003','LD.0004','LD.0001','LD.0002','LD.0006','LD.0005','LD.0008','LD.0007','KR.0004','KR.0005','KR.0002','NP.0004','NP.0005','ST.Q2002','ST.1606','ST.1117','ST.1615','TL.2002','TL.1002','TL.2003','TL.1003','TL.1001','TL.1006','TL.1005','TL.2001','RQ.0004','RQ.0003','RQ.1205','RQ.1203','RQ.0008','ST.Q2001','ST.Q2007','ST.Q2016','ST.Q2006','ST.Q2017','ST.Q2004','ST.Q2018','HK.1001','HK.1002','FC.1001','RQ.1301','RQ.1302','RQ.1303','FC.1002','FC.1003','FC.1004','FC.1005','FC.1006','FC.1007','FC.1008','FC.1009','FC.1010','FC.1017','HB.1011','HB.1003','HB.1005','HB.1009','HB.1010','AS.1001','AS.1002','AS.1003','AS.1004','AS.1005','AS.1006','AS.1007','AS.1008','AS.1009','AS.1010','AS.1011','AB.0002','ST.1130','ST.1614','TM.1004','TM.1010','TM.1009','TM.1001','TM.1002','TM.1003','MIS.1012','MIS.1013','MIS.1011','MIS.1006','MIS.1005','MIS.1009','MIS.1004','MIS.1003','MIS.1010','MIS.1014','CT.2610','CT.2613','CT.2810','CT.2811','LEO.1001','LEO.1002','LEO.1006','LEO.1007','LEO.1005','LEO.1010','LEO.1011','LEO.1012','LEO.1014','LEO.1015','LEO.1016','JJ.0003','JJ.0006','JJ.0004','JJ.0002','AP.2007','SB.1056','CB.1044','SB.1050','CB.1036','CB.1003','CB.1004','CB.1017','CB.1024','CT.2910','CT.2911','BS.1004','BS.1005','BS.1020','BS.1016','BS.1007','BS.1014','ST.1514','ST.1515','ST.1516','ST.1001','ST.1004','ST.1612','ST.1003','MIS.1008','ST.1108','ST.1131','ST.1411','ST.1502','ST.1506','ST.1512','ST.1602','ST.1603','ST.1604','ST.1605','ST.1609','ST.1610','KR.0001','KR.0006','ST.1112','ST.1118','ST.1501','ST.1513','ABC.0001','ABC.0002','CF.1001','CF.1002','CF.1007','CF.1008','CF.1010','FC.1016','LN.1023','BB.0002','JJ.0001','JJ.0007','BB.0001','DSL.0002','TY.1001','TY.1002','TY.1003','TY.1005','TY.1006','COC.0005','COC.0006','EV.1003','DSL.0001','HB.1008','MR.1005','FH.SWI.9311770596732','PD.1001','PD.1003','PD.1004','EO.1010','EO.1011','EO.1013','EO.1014','EO.1015','EO.1018','EV.1002','FS.1003','QIH.0001','YZ.1002','YZ.1003','PS.1001','PS.1002','MH.1001','MH.1006','WH.1001','JD.1004','RQ.0005','QIH.0004','ZHMR.0003','CB.1007','CB.1008','SN.0001','CTP.0001','EM.1001','BK.1001','BK.1002','BK.1009','BK.1005','BK.1006','BK.1007','XF.1001','XF.1003','XF.1005','NX.1001','NX.1002','NX.1003','NX.1004','NX.1005','NX.1007','NX.1008','NX.1009','NZ.1001','NZ.1002','NZ.1003','GY.1002','GY.1003','GY.1004','NRK.1001','NRK.1002','NRK.1004','NRK.1003','MS.1004','MS.1002','MS.1003','MS.1001','MS.1005','MS.1006','RE.1001','AE.1001','BUY.1002','BUY.1001','SN.0003','SN.0005','SN.0007','XB.1001','XB.1002','WH.1002','FS.1001','FS.1002','AT.1001','CTP.0011','AT.1002','ST.P1117','ST.P1112','LEO.1004','SUV.0002','COP.0004','SUV.0001','AP.0006','AP.2006','AP.1006','AP.1000','AP.0002','AP.2002','AP.1002','AP.0003','AP.2003','AP.1003','AP.0001','AP.2001','AP.1001','AP.0005','AP.2005','AP.0004','AP.2004','AP.1004','AP.2009','TY.1009','TY.1010','TY.1008','TY.1011','TY.1012','TY.1007','MIS.1002','MIS.1001','FC.1014','FC.1011','MR.0001','MR.0002','MI.1002','MI.1001','MI.1004','MI.1003','BU.1001','RQ.0018','RQ.0014','RQ.1208','RQ.1209','RQ.1210','RQ.1211','RQ.0010','RQ.1201','RQ.1202','RQ.0009','RQ.2109','RQ.2110','RQ.2111','RQ.2108','RQ.2101','RQ.0017','RQ.0015','RQ.0016','RQ.1204','RQ.0012','RQ.0006','FB.5504','FB.5518','FB.5519','FB.5521','FB.5520','FB.5522','FB.5517','FR.L5403','FR.L5405','FR.L5404','FR.L5401','ST.1601','ST.1616','ST.1410','ST.1608','ST.1121','ST.1618','ST.Q2023','TY.1004','CB.1016','CB.1028','CB.1030','CB.1033','CB.1021','CB.1015','CB.1027','CB.1025','CB.1009','CB.1010','CB.1011','CB.1026','CB.1014','CB.1018','CB.1020','CB.1002','CB.1047','CB.1046','SB.1035','CB.1040','CB.1012','CB.1023','CB.1029','CB.1001','CB.1022','CB.1006','CB.1005','TN.1007','TN.1006','TN.1003','TN.1002','TN.1001','TN.1005','TN.1004','SKF.1008','SKF.1007','SKF.1003','SKF.1002','SKF.1001','SKF.1005','SKF.1004','SKF.1010','SKF.1009','TM.1008','TM.1007','TM.1006','TM.1005','GY.1001','GY.1005','GY.1008','GY.1007','GY.1006','HB.1004','HB.1006','BOS.1004','BOS.1003','BOS.1020','BOS.1019','BOS.1018','BOS.1002','BOS.1001','BOS.1007','BOS.1006','BOS.1017','BOS.1016','BOS.1015','BOS.1014','BOS.1013','BOS.1012','BOS.1011','BOS.1010','BOS.1009','BOS.1008','BY.1001','OA.1008','OA.1007','OA.1006','OA.1005','OA.1004','OA.1003','OA.1002','OA.1001','QIH.0003','QIH.0002','AB.0010','AB.0003','ST.1611','CF.1004','CF.1005','CF.1006','CF.1003','CF.1011','CF.1009','BY.1002','LEO.1003','LEO.1013','CT.2711','CT.2710','AP.2008','TH.1017','TH.1018','RQ.0013','AB.0006','AB.0013','AB.0014','AB.0015','AB.0016','AB.0017','AB.0018','RQ.1207','ZHAB.0003','ZHTL.001','AK.1002','AK.1004','AK.1005','HR.1001','LN.1012','BN.1001','BN.1002','BN.1004','BO.1001','BO.1005','IM.1006','EC.1001','PK.1001','SD.1004','SD.1006','YH.1008','YH.1009','YH.1010','YH.1011','LN.1007','LN.1008','LN.1009','EI.1001','EI.1002','EI.1007','LC.1005','LC.1006','LC.1007','NU.1003','TH.1002','NU.1001','TH.1012','WQ.1002','FMS.1001','FMS.1002','PM.1001','PM.1002','PM.1004','MS.1009','DE.1002','DE.1004','DE.1005','DE.1001','VT.1007','ES.1002','ES.1004','ES.1006','FH.0001','BP.0001','BP.0002','BP.0003','BP.0004','BP.0005','BP.0006','BP.0007','BP.0008','BP.0009','GD.0001','GD.0002','GD.0003','STM.0001','STM.0002','AK.1001','AK.1010','BO.1003','EI.1009','LC.1003','MS.1011','SD.0027','DE.1006','OK.1001','ES.1001','ES.1005','ES.1007','ES.1008','ST.1623','ZHTL.0005','ZHTL.0006','ZHTL.0007','ZHTL.0008','ZHTL.0009','ST.Q2015','ST.Q2017','ST.Q2016','ST.Q2001','ST.Q2018',]

    def handle1(self):
        dispatchid = self.dispatchid
        with connection.cursor() as cursor:
            for k,v in dispatchid.items():
                if v > 0:
                    #搜索快递名称
                    sql = "select dispatchname from bpy_ewei_shop_dispatch where id = %d" % (v)
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    print(str(k) + '--' + result['dispatchname'])
                    dispatchid[k] = result['dispatchname'] + str(v)
        self.df['dispatchid'] = dispatchid
        return self.df

    def handle2(self):
        for k,v in self.dispatchid.items():
            try:
                patchid = round(float(v))
            except:
                continue
            if patchid == 0:
                goodssn = self.goodssn[k]
                if goodssn in self.sn:
                    print ("%s中：%s商品查找到，sn：%s"%(self.filename, self.title[k], goodssn))
                    self.dispatchid[k] = 9999
        self.df['dispatchid'] = self.dispatchid
        return self.df



if __name__ == '__main__':
    # h = Handle('1.csv')
    # df = h.handle1()

    # df.to_csv('./one.csv')

    for filename in os.listdir('./一次处理'):
        h = Handle('./一次处理/'+filename)
        df = h.handle2()
        df.to_csv('./二次处理/'+filename+'.csv', encoding='gbk')


