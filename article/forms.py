from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):  #bu yeni yontem ders218
    class Meta:
        model = Article   #form ile django bağlantılandı
        fields = ["title","content","article_image"] #225
        