from django.shortcuts import render, redirect

from app01 import models


# Create your views here.

def publish_list(request):
    publish_all = models.Publisher.objects.all()
    return render(request, 'publish/publish_list.html', {'publish_all': publish_all})


def publish_add(request):
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        pub_obj = models.Publisher.objects.create(p_name=pub_name)
        pub_obj.save()
        return redirect('/publish_list')
    return render(request, 'publish/publish_add.html')


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


def book_add(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        book_obj = models.Book.objects.create(b_name=book_name)
        book_obj.pub_id = pub_id    # 外键
        book_obj.save()
        return redirect('/book_list/')

    # 查询所有的出版社
    pub_all = models.Publisher.objects.all()
    return render(request, 'book/book_add.html', {'pub_all': pub_all})


def book_edit(request, pk):
    # 给编辑页面传回id--对应的默认值
    book_obj = models.Book.objects.filter(pk=pk).first()

    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        book_obj.p_name = book_name
        book_obj.pub_id = pub_id
        book_obj.save()
        return redirect('/book_list/')
    pub_all = models.Publisher.objects.all()
    return render(request, 'book/book_edit.html', {'book_obj': book_obj, 'pub_all': pub_all})


def book_del(request, pk):
    pub_obj = models.Book.objects.filter(pk=pk)
    pub_obj.delete()
    return redirect('/book_list/')


def author_list(request):
    author_all = models.Author.objects.all()
    return render(request, 'author/author_list.html', {'author_all': author_all})


def author_add(request):
    if request.method == 'POST':
        a_name = request.POST.get('a_name')
        book = request.POST.getlist('book_id')  # 多对多的操作get_list,获取select-option-multiple
        author_obj = models.Author.objects.create(a_name=a_name)
        author_obj.books.set(book) # 找到多对多的关系对象.set()进行设置
        return redirect('/author_list/')

    # 查询所有的出版社
    book_all = models.Book.objects.all()
    return render(request, 'author/author_add.html', {'book_all': book_all})


def author_edit(request, pk):
    # 给编辑页面传回id--对应的默认值
    aut_obj = models.Author.objects.filter(pk=pk).first()

    if request.method == 'POST':
        a_name = request.POST.get('a_name')
        book = request.POST.getlist('book_id')
        aut_obj.a_name = a_name
        aut_obj.books.set(book)
        return redirect('/author_list/')
    book_all = models.Book.objects.all()
    return render(request, 'author/author_edit.html', {'aut_obj': aut_obj, 'book_all': book_all})


def author_del(request, pk):
    aut_obj = models.Author.objects.filter(pk=pk)
    aut_obj.delete()
    return redirect('/author_list/')
