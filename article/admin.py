from django.contrib import admin


from .models import Article,Comment     #.models demek aynı klasörden models i al demek, 
#class olarak ta bizim olusturdugumuz Article yi aldık
#comment i 234.derste ekledik comment alanı için

# Register your models here.

#admin.site.register(Article)  #Article artık admin panelinde de görünecek.
#ilk olarak 199.DERSte yukarıdaki gibi yazdık ama artık aşağıdaki kodları yazıp daha da geliştiriyoruz.

admin.site.register(Comment)  #comment kısmını kaydettik (234.ders)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date","content"]   
    #üstteki kod ile web arayüzünde http://127.0.0.1:8000/admin/article/article/ yeni içerikler ekleyebiliriz.
    # bu döküman ile bu sayfayı oluşturuyoruz: https://docs.djangoproject.com/en/3.0/ref/contrib/admin/

    list_display_links = ["title","created_date"]
    
    search_fields = ["title"]
    
    list_filter = ["created_date"]   #sitenin sağ tarafında güzel bir filtre kutucuğu oluşturduk
    #bu kutucuga created_date dediğimizde tarihe, title dediğimizde başlığa, content dediğimizde içeriğe göre filtre yapar
    
    class Meta:   #django dökümanında geçiyor bu kod
        model = Article
