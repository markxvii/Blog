import datetime
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
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
    return blogs[:7]


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = seven_days_data(blog_content_type)
    # 获取近7日热门博客的缓存数据,如果无则创建缓存
    hot_blogs_for_week = cache.get('hot_blogs_for_week')
    if hot_blogs_for_week is None:
        hot_blogs_for_week = week_hot_blog()
        cache.set('hot_blogs_for_week', hot_blogs_for_week, 3600)
        print('calc')
    else:
        print('use cache')

    context = {}
    context['read_nums'] = read_nums
    context['dates'] = dates
    context['today_hot_data'] = today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = yesterday_hot_data(blog_content_type)
    context['week_hot_blog'] = week_hot_blog()
    return render(request, 'home.html', context)


