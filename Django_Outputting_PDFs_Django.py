# Python Outputting PDFs with Django.
# This document explains how to output PDF files dynamically using Django views.
# The key to generating PDFs dynamically with Django is that the ReportLab API acts on file-like objects, and Django’s FileResponse objects accept
# file-like objects.
#

#
# Here’s a “Hello World” example:
#

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def some_view(request):

# Create a file-like buffer to receive PDF data.

buffer = io.BytesIO()

# Create the PDF object, using the buffer as its "file."

p = canvas.Canvas(buffer)

# Draw things on the PDF. Here's where the PDF generation happens.
# See the ReportLab documentation for the full list of functionality.

p.drawString(100, 100, "Hello world.")

# Close the PDF object cleanly, and we're done.

p.showPage()
p.save()

# FileResponse sets the Content-Disposition header so that browsers
# present the option to save the file.

return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
