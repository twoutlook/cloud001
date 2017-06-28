

import os
import sys
import django




# https://stackoverflow.com/questions/28525825/django-core-exceptions-improperlyconfigured-requested-setting-logging-config-b
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.db import models
from projectnote.models import TrackReport00
from projectnote.models import T100Dept

# all=TrackReport00.objects.all()
# print("to update dept report cnt")
# print (all)
#
# dept_id =1004
status01='鼎捷開發未开工'
status02='鼎捷開發在制'
status03='鼎捷開發完成待验收'
status04='鼎捷開發完成已验收'
status05='鼎捷開發取消'
status06='鼎捷開發状态不明'

# dept_list= T100Dept.objects.filter(D0__gt = 0).order_by("t100DeptId")

dept_list= T100Dept.objects.order_by("t100DeptId")
for d in dept_list:
    print('--- before ---',d.t100DeptId, d.t100DeptName, d.D0,d.D1,d.D2,d.D3,d.D4,d.D5,d.D6)
    # https://stackoverflow.com/questions/629551/how-to-query-as-group-by-in-django
    # item_list = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(h = status01).values('h').annotate(cnt=models.Count('h'))

    # d.D1 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(h = status01).count()
    # d.D2 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(h = status02).count()
    # d.D3 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(h = status03).count()
    # d.D4 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(h = status04).count()
    # d.D5 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(h = status05).count()
    # d.D6 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(h = status06).count()
    d.D1 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(status = 1).count()
    d.D2 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(status = 2).count()
    d.D3 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(status = 3).count()
    d.D4 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(status = 4).count()
    d.D5 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(status = 5).count()
    d.D6 = TrackReport00.objects.filter(deptId = d.t100DeptId).filter(status = 6).count()

    print('   ',d.t100DeptId, d.t100DeptName, status01, d.D1)
    print('   ',d.t100DeptId, d.t100DeptName, status02, d.D2)
    print('   ',d.t100DeptId, d.t100DeptName, status03, d.D3)
    print('   ',d.t100DeptId, d.t100DeptName, status04, d.D4)
    print('   ',d.t100DeptId, d.t100DeptName, status05, d.D5)
    print('   ',d.t100DeptId, d.t100DeptName, status06, d.D6)


    d.D0=d.D1+d.D2+d.D3+d.D4+d.D5+d.D6
    d.save()
    print('--- after ---',d.t100DeptId, d.t100DeptName, d.D0,d.D1,d.D2,d.D3,d.D4,d.D5,d.D6)
    print()


# item_list = TrackReport00.objects.filter(deptId = dept_id).order_by('dept','a')
# for item in item_list:
#     print(item)
