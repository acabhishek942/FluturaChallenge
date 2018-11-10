from django.core.management.base import BaseCommand, CommandError

from stock_info_app.models import Stock


from xlrd import open_workbook

class Command(BaseCommand):
    help = 'Reads stocks data from the provided xlsx file and save to sqlite DB'

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            help='The path of the excel file to read from',
            action='store',
            dest='path',
            default=False,
        )

    def handle(self, *args, **options):
        if options['path']:

            book = open_workbook(options['path'])

            first_sheet = book.sheet_by_index(0)

            print(first_sheet.row_values(0))

            for row in range(1, first_sheet.nrows):
                stock_info_array = first_sheet.row_values(row)
                single_stock_info = Stock(
                    symbol=stock_info_array[0],
                    name=stock_info_array[1],
                    market_capital=stock_info_array[2],
                    sector=stock_info_array[3] if stock_info_array[3] != 'n/a' else None,
                    industry=stock_info_array[4] if stock_info_array[3] != 'n/a' else None
                )
                single_stock_info.save()

        else:
            raise CommandError("Please enter a file name like --path='file-path'")

