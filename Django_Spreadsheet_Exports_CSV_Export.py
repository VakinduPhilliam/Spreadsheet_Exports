# Python Spreadsheet Exports.
# Exporting your Data as CSV, Excel (XLS), or XLSX in python with django.
#

#
# Comma-Separated Values Format(CSV).
# CSV is the most common import and export format for spreadsheets and databases.
# It's a textual format which one could easily create or parse himself, but there is also a python built-in library csv for handy data manipulation.
#

#
# Here, todo_obj is data source 
#

def export_csv(request):

    import csv
    from django.utils.encoding import smart_str
    
    todo_obj=Todo.objects.filter(user_id=request.session['user_id'])

    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=todo.csv'

    writer = csv.writer(response, csv.excel)

    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)

    writer.writerow([
        smart_str(u"sl"),
        smart_str(u"job"),
        smart_str(u"date"),
    ])

    row_num = 0

    for obj in todo_obj:
        row_num += 1

        writer.writerow([
            smart_str(row_num),
            smart_str(obj.todo_job),
            smart_str(obj.created_date.strftime("%A %d. %B %Y")),
        ])

    return response 