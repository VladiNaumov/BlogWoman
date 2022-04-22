from django import forms
from django.core.exceptions import ValidationError

from blogWoman.models import Category, Women

"""
# добавление формы не связанные с моделью
class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField(label="Publication", required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),  empty_label="Category not selected")
"""

# добавление формы связанные с моделью
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Category not selected"

    class Meta:
        model = Women
        #fields = '__all__'
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

        """ создание пользовательского (своего) валидатора (проверки) """
        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 200:
                raise ValidationError('Длина заголовка превышает 200 символов')

            return title






