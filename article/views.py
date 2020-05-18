from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm   #article formdan import ettik
from .models import Article,Comment  #ders 220 articleleri gösterdik
from django.contrib import messages #mesaj yayınlatmak için bu modülü dahil ettik
from django.contrib.auth.decorators import login_required   #loginrequired 228.ders

def articles(request): #içine request gönder demek, ders229

     keyword = request.GET.get("keyword")       #ders232 aranan kelimeye ilişkin makale bulmak için(4 satır)
     if keyword:
          articles = Article.objects.filter(title__contains = keyword)
          return render(request,"articles.html",{"articles":articles})

     articles = Article.objects.all()  #tüm articleleri aldı ve listeye attı

     return render(request,"articles.html",{"articles":articles})

# Create your views here.
def index(request):
     return render(request,"index.html")  #bu içeriği verdik ve bunu ana sayfada görebiliriz.


def about(request):
     return render(request,"about.html")


@login_required(login_url = "user:login")   #ders228 loginrequired bu şekilde kullanılabilir
def dashboard(request):
     articles = Article.objects.filter(author = request.user)  #sistemde kim varsa onun articleleri gelecektir
     context = {
          "articles" : articles
     }

     return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def addArticle(request):   #ders219
     form = ArticleForm(request.POST or None,request.FILES or None)  #yani post requestte form gelecek
     #request fıle or none kısmını 225.Derste file varsa file import et yoksa boş import et anlamında yazdık
     if form.is_valid():
          article = form.save(commit = False)   #commit etme ben edeceğim diyoruz
          article.author = request.user
          article.save()

          messages.success(request,"Makale Başarıyla Oluşturuldu...")
          return redirect("article:dashboard")

     return render(request,"addarticle.html",{"form":form})

def detail(request,id):
     #ders 222de yorum yaptık : article = Article.objects.filter(id=id).first   #.first kısmı çok çok önemli
     article = get_object_or_404(Article,id = id)   #article'ı cek ve id karşılaştır dedik
     
     comments = article.comments.all()

     return render(request,"detail.html",{"article":article,"comments":comments})


@login_required(login_url = "user:login")
def updateArticle(request,id): #226.Ders

     article = get_object_or_404(Article,id=id) 
     form = ArticleForm(request.POST or None, request.FILES or None,instance = article)
     
     if form.is_valid():   #form valid mi değil mi
          article = form.save(commit = False)   #commit etme ben edeceğim diyoruz
          article.author = request.user
          article.save()

          messages.success(request,"Makale Başarıyla Güncellendi...")
          return redirect("index")

     return render(request,"update.html",{"form":form}) #bu şekilde de formumuzu gönderiyoruz yoksa boş ekran

@login_required(login_url = "user:login")
def deleteArticle(request,id):

     article = get_object_or_404(Article, id = id )
     article.delete()
     messages.success(request,"Makale Başarıyla Silindi")
     return redirect("article:dashboard") #article altındaki dashboard'a git dedik

def addComment(request,id):
     article = get_object_or_404(Article, id = id)

     if request.method == "POST":
          comment_author = request.POST.get("comment_author")
          comment_content = request.POST.get("comment_content")

          newComment = Comment(comment_author = comment_author , comment_content = comment_content)

          newComment.article = article
          newComment.save()

     return redirect(reverse("article:detail",kwargs={"id":id}))
