# Python_Spreadsheet_Exports
Python Spreadsheet Exports. 

Exporting your Data as CSV, Excel (XLS), or XLSX in Python with Django.  

Formats Explored;  

> Comma-Separated Values Format (CSV): CSV is the most common import and export format for spreadsheets and databases. It's a textual format which one could easily create or parse himself, but there is also a python built-in library csv for handy data manipulation.  >    Excel Binary File Format: XLS is the main spreadsheet format which holds data in worksheets, charts, and macros. We are going to use xlwt library to create a spreadsheet. There is analogous library xlrd to read XLS files. Note, that this format allows to have only 256 columns.  >      Office Open XML Format: XLSX (a.k.a. OOXML or OpenXML) is a zipped, XML-based file format developed by Microsoft. It is fully supported by Microsoft Office 2007 and newer versions. OpenOffice 4.0, for example, can only read it. There is a python library openpyxl for reading and writing those files. This format is great when you need more than 256 columns and text formatting options.  >     PDFs with Django This document explains how to output PDF files dynamically using Django views. The key to generating PDFs dynamically with Django is that the ReportLab API acts on file-like objects, and Django’s FileResponse objects accept file-like objects.
