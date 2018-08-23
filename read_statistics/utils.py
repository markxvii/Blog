from django.contrib.contenttypes.models import ContentType
from .models import ReadNum


# 如果获取不了浏览器存储的cookie则次数+1
def read_statistics_once(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = '%s_%s_read' % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            # 存在记录则取出数据
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        else:
            # 不存在记录则新建一条对应博客的数据
            readnum = ReadNum(content_type=ct, object_id=obj.pk)
        # 计数加一
        readnum.read_num += 1
        readnum.save()
    return key
