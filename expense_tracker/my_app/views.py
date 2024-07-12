from django.shortcuts import render, redirect
from .models import Book, Category
from .forms import BookForm,CategoryForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# Import django's Paginator
from django.core.paginator import Paginator


# Routing logic for authenticated users
@login_required(login_url="login")
def home(req):
    # Set up Pagination
    pag = Paginator(Book.objects.all().order_by("category"), 75)
    page = req.GET.get("page")
    book_pages = pag.get_page(page)

    # Render home page
    context = {"book_pages": book_pages}
    return render(req, "home.html", context)


@login_required(login_url="login")
def contact_us(req):
    return render(req, "contact_us.html")
@login_required(login_url="login")
def categories(req):

    pag = Paginator(Category.objects.all().order_by("name"), 10)
    page = req.GET.get("page")
    category_pages = pag.get_page(page)

    # Render home page
    context = {"category_pages": category_pages}
    return render(req, "categories.html", context)

@login_required(login_url="login")
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

@login_required(login_url="login")
def delete_book(req, book_id):
    book = Book.objects.filter(id=book_id)
    messages.success(req, f'Successfully deleted '
                          f'"{Book.objects.filter(id__contains=book_id)[0].title}"')
    book.delete()
    return redirect("home")

@login_required(login_url="login")
def update_book(req, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookForm(req.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(req,f'Successfully updated '
                             f'"{Book.objects.filter(id__contains=book_id)[0].title}"')
        return redirect("home")
    else:
        context = {"book":book,"form":form}
        return render(req, "update_book.html",context)

@login_required(login_url="login")
def search_results(req):
    if req.method == "POST":
        searched = req.POST.get("search")
        if searched:
            books = Book.objects.filter(id_num__contains=searched) |\
                Book.objects.filter(title__contains=searched) |\
                Book.objects.filter(author__contains=searched) |\
                Book.objects.filter(category__name__contains=searched) | \
                Book.objects.filter(publish_date__contains=searched) | \
                Book.objects.filter(distribution_expense__contains=searched)
            return render(req, 'search_results.html', {'searched': books})
        else:
            return redirect("home")
    else:
        return redirect("home")
@login_required(login_url="login")
def add_category(req):
    submitted = False
    if req.method == "POST":
        form = CategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_category?submitted=True')
    else:
        form = CategoryForm()
        if 'submitted' in req.GET:
            submitted = True

    context = {'form': form, 'submitted': submitted, }
    return render(req, 'add_category.html', context)

@login_required(login_url="login")
def update_category(req, category_id):
    category = Category.objects.get(pk=category_id)
    form = CategoryForm(req.POST or None, instance=category)
    if form.is_valid():
        form.save()
        messages.success(req,f'Successfully updated '
                             f'"{Category.objects.filter(id__contains=category_id)[0].name}"')
        return redirect("categories")
    else:
        context = {"category":category,"form":form}
        return render(req, "update_category.html",context)

@login_required(login_url="login")
def delete_category(req, category_id):
    category = Category.objects.filter(id=category_id)

    messages.success(req, f'Successfully deleted '
                          f'"{Category.objects.filter(id__contains=category_id)[0].name}"')
    category.delete()
    return redirect("categories")