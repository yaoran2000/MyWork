#Read Excel Library
import xlrd
#Write Excel Library
from pyexcelerate import Workbook
#RegEx Support
import re

def writeHeaders(targetBook):
	ws = targetBook.new_sheet("Result")
	ws.range("A1","P1").value = [['盘点日期','罐号','结构形式','属性','品名','截止时间','租罐性质','当日结存','海关放行数量',	'','财务控量','未放行量','罐容','合同开始','合同结束','备注']]

	return ws


def processSheetTable(sourceTable,targetBookSheet,startline):
	#print(sourceTable.nrows)
	print(startline)

	for j in range(1,sourceTable.nrows):
		for k in range(1,16):
			targetBookSheet.set_cell_value(startline + j,k,sourceTable.cell(j,k - 1).value)


	return targetBookSheet, startline + sourceTable.nrows - 1



if __name__ == "__main__":

	targetWorkBook = Workbook()
	targetWorkSheet = writeHeaders(targetWorkBook)

	sourceBook = xlrd.open_workbook("/Users/yao/MyWork/combinExcel/201701.xlsx")

	sheetlist = sourceBook.sheet_names()

	#print(sheetlist)

	p = 1
	for i in range(0, len(sheetlist)):
		if re.match('\d{8}',sheetlist[i]):	#Exclude Non-number Sheet eg: 20170101
			#print(sheetlist[i])
			#processSheetTable(sourceBook.sheet_by_name(sheetlist[i]))
			targetWorkSheet, p = processSheetTable(sourceBook.sheet_by_name(sheetlist[i]),targetWorkSheet,p)

	targetWorkBook.save("/Users/yao/MyWork/combinExcel/result.xlsx")

