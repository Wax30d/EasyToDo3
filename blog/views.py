from django.shortcuts import render, get_object_or_404
from .models import Todo


# Rendering home page
def index(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'index.html', {'todos': todos})


# Creating a new
def create_todo(request):
    title = request.POST.get('title')
    todo = Todo.objects.create(title=title)
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})


# Marking completed True
def mark_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})


# Deleting a ...
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})


def update_view_todo(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Todo, id=id)

    # pass the object as instance in form
    form = FirstForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        print("1")
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)
