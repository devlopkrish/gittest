from django.shortcuts import render,HttpResponseRedirect
from .models import TodoItems


# Create your views here.
def todoView(request):
    all_todo_items=TodoItems.objects.all()
    return render(request,'todo.html',{"all_items":all_todo_items})


def addToview(request):
    new_item=TodoItems(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteview(request):
    deleteitem=TodoItems(content=request.POST['content'])
    TodoItems.objects.filter(content=deleteitem).delete()
    return HttpResponseRedirect('/todo/')