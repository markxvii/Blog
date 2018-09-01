from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from .models import Comment
from .forms import CommentForm


# Create your views here.
def update_comment(request):
    '''referer = request.META.get('HTTP_REFERER', reverse('home'))
    # 数据检查
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message': '请先登陆', 'redirect_to': referer})
    text = request.POST.get('text', '').strip()
    if text == '':
        return render(request, 'error.html', {'message': '评论内容不能为空！', 'redirect_to': referer})
    try:
        content_type = request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except Exception as e:
        return render(request, 'error.html', {'message': '评论博客不存在', 'redirect_to': referer})

    # 检查通过后将评论内容存入数据库
    comment = Comment()
    comment.user = request.user
    comment.text = text
    comment.content_object = model_obj
    comment.save()

    return redirect(referer)'''
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message': '请先登陆', 'redirect_to': referer})

    comment_form = CommentForm(request.POST, user=request.user)
    if comment_form.is_valid():
        # 检查通过后将评论内容存入数据库
        comment = Comment()
        comment.user = request.user
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']
        comment.save()
        return redirect(referer)
    else:
        return render(request, 'error.html', {'message': comment_form.errors, 'redirect_to': referer})
