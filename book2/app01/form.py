from django import forms
from django.forms import models as form_model

from app01 import models


class PublisherForm(forms.Form):
    p_name = forms.CharField(max_length=64,
                             label='出版社名字',
                             # widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                             )


class BookForm(forms.Form):
    b_name = forms.CharField(max_length=64, label='出版的书籍')
    # 下拉框单选
    pub_obj = form_model.ModelChoiceField(queryset=models.Publisher.objects.all())


class AuthorForm(forms.Form):
    a_name = forms.CharField(max_length=64, label='作者的名字')
    # 下拉框多选
    books = form_model.ModelMultipleChoiceField(queryset=models.Book.objects.all())
