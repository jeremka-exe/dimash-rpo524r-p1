from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Adv
from django.db.models import Q, Func, F

def home_page(request):
    hot_posts = Post.objects.all().order_by('-created_at')[:4]
    posts = Post.objects.all().order_by('-created_at')
    advs = Adv.objects.order_by('?')[:4]
    context = {
        'hot_posts': hot_posts,
        'posts': posts,
        'advs': advs
    }
    return render(request, "index.html", context)

def all_news_page(request):
    posts = Post.objects.all().order_by('-created_at')
    advs = Adv.objects.order_by('?')[:4]
    context = {
        'posts': posts,
        'advs': advs
    }
    return render(request, "all-news.html", context)


def news_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    advs = Adv.objects.order_by('?')[:4]
    context = {
        'category': category,
        'posts': posts,
        'advs': advs
    }
    return render(request, "news-by-category.html", context)


def search_page(request):
    advs = Adv.objects.order_by('?')[:4]
    context = {
        'advs': advs
    }
    return render(request, "search.html", context)

def search_results(request):
    advs = Adv.objects.order_by('?')[:4]

    query = request.GET.get('q', '').strip()

    results = []

    if query:
        query_lower = query.lower()

        for post in Post.objects.all().order_by('-created_at'):
            if query_lower in post.title.lower() or query_lower in post.content.lower():
                results.append(post)

    context = {
        'query': query,
        'results': results,
        'advs': advs
    }

    return render(request, "search-results.html", context)

def read_news_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    advs = Adv.objects.order_by('?')[:4]
    similar_posts = Post.objects.filter(
        category=post.category
    ).exclude(pk=post.pk).order_by('-created_at')[:4]
    context = {
        'post': post,
        'advs': advs,
        'similar_posts': similar_posts
    }
    return render(request, "read-news.html", context)