from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm


# List Blog Posts:
def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

# View Blog Post Details:
def post_detail(request, hajar):
    post = get_object_or_404(BlogPost, hajar=hajar)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})

# Create Blog Post:
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

# Edit Blog Post
def edit_post(request, hajar):
    post = get_object_or_404(BlogPost, hajar=hajar)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', hajar=post.hajar)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

# Add Comment to blog post
def add_comment(request, hajar):
    post = get_object_or_404(BlogPost, hajar=hajar)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', hajar=post.hajar)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

# Edit Comment
def edit_comment(request, hajar):
    comment = get_object_or_404(Comment, hajar=hajar)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', hajar=comment.post.hajar)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form})

# Delete Blog Post
def delete_post(request, hajar):
    post = get_object_or_404(BlogPost, hajar=hajar)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'delete_post.html', {'post': post})

# Delete Comment
def delete_comment(request, hajar):
    comment = get_object_or_404(Comment, hajar=hajar)
    post_hajar = comment.post.hajar
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', hajar=post_hajar)
    return render(request, 'delete_comment.html', {'comment': comment})
