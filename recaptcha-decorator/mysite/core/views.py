from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from .decorators import check_recaptcha
from .models import Comment
from .forms import CommentForm


@check_recaptcha
def comments(request):
    comments_list = Comment.objects.order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            form.save()
            messages.success(request, 'New comment added with success!')
            return redirect('comments')
    else:
        form = CommentForm()

    return render(request, 'core/comments.html', {'comments': comments_list, 'form': form})
