from django.db import models
from ckeditor.fields import RichTextField   #ders 224

# Create your models here.

class Article(models.Model):  #yukarıdaki models'ten türettik.
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar") #bu alanım users tablosunu işaret ediyor diyoruz.
#on_delete yaptık yani user kullanıcısı silindiğinde o kullanıcıya ait veriler de silinecektir.
    title = models.CharField(max_length = 50,verbose_name="Başlık") #title max uzunlugu 50 karakter oldu
    content = RichTextField()     #text field i kullanıyoruz
    created_date = models.DateTimeField(auto_now_add = True,verbose_name="Oluşturma tarihi") 
    article_image = models.FileField(blank=True,null = True,verbose_name ="Makaleye Fotoğraf Ekleyin") #225
    def __str__(self): #bu metod ile arayüzde articlelerde Article object 1vs. yerine title bilgisini göreceğiz. 
        return self.title #ayni sekilde self.author dersek yazar ismi görünecektir.
        
    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):  #ders234 yorum ekleme alanı için
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment_content  #bu işlemden sonra admin panelimizde commentler daha güzel görünüme sahip oldu

    class Meta:
        ordering = ['-comment_date']
