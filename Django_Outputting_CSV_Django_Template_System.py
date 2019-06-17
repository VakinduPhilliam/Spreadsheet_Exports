# Python Outputting CSV with Django
#
# Using the template system.
# Alternatively, you can use the Django template system to generate CSV. This is lower-level than using the convenient
# Python csv module, but the solution is presented here for completeness.
#
# The idea here is to pass a list of items to your template, and have the template output the commas in a for loop.
#
# Here’s an example, which generates the same CSV file as above:
#

from django.http import HttpResponse
from django.template import Context, loader

def some_view(request):

# Create the HttpResponse object with the appropriate CSV header.

response = HttpResponse(content_type='text/csv')
response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

# The data is hard-coded here, but you could load it from a database or
# some other source.

csv_data = (
('First row', 'Foo', 'Bar', 'Baz'),
('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"), )

t = loader.get_template('my_template_name.txt')

c = Context({
'data': csv_data,
})

response.write(t.render(c))

return response
