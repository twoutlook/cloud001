from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import Count, Min, Sum, Avg

# PART 1 OF 2
# from .models import Materialprice
# from .models import Purchaseorder
# from .models import Receiving
from .models import Flowchart
from .models import Flowchartprocess


# PART 2 OF 2
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
         return redirect('/')
    # 总平均价
    # item_list = Materialprice.objects.order_by('designation', 'id')[:3000]
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'FLOW CHART'}
    return render(request, 'flowchart/index.html', context)

def view_flowchart_list(request):
    if not request.user.is_authenticated:
         return redirect('/')
    # 总平均价
    item_list = Flowchart.objects.order_by('part_name', 'id')[:3000]

    context = {'current_user':request.user,'page_title':'FLOW CHART','item_list':item_list}
    return render(request, 'flowchart/flowchart_list.html', context)



def view_flowchart(request,item_id):
    if not request.user.is_authenticated:
        return redirect('/')
    item=get_object_or_404(Flowchart, pk=item_id)
    itemprocess=Flowchartprocess.objects.filter(flowchart = item_id)

    context = {'current_user':request.user,'page_title':'ONE FLOWCHART','item': item,'itemprocess': itemprocess}
    return render(request, 'flowchart/flowchart.html', context)
