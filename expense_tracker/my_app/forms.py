from django import forms
from django.forms import ModelForm
from .models import Book,Category



class CategoryForm(ModelForm):
    class Meta:
        model = Category

        fields = ("name",)
        labels = {"name":""}
        widgets = {
            "name": forms.TextInput(attrs={"class": 'form-control', "placeholder": "Category Name"}),
        }

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
        category = forms.ChoiceField(choices=Category.cat_dict())

        widgets = {
            "id_num":forms.TextInput(attrs={"class":'form-control',"placeholder":"ID Number"}),
            "title":forms.TextInput(attrs={"class":'form-control',"placeholder":"Title"}),
            "author":forms.TextInput(attrs={"class":'form-control',"placeholder":"Author"}),
            "publish_date":forms.TextInput(attrs={"class":'form-control',"placeholder":"Publish Date"}),
            "category":forms.Select(attrs={"class":'form-control',"placeholder":"Categories"}),
            "distribution_expense": forms.TextInput(attrs={"class":'form-control',"placeholder":"Distribution Expense"}),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False