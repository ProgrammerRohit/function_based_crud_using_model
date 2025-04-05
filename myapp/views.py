from django.shortcuts import render, HttpResponseRedirect
from .models import UserDetails
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    userdetails = UserDetails.objects.all()
    query = ""
    if request.method == "POST":
        if "create" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            UserDetails.objects.create(
                name=name,
                email=email,
                passw=password
            )
            messages.success(request,"Student add successfully")
            return HttpResponseRedirect('/')
        elif "update" in request.POST:
            studentid = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            student = UserDetails.objects.get(id=studentid)
            student.name = name
            student.email = email
            student.passw = password
            student.save()
            messages.success(request,"Student update successfully")
            return HttpResponseRedirect('/')
        elif "delete" in request.POST:
            studentid = request.POST.get('id')
            UserDetails.objects.get(id=studentid).delete()
            messages.success(request,"Student delete successfully")
            return HttpResponseRedirect('/')
        elif "search" in request.POST:
            query = request.POST.get('querySearch')
            userdetails = UserDetails.objects.filter(Q(name__icontains=query) | Q(email__icontains=query) | Q(passw__icontains=query))
            context = {
                'userdetails': userdetails,
                'search_query': query
            }
            return render(request, template_name='index.html', context=context)
    
    context = {
        'userdetails': userdetails,
        'search_query': query
    }
    return render(request, template_name='index.html', context=context)