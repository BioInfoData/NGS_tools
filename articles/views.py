from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html')

def articles_list(request):
    #articles = Articles.objects.all().order_by('date')
    articles_alignment = Articles.objects.all().filter(type = "alignment")
    articles_DE = Articles.objects.all().filter(type="DE")
    articles_counts = Articles.objects.all().filter(type="count_reads")
    articles_qc = Articles.objects.all().filter(type="QC")
    articles_func = Articles.objects.all().filter(type="functional")
    return render(request,"articles/articles_list.html",
                  {"articles_alignment":articles_alignment,
                   "articles_DE":articles_DE,
                   "articles_counts":articles_counts,
                   "articles_qc" : articles_qc,
                   "articles_func":articles_func})


def articale_detail(request, slug):
    article = Articles.objects.get(slug=slug)
    comments = article.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article = article
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    #return render(request, "articles/article_detail.html", {"article": article})
    return render(request, "articles/article_detail.html", {'article': article,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def about(request):
    return render(request,'about.html')

