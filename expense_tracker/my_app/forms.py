from django import forms
from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ("id_num", "title", "author", "publish_date", "category",
                  "distribution_expense",)
        labels = {
            "id_num":"",
            "title":"",
            "author":"",
            "publish_date":"",
            "category":"",
            "distribution_expense":""
        }
        widgets = {
            "id_num":forms.TextInput(attrs={"class":'form-control',"placeholder":"ID Number"}),
            "title":forms.TextInput(attrs={"class":'form-control',"placeholder":"Title"}),
            "author":forms.TextInput(attrs={"class":'form-control',"placeholder":"Author"}),
            "publish_date":forms.TextInput(attrs={"class":'form-control',"placeholder":"Publish Date"}),
            "category":forms.TextInput(attrs={"class":'form-control',"placeholder":"Category"}),
            "distribution_expense": forms.TextInput(attrs={"class":'form-control',"placeholder":"Distribution Expense"}),
        }
    def update_db(self):
        new_book = Book(id_num=self.cleaned_data['ID'],
                        title=self.cleaned_data['title'],
                        author=self.cleaned_data['author'],
                        publish_date=self.cleaned_data['publish_date'],
                        category=self.cleaned_data['category'],
                        distribution_expense=self.cleaned_data['distribution_expense'])
        new_book.save()
