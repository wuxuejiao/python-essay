# -*- coding:utf-8 -*-  
      
import xlrd  
import uniout  
      
x1 = xlrd.open_workbook(u"E:\\副本Baikal版本详细需求列表V1.3+测试分工.xlsx")  
print [x.encode("gb2312") for x in x1.sheet_names()]
