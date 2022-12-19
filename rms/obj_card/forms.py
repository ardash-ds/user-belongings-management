from django import forms

from .models import Object, Picture, Category


class ObjForm(forms.Form):

    name = forms.CharField(label=u'Название')
    dis = forms.CharField(label=u'Описание')
    category = forms.ModelChoiceField(
        queryset=Category.objects, 
        label="Выберите категорию",
        )
    photos = forms.ImageField(
        label=u'Фотографии', 
        widget=forms.FileInput(attrs={'multiple': 'multiple'})
        )

    
# class ObjForm(forms.ModelForm):
#
#     class Meta:
#         model = Object
#         fields = ('name', 'description',)
#
#
# class PicForm(forms.ModelForm):
#
#     class Meta:
#         model = Picture
#         fields = ('image',)
