import  xlrd
import xlwt

import time as t
from datetime import datetime,timedelta

import  json
# -*- coding:utf-8 -*-


data = xlrd.open_workbook('门店班车到达时间.xlsx')



class departEntity():

       def __init__(self,name,code):
           self.name=name
           self.code=code
           self.times = []
           self.info=''



       def addTime(self,time):
           if time:
             newTime=t.strptime(time,'%Y-%m-%d %H:%M:%S.000000')
             endTime=None;
             #基本处理分钟小于30，直接00，大于30，按照30算
             if newTime.tm_min<30:
                 newTime=datetime(newTime.tm_year,newTime.tm_mon,20,newTime.tm_hour,00)


             elif newTime.tm_min>=30:
                 newTime = datetime(newTime.tm_year, newTime.tm_mon, 20, newTime.tm_hour, 30)


           #默认+4小时,设置结束时间
           endTime = newTime + timedelta(hours=4)



           if len(self.times)==1:
               #如果存在2班车，则+2小时
               self.times[0]['end']=self.times[0]['begin']+timedelta(hours=2)
               endTime = newTime + timedelta(hours=2)
               #检测时间是否有交叉

               if self.times[0]['begin']<=newTime and self.times[0]['end']>=newTime:
                   endTime = self.times[0]['begin'] + timedelta(hours=4)
                   self.times = [{'begin': newTime, 'end': endTime}]
               elif newTime<=self.times[0]['begin'] and self.times[0]['begin']<=endTime:
                   #newTime = newTime
                   endTime = newTime + timedelta(hours=4)
                   self.times = [{'begin': newTime, 'end': endTime}]
               else:
                   if self.removal({'begin': newTime, 'end': endTime}):
                       self.times.append({'begin': newTime, 'end': endTime})



           elif len(self.times)>1:

               self.info='三班车，不处理'
               if self.removal({'begin': newTime, 'end': endTime}):
                   self.times.append({'begin': newTime, 'end': endTime})

           else:
               if self.removal({'begin': newTime, 'end': endTime}):
                   self.times.append({'begin':newTime,'end':endTime})

       def removal(self,data):
            for i in self.times:
                if i.get('begin')==data.get('begin'):
                     return False
                if   i.get('begin')>=data.get('begin') and data.get('begin')<=i.get('end'):
                      return False

            return True

def obj_str(obj):
   print(obj.name,'---',obj.times)
   return ''
def  get_ArriveTime(excelName):
    records ={}
    data = xlrd.open_workbook(excelName)
    sheet1=data.sheet_by_name('Sheet2')
    print(sheet1.nrows)
    print(range(sheet1.nrows))
    for i in range(sheet1.nrows-1):
        i=i+1

        #W0000000924 - -   - -    2020 - 07 - 20 07: 43:10.000000
        if sheet1.cell(i,1) and sheet1.cell(i,0):
            print(sheet1.cell(i, 0).value, '--', sheet1.cell(i, 1).value, '--', sheet1.cell(i, 3).value)
            if records.get(sheet1.cell(i,1).value):
                d =records.get(sheet1.cell(i,1).value)
            else:
                d=departEntity(sheet1.cell(i,1).value,sheet1.cell(i,0).value)
            d.addTime(sheet1.cell(i,3).value.strip())
            records[sheet1.cell(i,1).value]=d
        else:
            print('结束')
    return records




def sipInfo(fileName):
    data = xlrd.open_workbook(fileName)
    sheet1 = data.sheet_by_name('门店SIP')
    sipDict={}
    for i in range(sheet1.nrows-1):
        sipDict[sheet1.cell(i+1,1).value]=sheet1.cell(i+1,9).value
    return sipDict
def saveInfo(data,sipDict):
    workbook = xlwt.Workbook(encoding='gbk')
    sheet = workbook.add_sheet("分析时间清单")
    sheet.write(0, 0, '部门')
    sheet.write(0, 1, '编码')
    sheet.write(0, 2, 'sip')
    sheet.write(0, 3, '开始时间')
    sheet.write(0, 4, '结束时间')
    sheet.write(0,5,'备注')
    j=1
    for key in data.keys():
        value=data[key]
        time_length=0
        for time in data[key].times:
            #计算总抽查市时长不得240分钟
            sheet.write(j,0, value.name)
            sheet.write(j,1, value.code)
            sip=sipDict.get(value.name)
            if sip:
               sheet.write(j, 2, sipDict[value.name])
            else:
               sheet.write(j, 2, '暂无sip')
            sheet.write(j, 3, time['begin'].strftime('%H:%M'))
            sheet.write(j, 4, time['end'].strftime('%H:%M'))
            sheet.write(j, 5, value.info)
            j = j + 1


    workbook.save('ceshi.xls')

data=get_ArriveTime("./门店班车到达时间.xlsx")
sips=sipInfo('./龙田门店SIP（0805）(1).xlsx')
saveInfo(data,sips)


