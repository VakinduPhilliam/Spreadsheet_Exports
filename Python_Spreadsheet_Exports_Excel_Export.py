# Python Spreadsheet Exports.
# Exporting your Data as CSV, Excel (XLS), or XLSX in python with django.
#

#
# Excel Binary File Format.
# XLS is the main spreadsheet format which holds data in worksheets, charts, and macros.
# We are going to use xlwt library to create a spreadsheet.
# There is analogous library xlrd to read XLS files.
# Note, that this format allows to have only 256 columns.
#

#
# Here todo_obj is data source. 
#

def export_excell(request):

    import xlwt
    import datetime
    
    todo_obj=Todo.objects.filter(user_id=request.session['user_id'])

    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=todo.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Todo")
    
    row_num = 0
    
    columns = [
        (u"sl", 2000),
        (u"job", 8000),
        (u"date", 6000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)

        # set column width

        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    
    for obj in todo_obj:
        row_num += 1

        row = [
            row_num,
            obj.todo_job,
            obj.created_date.strftime("%A %d. %B %Y"),
        ]

        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)

    return response 

#
# Here, one worksheet is created, filled it with data, marked the first row in bold, and made the lines in the other cells wrapped.
# Also we set the width for each column.
#