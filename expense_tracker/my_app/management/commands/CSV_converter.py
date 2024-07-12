import csv
from os import path
from django.core.management.base import BaseCommand
from ... import forms
from ...models import Category

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.main()

    def main(self):
        categories = dict(map(lambda x: (x.name, x.id), Category.objects.all()))
        categories[""] = "99"
        with open(path.join(path.dirname(path.dirname(__file__)),
                                    '../static/books.csv')) as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for id, title, subtitle, authors, publisher, published_date, cat, distribution_expense in reader:
                bookdict = {"id_num": id,
                            "title": title,
                            "author": authors,
                            "publish_date": published_date,
                            "category": categories[cat],
                            "distribution_expense": distribution_expense}
                book = forms.BookForm(bookdict)
                if book.is_valid():
                    book.save()
                    print("Book Valid: ", bookdict)
                else:
                    print("Book invalid: ")
                    print(bookdict)

