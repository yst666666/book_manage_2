from django.shortcuts import render, redirect

from app01 import models
from app01.form import PublisherForm
from app01.model_form import BookForm,AuthorForm


# Create your views here.

def publish_list(request):
    publish_all = models.Publisher.objects.all()
    return render(request, 'publish/publish_list.html', {'publish_all': publish_all})


# *--*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*--*-*-**-*--*-*-*-*-*-*-
#     form 的使用,不能放源数据,不能进行改的操作,low               -*
# *-*-*-**-*-*-*-**-*-**-*-*+**-*-*-**-*-*-**-*-**-*-*-*-*-*-
def publish_add(request, pk=None):
    form_obj = PublisherForm()
    if request.method == 'POST':
        form_obj = PublisherForm(data=request.POST)
        if form_obj.is_valid():
            p_name = form_obj.cleaned_data.get('p_name')
            models.Publisher.objects.create(p_name=p_name)
            return redirect('/publish_list/')

    return render(request, 'publish/publish_add_1.html', {'form_obj': form_obj})


def publish_edit(request, pk):
    # 给编辑页面传回id--对应的默认值
    pub_obj = models.Publisher.objects.filter(pk=pk).first()

    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        pub_obj.p_name = pub_name
        pub_obj.save()
        return redirect('/publish_list/')

    return render(request, 'publish/publish_edit.html', {'pub_obj': pub_obj})


def publish_del(request, pk):
    pub_obj = models.Publisher.objects.filter(pk=pk)
    pub_obj.delete()
    return redirect('/publish_list/')


def book_list(request):
    book_all = models.Book.objects.all()
    return render(request, 'book/book_list.html', {'book_all': book_all})


# *--*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*--*-*-**-*--*-*-*-*-*-*-
#                     ModelForm                            -*
# *-*-*-**-*-*-*-**-*-**-*-*+**-*-*-**-*-*-**-*-**-*-*-*-*-*-
def book_add_edit(request, pk=None):
    obj = models.Book.objects.filter(pk=pk).first()
    form_obj = BookForm(instance=obj)
    if request.method == 'POST':
        form_obj = BookForm(data=request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/book_list')
    if pk:
        title = '书籍编辑页面'
    else:
        title = '书籍新增页面'
    return render(request, 'book/book_add_edit.html', {'form_obj': form_obj, 'title': title})


def book_del(request, pk):
    pub_obj = models.Book.objects.filter(pk=pk)
    pub_obj.delete()
    return redirect('/book_list/')


def author_list(request):
    author_all = models.Author.objects.all()
    return render(request, 'author/author_list.html', {'author_all': author_all})


# *--*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*--*-*-**-*--*-*-*-*-*-*-
#                     ModelForm                            -*
# *-*-*-**-*-*-*-**-*-**-*-*+**-*-*-**-*-*-**-*-**-*-*-*-*-*-
def author_add_edit(request, pk=None):
    obj = models.Author.objects.filter(pk=pk).first()
    form_obj = AuthorForm(instance=obj)
    if request.method == 'POST':
        form_obj = AuthorForm(data=request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/author_list')
    if pk:
        title = '作者编辑页面'
    else:
        title = '作者新增页面'
    return render(request, 'author/author_add_edit.html', {'form_obj': form_obj, 'title': title})


def author_del(request, pk):
    aut_obj = models.Author.objects.filter(pk=pk)
    aut_obj.delete()
    return redirect('/author_list/')
