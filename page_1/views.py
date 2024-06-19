from django.shortcuts import render, redirect
from page_1.models import Register

# Create your views here.
# new code


def home(request):
    query = Register.objects.all()
    context = {"data": query}
    return render(request, "home.html", context)


# table creation and adding data to it
def register(request):
    query = Register.objects.all()
    context = {"data": query}

    if request.method == "POST":
        fullname = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        course = request.POST.get("course")
        # print(fullname, email, age, course)

        query = Register(fullname=fullname, email=email, age=age, course=course)
        query.save()

        print(" :) ")

    return render(request, "home.html", context)


# update function
def update(request, id):
    query = Register.objects.get(id=id)
    context = {"data": query}
    if request.method == "POST":
        fullname = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        course = request.POST.get("course")
        edit = Register.objects.get(id=id)
        edit.fullname = fullname
        edit.email = email
        edit.age = age
        edit.course = course
        edit.save()
        return redirect("/")
    return render(request, "update.html", context)


def deletedata(request, id):
    query = Register.objects.get(id=id)
    query.delete()
    return redirect("/")
