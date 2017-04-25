import sys
#Read Excel Library
import xlrd
#Write Excel Library
from pyexcelerate import Workbook
#RegEx Support
import re


#	HJDX Biz Excel Combine Tool V1.0
#	Author: Yao Ran
#	Usage:
#		$ python3 combExcel.py Source/201703.xls Target/201703c.xlsx


def writeHeaders(targetBook):
	ws = targetBook.new_sheet("Result")
	ws.range("A1","P1").value = [['盘点日期','罐号','结构形式','属性','品名','截止时间','租罐性质','当日结存','海关放行数量',	'','财务控量','未放行量','罐容','合同开始','合同结束','备注']]

	return ws


def processSheetTable(sourceTable,targetBookSheet,startline):
	#print(sourceTable.nrows)
	print("%d rows processsed"%startline)

	for j in range(1,sourceTable.nrows):
		for k in range(1,16):
			targetBookSheet.set_cell_value(startline + j,k,sourceTable.cell(j,k - 1).value)


	return targetBookSheet, startline + sourceTable.nrows - 1


if __name__ == "__main__":

	#for arg in sys.argv:
	#	print(arg)
	if len(sys.argv) == 3:

		targetWorkBook = Workbook()
		targetWorkSheet = writeHeaders(targetWorkBook)

		#sourceBook = xlrd.open_workbook("/Users/yao/MyWork/combinExcel/Source/201701.xlsx")
		sourceBook = xlrd.open_workbook(sys.argv[1])
		sheetlist = sourceBook.sheet_names()

		#print(sheetlist)

		p = 1
		for i in range(0, len(sheetlist)):
			if re.match('\d{8}',sheetlist[i]):	#Exclude Non-number Sheet eg: 20170101
				#print(sheetlist[i])
				#processSheetTable(sourceBook.sheet_by_name(sheetlist[i]))
				targetWorkSheet, p = processSheetTable(sourceBook.sheet_by_name(sheetlist[i]),targetWorkSheet,p)

		targetWorkBook.save(sys.argv[2])
		#targetWorkBook.save("/Users/yao/MyWork/combinExcel/Target/result.xlsx")
	else:
		print("Usage: python3 combExcel.py SourceExcelFile TargetExcelFile")




