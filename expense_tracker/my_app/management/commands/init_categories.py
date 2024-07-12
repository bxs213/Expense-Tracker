from django.core.management.base import BaseCommand
from ... import models,forms

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.main()

    def main(self):
        initial_categories = ("Business Analytics",
                              "Python",
                              "Data Science",
                              "Math",
                              )

        for model in initial_categories:
             form = forms.CategoryForm({"name":model})
             if form.is_valid():
                 form.save()

             else:
                print("invalid form", model)



