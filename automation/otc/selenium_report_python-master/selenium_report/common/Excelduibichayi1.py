# coding:utf-8
import xlrd
import xlwt
import operator


def get_style():
    # 创建pattern
    pattern = xlwt.Pattern()
    # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan,
    # 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal,
    # 22 = Light Gray, 23 = Dark Gray, the list goes on...
    pattern.pattern_fore_colour = 2
    # Create the Pattern
    style = xlwt.XFStyle()
    # Add Pattern to Style
    style.pattern = pattern
    return style


def compared():
    # 新建一个文件，用来保存结果
    wb_result = xlwt.Workbook()
    # 打开exlce表格，参数是文件路径
    data1 = xlrd.open_workbook(file1)
    data2 = xlrd.open_workbook(file2)
    # 通过名称获取
    sheets1 = len(data1.sheets())
    sheets2 = len(data2.sheets())

    for i in range(max(sheets1, sheets2)):
        # 新建一个result的sheet
        sheet_result = wb_result.add_sheet("result{i}".format(i=i), cell_overwrite_ok=True)

        if sheets1 > sheets2 and i >= sheets2:
            table1 = data1.sheet_by_index(i)
            nrows1 = table1.nrows
            ncols1 = table1.ncols
            for s in range(nrows1):
                for k in range(ncols1):
                    sheet_result.write(s, k, table1.row_values(s)[k] + "-----", style)

        elif sheets2 > sheets1 and i >= sheets1:
            table2 = data2.sheet_by_index(i)
            nrows2 = table2.nrows
            ncols2 = table2.ncols
            for s in range(nrows2):
                for k in range(ncols2):
                    sheet_result.write(s, k, "-----" + table2.row_values(s)[k], style)

        else:
            table1 = data1.sheet_by_index(i)
            table2 = data2.sheet_by_index(i)
            nrows1 = table1.nrows
            nrows2 = table2.nrows
            ncols1 = table1.ncols
            ncols2 = table2.ncols

            for s in range(max(nrows1, nrows2)):
                for k in range(max(ncols1, ncols2)):
                    try:
                        a = table1.row_values(s)[k]
                    except IndexError:
                        if table2.row_values(s)[k] == "":
                            continue
                        sheet_result.write(s, k, "-----" + table2.row_values(s)[k], style)
                    else:
                        try:
                            b = table2.row_values(s)[k]
                        except IndexError:
                            sheet_result.write(s, k, a + "-----", style)
                        else:
                            if operator.eq(a, b):
                                sheet_result.write(s, k, a)
                            else:
                                sheet_result.write(s, k, a + "-----" + b, style)

    wb_result.save(result_file)
    print (u"执行结束，请在如下文件查看" + result_file)


# 设置对比文件
file1 = u"C:\\Users\\lipingwei\\Downloads\\recheckList20180808155956.xlsx"
file2 = u"C:\\Users\\lipingwei\\Downloads\\recheckList20180808155758.xlsx"
# 结果保存目录
result_file = u"C:\\Users\\lipingwei\\Downloads\\result.xls"
# 设置对比文字格式
style = get_style()
# 执行对比
compared()
