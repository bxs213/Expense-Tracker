from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    books = Book.objects.all()
    context = {"Books": books}
    return render(request, "home.html", context)


def contact_us(request):
    return render(request, "contact_us.html")
def categories(request):
    return render(request, "categories.html")
def info(request):
    return render(request, "book_info.html")
def add_book_view(req):
    submitted = False
    if req.method == "POST":
        form = BookForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_book?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in req.GET:
            submitted = True
    context = {'form': form,'submitted': submitted, }
    return render(req, 'add_book.html', context)

def delete_book(req, book_id):
    book = Book.objects.filter(id=book_id)
    book.delete()
    return redirect("home")

def update_book(req, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookForm(req.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("home")
    else:
        context = {"book":book,"form":form}
        return render(req, "update_book.html",context)
def search_results(req):
    if req.method == "POST":
        searched = req.POST.get("search")
        books = Book.objects.filter(id_num__contains=searched) | Book.objects.filter(title__contains=searched) | Book.objects.filter(author__contains=searched) | Book.objects.filter(category__contains=searched)
        return render(req, 'search_results.html', {'searched': books})
    else:
        return render(req, "home", BookForm.objects.all())