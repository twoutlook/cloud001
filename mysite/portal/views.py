from django.shortcuts import render
# from django.shortcuts import get_object_or_404, render
# Create your views here.

def index(request):
    current_user = request.user.username
    context={'current_user':current_user}
    return render(request, 'portal/index.html', context)
