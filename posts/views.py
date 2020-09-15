from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post_table


# Create your views here.
def home(request):
    post_list = Post_table.objects.all().order_by('-id')  # latest will appear first thats why '-id'
    query = request.GET.get('q')

    if query:
        post_list = post_list.filter(Q(title__icontains=query) |
                                     Q(content__icontains=query))

    paginator = Paginator(post_list, 3)  # 3 is the num of posts in a single page
    page = request.GET.get('page')

    post_list = paginator.get_page(page)

    context = {
        'posts': post_list
    }
    return render(request, "index.html", context)


def detail_view(request, id):
    # post = Post_table.objects.get(id=id)  #this also works but not recomended
    # bcz we get name error if page is not present

    post = get_object_or_404(Post_table, id=id)
    context = {
        'post': post
    }

    return render(request, 'details.html', context)


@login_required(login_url='/')
def form_view(request):
    form = PostForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'form.html', context)


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post_table, id=id)
    post.delete()
    return redirect('/')


@login_required
def update_post(request, id):
    post = get_object_or_404(Post_table, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(post.get_absolute_url())
        # return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'form.html', context)
