from django.shortcuts import render, redirect
from django.views.generic import ListView


from .forms import ContactForm, AddComment
from .models import News, Category, Comment
from django.core.mail import send_mail


class HomePromod(ListView):
    model = News
    template_name = 'news/home_promod_list.html'
    context_object_name = 'news'
    extra_context = {'title': 'ПроМод'}


class PromodByCategory(ListView):
    model = News
    template_name = 'news/home_promod_list.html'
    context_object_name = 'news'


def add_feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], ['arhangel317@yandex.ru'], fail_silently=False)
        return redirect('add_feedback')
    else:
        form = ContactForm()
    return render(request, 'news/add_feedback.html', {"form": form})


# def index(request):
#     news = News.objects.all()
#     context = {'news': news,
#                'title': 'ПроМод.бел', }
#     return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, "category": category})


def view_more(request, news_id):
    more_item = News.object.get(pk=news_id)
    return render(request, 'news/view_more.html', {"more_item": more_item})


def add_comment(request):
    if request.method == "POST":
        form = AddComment(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = AddComment()
    comment = Comment.objects.all
    context = {
        'form': form,
        'comment': comment,
        }
    return render(request, 'news/add_comment.html', context)


def contacts(request):
    return render(request, 'news/contacts.html')


def add_busket(request):
    return render(request, 'news/add_busket.html')
