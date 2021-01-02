#
# 数据处理
#
import datetime
from StockInfoPaopao import *

# 剪切数据格式化
def informatcsv(path):
    with open(path, 'r', encoding='gbk') as f:
        text = f.readlines()
    with open(path, 'w+', encoding='gbk')as f:
        f.write(text[0])
        f.write(text[1])
        parts1 = text[1].split(',')
        for i in range(2, text.__len__() - 1):
            parts2 = text[i].split(',')
            if (parts2[7] != parts1[3]):
                n = float(parts1[3]) / float(parts2[7])
                parts2[3] = str(round(float(parts2[3]) * n, 2))
                parts2[4] = str(round(float(parts2[4]) * n, 2))
                parts2[5] = str(round(float(parts2[5]) * n, 2))
                parts2[6] = str(round(float(parts2[6]) * n, 2))
                parts2[7] = parts1[3]
                parts2[8] = str(round(float(parts2[3]) - float(parts2[7]), 2))
                t = ''
                for part in parts2[:-1]:
                    t += part + ','
                t += parts2[-1]
                text[i] = t
            f.write(text[i])
            parts1 = parts2



#输入(剪切)数据
def incsv(code ,fromdate , todate):
    #开始日期年月日
    try:
        fromDate = datetime.datetime.strptime(fromdate,'%Y-%m-%d')
        #结束日期年月日
        toDate = datetime.datetime.strptime(todate,'%Y-%m-%d')
    except ValueError:
        raise
    with open('./MyStrategy/datas/' + code + '.csv',"r",encoding="gbk") as f:
        text = f.readlines()
    with open("./MyStrategy/datas/datachoice.csv", "w+", encoding="gbk") as f:
        f.write(text[0])
        for line in text[1:]:
            #每行数据
            linels = line.split(',')
            parts = [q for q in linels if q]
            #日期
            date = parts[0]
            Date = datetime.datetime.strptime(date, '%Y-%m-%d')
            if(fromDate<=Date<=toDate):
                f.write(line)
    informatcsv("./MyStrategy/datas/datachoice.csv")



#下载数据后格式化
def downloadformatcsv(path):
    result = []
    with open(path,'r',encoding='gbk') as f:
        text = f.readlines()
    with open(path,'w+',encoding='gbk')as f:
        f.write(text[0])
        for line in text[1:]:
            parts = line.split(',')
            parts = [part for part in parts if part]
            if(parts[3]!='0.0'):
                result.append(line)
        result.reverse()
        for line in result:
            f.write(line)

#下载数据
def downloadcsv(code):
    path = "./MyStrategy/datas/"
    start = ""
    end = ""
    getCodeData(code, start, end, path)
    with open("./MyStrategy/datas/"+code+".csv", "r", encoding="gbk") as f:
        text = f.readlines()
    if text.__len__()==1:
        os.remove("./MyStrategy/datas/"+code+".csv")
        return False
    else:
        with open("./MyStrategy/datas/"+code+".csv", "r", encoding="gbk") as f:
            text = f.readlines()
            codename = text[1].split(",")[2]
        downloadformatcsv(path+code+".csv")
        with open("./MyStrategy/datas/codelist.csv", "a+", encoding="gbk") as f:
            f.write(code+" "+codename+'\n')
    return True

#更新已有股票代码数据
def updatecsv():
    with open("./MyStrategy/datas/codelist.csv", "r", encoding="gbk") as f:
        codelist = f.readlines()

    path = "./MyStrategy/datas/"
    start = ""
    end = ""
    for code in codelist[0:1]:
        os.remove(path + code[0:6] + ".csv")
        getCodeData(code[0:6], start, end, path)
        downloadformatcsv(path + code[0:6] + ".csv")
