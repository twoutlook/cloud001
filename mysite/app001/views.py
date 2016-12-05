from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
# from django.shortcuts import render

from django.conf import settings
from django.shortcuts import redirect
from django.db.models import Count, Avg, Sum

# from .models import Customer
from .models import Item000
from .models import Item001
from .models import Item002v2 #TODO HOW TO MIGRATE old table
from .models import Item003
from .models import Item003v2

from .models import Item004 # version 2

from .models import Item005
from .models import Item006 #2016-08-26 按胡課要求同富甲方式實施
from .models import Item007
from .models import Item008
from .models import Item009
from .models import Item010
# from .models import T01

# 2016/09/20
from .models import Item011

from .models import Item012

from .models import Flowchart
from .models import Flowchartprocess






# V2
# from .models import Item004v2

from .models import Spec
from .models import Cust

# from ipware.ip import get_ip

# def index(request):
#     return HttpResponse("Hello, world. 欠料")


# def index(request):
#     if not request.user.is_authenticated:
#         # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
#         #return redirect('../admin')
#         context = {'page_title':'xxx','customer_list': {}}
#         return render(request, 'app001/index.html', context)

#     customer_list = Customer.objects.order_by('field1')[:100]
#     context = {'page_title':'yyy','customer_list': customer_list}
#     return render(request, 'app001/index.html', context)

def item000(request):
    if not request.user.is_authenticated:
        #  return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        context = {'page_title':'您現在訪問 APP001，但是還沒有登入','item_list': {}}
        return render(request, 'app001/index.html', context)

    item_list = Item000.objects.order_by('field1')[:100]
    context = {'current_user':request.user,'page_title':'APP001-雲端佈告欄','item_list': item_list}
    print("by Mark: to debug here...")
    # ip = get_ip(request)
    # if ip is not None:
    #     print("we have an IP address for user: "+ip)
    # else:
    #     print("we don't have an IP address for user")
    return render(request, 'app001/index.html', context)

def p1(request):
    if not request.user.is_authenticated:
        #  return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        context = {'page_title':'您現在訪問 APP001，但是還沒有登入','item_list': {}}
        return render(request, 'app001/index.html', context)



    item_list = Flowchartprocess.objects.all()



    context = {'current_user':request.user,'page_title':'APP001-雲端佈告欄','item_list': item_list}
    print("by Mark: to debug here...")
    # ip = get_ip(request)
    # if ip is not None:
    #     print("we have an IP address for user: "+ip)
    # else:
    #     print("we don't have an IP address for user")
    return render(request, 'app001/p1.html', context)


def index_bootstrap(request):
    if not request.user.is_authenticated:
        #  return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        context = {'page_title':'APP001-雲端佈告欄 (手機版)','item_list': {}}
        return render(request, 'app001/index_bootstrap.html', context)

    item_list = Item000.objects.order_by('field1')[:100]
    context = {'current_user':request.user,'page_title':'APP001-雲端佈告欄 (手機版)','item_list': item_list}
    print("by Mark: to debug here...")
    # ip = get_ip(request)
    # if ip is not None:
    #     print("we have an IP address for user: "+ip)
    # else:
    #     print("we don't have an IP address for user")
    return render(request, 'app001/index_bootstrap.html', context)

def help(request):
    # item_list = Spec.objects.order_by('field1')[:100]
    context = {'page_title':'App001 Help','item_list': [],'current_user':request.user}
    return render(request, 'app001/help.html', context)



def spec(request):
    if not request.user.is_authenticated:
         return redirect('../../admin/login/?next=/app001/spec/')

    item_list = Spec.objects.order_by('field1')[:100]
    context = {'page_title':'App001 SPEC','item_list': item_list,'current_user':request.user}
    return render(request, 'app001/spec.html', context)

def cust(request):
    # if not request.user.is_authenticated:
    #     # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    #     #return redirect('../admin')
    #     context = {'page_title':'Spec','item_list': {}}
    #     return render(request, 'app001/spec.html', context)

    item_list = Cust.objects.order_by('field1')[:100]
    context = {'page_title':'App001 Cust','item_list': item_list}
    return render(request, 'app001/cust.html', context)

# def item001obj(request):
#     if not request.user.is_authenticated:
#         context = {'page_title':'item001-obj-富鈦-壓鑄機','item_list': {}}
#         return render(request, 'app001/item001.html', context)

#     # item_list = Item001.objects.order_by('field1')[:100]
#     # context = {'page_title':'item001-obj-富鈦-壓鑄機','item_list': item_list}
#     context = {'page_title':'item001-obj-富鈦-壓鑄機','item_list': {}}
#     return render(request, 'app001/item001.html', context)


def item001detail(request, item001_id):
    if not request.user.is_authenticated:
         return redirect('/')

    item001=get_object_or_404(Item001, pk=item001_id)
    context = {'current_user':request.user,'page_title':'item001-富鈦-壓鑄機 編號︰','item001_id': item001_id,'item001': item001,'item001_upper': '/app001/item001/'}
    return render(request, 'app001/item001detail.html', context)

def item003detail(request, item001_id):
    if not request.user.is_authenticated:
         return redirect('/')

    item001=get_object_or_404(Item003, pk=item001_id)
    context = {'current_user':request.user,'page_title':'ITEM003-富甲-壓鑄機-單機 ','item001_id': item001_id,'item001': item001,'item001_upper': '/app001/item003/'}
    return render(request, 'app001/item001detail.html', context)


def item003v2detail(request,item001_id):
    if not request.user.is_authenticated:
        return redirect('/')
    item001=get_object_or_404(Item003v2, pk=item001_id)
    context = {'current_user':request.user,'page_title':'ITEM003-富甲-壓鑄機-單機','item001': item001,'item001_upper': '/app001/item003/'}
    return render(request, 'app001/item003v2detail.html', context)



def item001(request):
    # if not request.user.is_authenticated:
    #     context = {'page_title':'item001-富鈦-壓鑄機 編號︰','item_list': {}}
    #     return render(request, 'app001/item001.html', context)
    if not request.user.is_authenticated:
         return redirect('/')
        #  return redirect('../../admin/login/?next=/app001')

    item_list = Item001.objects.order_by('field1')[:100]
    context = {'current_user':request.user,'page_title':'ITEM001-富鈦-壓鑄機','item_list': item_list}
    return render(request, 'app001/item001.html', context)

def item002(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item002v2.objects.order_by('id')[:400]
    context = {'current_user':request.user,'page_title':'ITEM002-富鈦-欠料-(B)','item_list': item_list}
    return render(request, 'app001/item002.html', context)


# just use item001.html template
def item003(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item003.objects.order_by('field1')[:100]
    context = {'page_title':'ITEM003-富甲-壓鑄機','item_list': item_list}
    return render(request, 'app001/item001.html', context)


def item003v2(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item003v2.objects.order_by('headera')[:100]
    context = {'page_title':'ITEM003-富甲-壓鑄機','item_list': item_list}
    return render(request, 'app001/item003v2.html', context)

def item007(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item007.objects.order_by('headera')[:100]
    context = {'page_title':'ITEM007-富甲-壓鑄機','item_list': item_list}
    return render(request, 'app001/item007.html', context)

def item008(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item008.objects.order_by('headera')[:100]
    context = {'page_title':'ITEM008-富甲-壓鑄機','item_list': item_list}
    return render(request, 'app001/item008.html', context)

# 2016-11-24
# def t01(request):
#     if not request.user.is_authenticated:
#          return redirect('/')
#
#     item_list = T01.objects.order_by('id')[:3000]
#     context = {'page_title':'T01- 工序','item_list': item_list}
#     return render(request, 'app001/t01.html', context)



def item009(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item009.objects.order_by('headera')[:100]
    context = {'page_title':'ITEM009-富钛-壓鑄機','item_list': item_list}
    return render(request, 'app001/item008.html', context)



def item007detail(request,item001_id):
    if not request.user.is_authenticated:
        return redirect('/')
    item001=get_object_or_404(Item007, pk=item001_id)
    context = {'current_user':request.user,'page_title':'ITEM007-富甲-壓鑄機-單機','item001': item001,'item001_upper': '/app001/item003/'}
    return render(request, 'app001/item007detail.html', context)

def item008detail(request,item001_id):
    if not request.user.is_authenticated:
        return redirect('/')
    data=get_object_or_404(Item008, pk=item001_id)
    context = {'current_user':request.user,'page_title':'ITEM008-富甲-壓鑄機-單機','data': data,'item001_upper': '/app001/item003/'}
    return render(request, 'app001/item008detail.html', context)

def item009detail(request,item001_id):
    if not request.user.is_authenticated:
        return redirect('/')
    item001=get_object_or_404(Item009, pk=item001_id)
    context = {'current_user':request.user,'page_title':'ITEM009-富鈦-壓鑄機-單機','item001': item001,'item001_upper': '/app001/item003/'}
    return render(request, 'app001/item008detail.html', context)

def item008blueprint(request):
    if not request.user.is_authenticated:
        return redirect('/')
    # item001=get_object_or_404(Item009, pk=item001_id)
    context = {'current_user':request.user,'page_title':'ITEM008-富甲-壓鑄機-(需求說明)','item001_upper': '/app001/item003/'}
    return render(request, 'app001/item008blueprint.html', context)

def item009blueprint(request):
    if not request.user.is_authenticated:
        return redirect('/')
    # item001=get_object_or_404(Item009, pk=item001_id)
    context = {'current_user':request.user,'page_title':'ITEM009-富鈦-壓鑄機-(需求說明)','item001_upper': '/app001/item003/'}
    return render(request, 'app001/item009blueprint.html', context)



def item004(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item004.objects.order_by('id')[:400]
    context = {'current_user':request.user,'page_title':'ITEM004-富甲-欠料(B)','item_list': item_list}
    # return render(request, 'app001/item004.html', context)
    # 201-08-24 11:00, by Mark, 改用 item002.html
    # 201-08-24 14:56, by Mark, 改用 item004.html, Derrick 反應富鈦和富甲不完全相同
    return render(request, 'app001/item004.html', context)

def item004a(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item004.objects.order_by('id')[:400]
    context = {'current_user':request.user,'page_title':'ITEM004-富甲-欠料-(A)','item_list': item_list}

    # 201-08-24 11:00, by Mark, 改用 item002a.html
    # 201-08-24 14:56, by Mark, 改用 item004a.html, Derrick 反應富鈦和富甲不完全相同
    return render(request, 'app001/item004a.html', context)


def item002a(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item002v2.objects.order_by('id')[:400]
    context = {'current_user':request.user,'page_title':'ITEM002-富鈦-欠料-(A)','item_list': item_list}
    return render(request, 'app001/item002a.html', context)



# a standard view to logout
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    #return redirect('/admin/login/?next=/app001')
    # 2016-08-24
    # When log out, got to root
    return redirect('/')

# 201-08-25 13:00, by Mark, 客戶|產品 兩層分組
def item004c(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item004.objects.order_by('f01','f03')[:400]
    context = {'current_user':request.user,'page_title':'ITEM004-富甲-欠料-(打樣一)','item_list': item_list}
    return render(request, 'app001/item004c.html', context)
def item004d(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item004.objects.order_by('f01','f03')[:400]
    context = {'current_user':request.user,'page_title':'ITEM004-富甲-欠料-(打樣二)','item_list': item_list}
    return render(request, 'app001/item004d.html', context)

def item005(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item005.objects.order_by('f01','f03','id')[:400]
    context = {'current_user':request.user,'page_title':'ITEM005-富甲-欠料明细','item_list': item_list}
    return render(request, 'app001/item005.html', context)

def item006(request):
    if not request.user.is_authenticated:
         return redirect('/')

    item_list = Item006.objects.order_by('f01','f03','id')[:400]
    context = {'current_user':request.user,'page_title':'ITEM006-富鈦-欠料明细','item_list': item_list}
    #使用ITEM005  template
    return render(request, 'app001/item005.html', context)


def item010(request):
    if not request.user.is_authenticated:
         return redirect('/')

    # total = 0
    # for org in orgs:
    # orders = orgs[org]
    # subtotal = sum(order['qty']*order['price'] for order in orders)
    # total += subtotal
    # orgs[org] = {'orders': orders, 'subtotal': subtotal}


    # Transaction.objects.values('order_id').annotate(total=Sum('value'))
    subtotal=Item010.objects.values('f01').annotate(sumf07=Sum('f07'),sumf10=Sum('f10'))


    item_list = Item010.objects.order_by('f01','f02','f03','f04')[:400]
    context = {'current_user':request.user,'page_title':'ITEM010-富甲-压铸在制订单','item_list': item_list,'subtotal':subtotal}
    #使用ITEM005  template
    return render(request, 'app001/item010.html', context)

# share same template but different model
def item011(request):
    if not request.user.is_authenticated:
         return redirect('/')

    subtotal=Item011.objects.values('f01').annotate(sumf07=Sum('f07'),sumf10=Sum('f10'))


    item_list = Item011.objects.order_by('f01','f02','f03','f04')[:400]
    context = {'current_user':request.user,'page_title':'ITEM011-富鈦-压铸在制订单','item_list': item_list,'subtotal':subtotal}
    #使用ITEM005  template
    return render(request, 'app001/item010.html', context)


def item012(request):
    if not request.user.is_authenticated:
         return redirect('/')

    # f04 机台吨位
    # f07 f08 f09 f10 订单数量	已生产数量	未生产数量 	合计工时(小时）
    subtotal=Item012.objects.values('f04').annotate(sumf08=Sum('f08'),sumf09=Sum('f09'),sumf10=Sum('f10'),sumf11=Sum('f11'),sumf11v2=Sum('f11')/24)


    item_list = Item012.objects.order_by('f04','f02','f01')[:400]
    context = {'current_user':request.user,'page_title':'ITEM012-富鈦-压铸在制订单','item_list': item_list,'subtotal':subtotal}
    #使用ITEM005  template
    return render(request, 'app001/item012.html', context)

def item013(request):
    if not request.user.is_authenticated:
         return redirect('/')

    # f04 机台吨位
    # f07 f08 f09 f10 订单数量	已生产数量	未生产数量 	合计工时(小时）
    subtotal=Item012.objects.values('f02').annotate(sumf08=Sum('f08'),sumf09=Sum('f09'),sumf10=Sum('f10'),sumf11=Sum('f11'),sumf11v2=Sum('f11')/24)


    item_list = Item012.objects.order_by('f02','f04','f01')[:400]
    context = {'current_user':request.user,'page_title':'ITEM013-富鈦-压铸在制订单(物料代码)','item_list': item_list,'subtotal':subtotal}
    #使用ITEM005  template
    return render(request, 'app001/item013.html', context)

def item014(request):
    if not request.user.is_authenticated:
         return redirect('/')

    # f04 机台吨位
    # f07 f08 f09 f10 订单数量	已生产数量	未生产数量 	合计工时(小时）
    subtotal=Item012.objects.values('f03').annotate(sumf08=Sum('f08'),sumf09=Sum('f09'),sumf10=Sum('f10'),sumf11=Sum('f11'),sumf11v2=Sum('f11')/24)


    item_list = Item012.objects.order_by('f03','f02','f04','f01')[:400]
    context = {'current_user':request.user,'page_title':'ITEM014-富鈦-压铸在制订单(物料说明)','item_list': item_list,'subtotal':subtotal}
    #使用ITEM005  template
    return render(request, 'app001/item014.html', context)

def dev001(request):
    if not request.user.is_authenticated:
         return redirect('/')

    # item_list = Item006.objects.order_by('f01','f03','id')[:400]

    d01=['---','正常','磨損','無法修復']
    d02=['---','正常','磨損','裂縫','磨損、裂縫']
    d03=['---','正常','平面變型','無法修復']
    d04=['---','正常','平面變型','無法修復']
    d05=['---','正常','合模缸漏油','合模缸螺旋斷裂','合模活塞磨損','無法修復']
    d06=['---','正常','磨損','無法修復']
    d07=['---','正常','磨損','斷裂','無法修復']
    d08=['---','正常','開關損壞','線路不通','無法修復']
    d09=['---','正常','無壓力','線路不通','壓射缸漏油','射杆彎曲']
    d10=['---','正常','斷線','短路','鏈條斷','編碼器異常','銅套磨損']
    d11=['---','正常','磨損','斷裂','接頭滑絲']
    d12=['---','正常','破損','堵塞']
    d13=['---','正常','油品變質']
    d14=['---','正常','磨損','軸心斷裂']
    d15=['---','正常','線路不通','閥心斷裂']
    d16=['---','正常','管道不通','管道斷裂','泵心磨損']
    d17=['---','正常','鋼瓶裂縫','壓力過高','壓力過低']
    d18=['---','正常','線路不通','短路']
    d19=['---','正常','霧化器損壞','線路不通','緩衝彈簧斷裂']
    d20=['---','正常','開關損壞','軸承磨損','緩衝器斷裂','線路不通','編碼器異常']
    d21=['---','正常','尺寸NG','模崩','模芯斷','重覆修模','待修模']
        # CHOICE03=(
        #     ('---','---'),
        #     ('正常','正常'),
        #     ('平面變型','平面變型'),
        #     ('裂縫 ','裂縫'),
        #     ('無法修復','無法修復'),
        # )

    dlist=[d01,d02,d03,d04,d05,d06,d07,d08,d09,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21]


    item_list = {"input":dlist,"result":"將生成的代碼在這裡顯示"}

    context = {'current_user':request.user,'page_title':'DEV001-生成代碼-壓鑄機備註說明','item_list': item_list}
    #使用ITEM005  template
    return render(request, 'app001/dev001.html', context)
def view_flowchart_list(request):
    if not request.user.is_authenticated:
         return redirect('/')
    # 总平均价
    item_list = Flowchart.objects.order_by('part_name', 'id')[:3000]

    context = {'current_user':request.user,'page_title':'FLOW CHART','item_list':item_list}
    return render(request, 'app001/flowchart_list.html', context)



def view_flowchart(request,item_id):
    if not request.user.is_authenticated:
        return redirect('/')
    item=get_object_or_404(Flowchart, pk=item_id)
    itemprocess=Flowchartprocess.objects.filter(flowchart = item_id)

    context = {'current_user':request.user,'page_title':'ONE FLOWCHART','item': item,'itemprocess': itemprocess}
    return render(request, 'app001/flowchart.html', context)

def Flowchartprocess2(request):
    if not request.user.is_authenticated:
        return redirect('/')
    # item=get_object_or_404(Flowchart, pk=item_id)
    # itemprocess=Flowchartprocess.objects.filter(flowchart = item_id)
    itemprocess=Flowchartprocess.objects.order_by('b','c','d')


    context = {'current_user':request.user,'page_title':'ONE FLOWCHART','itemprocess': itemprocess}
    return render(request, 'app001/flowchart2.html', context)
def Flowchartprocess3(request):
    if not request.user.is_authenticated:
        return redirect('/')
    # item=get_object_or_404(Flowchart, pk=item_id)
    # itemprocess=Flowchartprocess.objects.filter(flowchart = item_id)
    # list1=Flowchartprocess.objects.order_by('b')
    # list2=Flowchartprocess.objects.order_by('b','c')
    # list3=Flowchartprocess.objects.order_by('b,'c','d')

    sub1=Flowchartprocess.objects.values('b').annotate(cnt=Count('b'))
    sub2=Flowchartprocess.objects.values('b','c').annotate(cnt=Count('b'))
    sub3=Flowchartprocess.objects.values('b','c','d').annotate(cnt=Count('b'))


    context = {'current_user':request.user,'page_title':'GROUP BY','sub1': sub1,'sub2': sub2,'sub3': sub3}
    return render(request, 'app001/flowchartprocess3.html', context)
