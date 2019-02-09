import xlwt;
from datetime import datetime;
from xlrd import open_workbook;
from xlwt import Workbook;
from xlutils.copy import copy
from pathlib import Path

'''style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save('example.xls')
'''

'''
# Add some cell formats.
format1 = workbook.add_format({'num_format': '#,##0.00'})
format2 = workbook.add_format({'num_format': '0%'})

# Set the column width and format.
worksheet.set_column('B:B', 18, format1)

# Set the format but not the column width.
worksheet.set_column('C:C', None, format2)
'''

def output(filename, sheet, num, name, id, present_status):
    my_file = Path('firebase/attendance_files/'+filename+str(datetime.now().date())+'.xls');
    if my_file.is_file():
        rb = open_workbook('firebase/attendance_files/'+filename+str(datetime.now().date())+'.xls');
        book = copy(rb);
        sh = book.get_sheet(0)
        
        # file exists
    else:
        book = xlwt.Workbook()
        sh = book.add_sheet(sheet)
    
    style0 = xlwt.easyxf('font: name Times New Roman, color-index blue, bold on, height 300',
                         num_format_str='#,##0.00')
    
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    #variables = [x, y, z]
    #x_desc = 'Display'
    #y_desc = 'Dominance'
    #z_desc = 'Test'
    #desc = [x_desc, y_desc, z_desc]
    sh.write(0,0,datetime.now().date(),style1);


    col1_name = 'Name'
    col2_name = 'ID'
    col3_name = 'Present Status'
    
    print("Successfully Recognized")
    
    #sh.col1_name('A:B', 20)
   # sh.set_column('C:C', 30)

    sh.write(1,0,col1_name,style0)
    sh.write(1, 1, col2_name,style0)
    sh.write(1, 2,col3_name, style0)
    #print("Successfully written")

    sh.write(num+1,0,name);
    sh.write(num+1, 1, id);
    sh.write(num+1, 2, present_status);
    #You may need to group the variables together
    #for n, (v_desc, v) in enumerate(zip(desc, variables)):
    fullname=filename+str(datetime.now().date())+'.xls';
    book.save('firebase/attendance_files/'+fullname)
    return fullname;
