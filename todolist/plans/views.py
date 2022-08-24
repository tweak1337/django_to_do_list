import datetime

from django.shortcuts import render, redirect


# Create your views here.
from rest_framework.viewsets import ModelViewSet

from plans.models import ActiveList
from plans.serializers import ListSerializer
from plans.forms import *


def list_page(request):
    if request.method == 'POST':
        if 'delete_deal' in request.POST:
            myid = int(request.POST['delete_deal'])
            ActiveList.objects.get(pk=myid).delete()
        elif 'finish_deal' in request.POST:
            myid = int(request.POST['finish_deal'])
            ActiveList.objects.filter(pk=myid).update(is_done = True)
            ActiveList.objects.filter(pk=myid).update(done_date=datetime.datetime.now())
            done_date = ActiveList.objects.get(pk=myid).done_date
            publish_date = ActiveList.objects.get(pk=myid).publish_date
            days = int((done_date - publish_date).days)
            hours = int((done_date - publish_date).seconds / 60 // 60)
            minutes = int((done_date - publish_date).seconds / 60 % 60)
            seconds = int((done_date - publish_date).seconds % 60 % 60)
            ActiveList.objects.filter(pk=myid).update(days=days)
            ActiveList.objects.filter(pk=myid).update(hours=hours)
            ActiveList.objects.filter(pk=myid).update(minutes=minutes)
            ActiveList.objects.filter(pk=myid).update(seconds=seconds)


    return render(request, 'index.html', {'deals' : ActiveList.objects.all()})


def look_done(request):
    if request.method == 'POST':
        if 'delete_deal' in request.POST:
            myid = int(request.POST['delete_deal'])
            ActiveList.objects.get(pk=myid).delete()

    return render(request, 'done_deal.html', {'deals': ActiveList.objects.all()})


def add_new_deal(request):
    error = ''
    if request.method == 'POST':
        # if 'delete' in request.POST:
        #     print('Ты на верном пути')
        #     # if id:
        #     #     print(id)
        #     #     skill = Skill.objects.get(pk=id).delete()
        # else:
        form = AddDealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Данные заполнены некорректно'


    form = AddDealForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'new_deal.html', data)



class ListViewSet(ModelViewSet):
    queryset = ActiveList.objects.all()
    serializer_class = ListSerializer



    # if request.method == 'POST':
    #     form = AddPostForm(request.POST)
    #     if form.is_valid():
    #         # print(form.cleaned_data)
    #         try:
    #             Women.objects.create(**form.cleaned_data)
    #             return redirect('home')
    #         except:
    #             form.add_error(None, 'Ошибка добавления поста')
    # else:
    #     form = AddPostForm()
    # return render(request,'women/addpage.html', {'form':form,'menu':menu, 'title':'Добавление статьи'})