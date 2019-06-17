# Python Outputting CSV with Django
# Python comes with a CSV library, csv.
# The key to using it with Django is that the csv module’s CSV-creation capability acts on file-like objects, and Django’s HttpResponse objects
# are file-like objects.
#
# Here’s an example:
#


import csv
from django.http import HttpResponse

def some_view(request):

# Create the HttpResponse object with the appropriate CSV header.

response = HttpResponse(content_type='text/csv')
response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

writer = csv.writer(response)
writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])

writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

return response