import os

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from main.forms import CommodityForm
from main.models import Commodity
from pintoo.settings import BASE_DIR, MEDIA_ROOT


def main(request): 
    commoditys = Commodity.objects.all()
    print(commoditys)
    context = {'commoditys':commoditys} 
    return render(request, 'main/main.html', context) 


def commodityCreate(request):
    template = 'commodity/commodityCreate.html'
    if request.method=='GET':
        return render(request, template, {'commodityForm':CommodityForm()})
    # POST
    commodityForm = CommodityForm(request.POST, request.FILES)
    if not commodityForm.is_valid():
        messages.success(request, '請上傳圖檔')
        return render(request, template, {'commodityForm':CommodityForm()})
    commodity = commodityForm.save()
    image1, image2 = False, False
    if commodity.image1:
        image1 = True
    if commodity.image2:
        image2 = True
    if image1:
        origFilename1 = str(commodity.image1).split('/')[-1]
        newFilename1 = str(commodity.id) + '-f1.' + origFilename1.split('.')[-1]
        commodity.image1 = 'commodity/' + newFilename1
        commodity.save()
        command1 = 'mv ' + MEDIA_ROOT + '/commodity/' + origFilename1 + ' ' + MEDIA_ROOT + '/commodity/' + newFilename1
        os.system(command1)
    if  image2:
        origFilename2 = str(commodity.image2).split('/')[-1]
        newFilename2 = str(commodity.id) + '-f2.' + origFilename2.split('.')[-1]
        commodity.image2 = 'commodity/' + newFilename2
        commodity.save()
        command2 = 'mv ' + MEDIA_ROOT + '/commodity/' + origFilename2 + ' ' + MEDIA_ROOT + '/commodity/' + newFilename2
        os.system(command2)
    commodity.save()
    return redirect('main:main')