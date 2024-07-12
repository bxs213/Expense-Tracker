import csv
from os import path
from django.core.management.base import BaseCommand
from ... import forms, models

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.main()

    def main(self):
        for form in models.Book.objects.all():
            print("Deleted ", form.title)
            form.delete()
