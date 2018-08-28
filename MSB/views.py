import datetime
from django.shortcuts import render_to_response
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from read_statistics.utils import seven_days_data, today_hot_data, yesterday_hot_data
from blog.models import Blog


def week_hot_blog():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects \
        .filter(read_details__date__lt=today, read_details__date__gte=date) \
        .values('id', 'title') \
        .annotate(read_num_sum=Sum('read_details__read_num')) \
        .order_by('-read_num_sum')
    return blogs


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = seven_days_data(blog_content_type)
    context = {}
    context['read_nums'] = read_nums
    context['dates'] = dates
    context['today_hot_data'] = today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = yesterday_hot_data(blog_content_type)
    context['week_hot_blog'] = week_hot_blog()
    return render_to_response('home.html', context)
