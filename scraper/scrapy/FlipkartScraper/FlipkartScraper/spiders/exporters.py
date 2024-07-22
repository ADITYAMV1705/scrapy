import csv
from scrapy.exporters import CsvItemExporter

class CustomCsvItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs['quotechar'] = '"'
        kwargs['quoting'] = csv.QUOTE_ALL
        super(CustomCsvItemExporter, self).__init__(*args, **kwargs)
