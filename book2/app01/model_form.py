from django import forms

from app01 import models


# class PublisherForm(forms.ModelForm):
#     class Meta:
#         model = models.Publisher
#         fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'
