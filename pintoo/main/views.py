from django.shortcuts import render, redirect, get_object_or_404



def main(request): 
    context = {} 
    return render(request, 'main/main.html', context) 