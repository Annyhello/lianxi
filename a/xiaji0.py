#coding=utf-8

# 读取excel内容
import xlrd

# 获取excel文件存放地址(加r声明为raw字符串，这样就不会处理其中的转义了。否则，可能会报错)
data = xlrd.open_workbook(r'../a/d/dataxiaji0.xlsx')#上级目录引用,b文件
# 获取第1个sheet
# tables = data.sheets()[0]
tables = data.sheet_by_index(0) #通过索引顺序获取
# tables = data.sheet_by_name(u'data')#通过名称获取
# 打印sheet名字
print data.sheet_names()
# 打印行数
rows = tables.nrows
print '行数：',rows
#打印列数
cols = tables.ncols
print '列数：',cols
# 获取整行和整列的值（数组）
# table.row_values(i)
# table.col_values(i)

# 打印第2行第4列，下标从[0]开始
for i in range(1,rows):
    for j in range(1,cols):
        #print '列值：',tables.col_values(j)
        #print '单元格列值：',tables.cell(i, j).value
        if tables.cell(i, j).value=='method':
            print 111111
            method=tables.cell_value(i+1,j)
            print 'method值：',method
        elif tables.cell(i, j).value=='path':
            path = tables.cell_value(i + 1, j)
            print 'path值：', path
        elif tables.cell(i, j).value=='header':
            header = tables.cell_value(i + 1, j)
            print 'header值：', header
        elif tables.cell(i, j).value=='params':
            params = tables.cell_value(i + 1, j)
            print 'params值：', params
    break
        # else:
        #     print '数据不存在！'