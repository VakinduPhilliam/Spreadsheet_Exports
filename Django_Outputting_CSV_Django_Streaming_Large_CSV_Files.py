# Python Outputting CSV with Django
#
# Streaming large CSV files.
# When dealing with views that generate very large responses, you might want to consider using Django�s StreamingHttpResponse instead. 
# For example, by streaming a file that takes a long time to generate you can avoid a load balancer dropping a connection that might have otherwise
# timed out while the server was generating the response.
#

#
# In this example, we make full use of Python generators to efficiently handle the assembly and transmission of a large CSV file:
#


import csv
from django.http import StreamingHttpResponse

class Echo:

"""An object that implements just the write method of the file-like interface."""

def write(self, value):

"""Write the value by returning it, instead of storing in a buffer."""

return value

def some_streaming_csv_view(request):

"""A view that streams a large CSV file."""

# Generate a sequence of rows. The range is based on the maximum number of
# rows that can be handled by a single sheet in most spreadsheet
# applications.

rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))

pseudo_buffer = Echo()
writer = csv.writer(pseudo_buffer)

response = StreamingHttpResponse((writer.writerow(row) for row in rows),
content_type="text/csv")

response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

return response