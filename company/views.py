from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
# from company.models import Eployee, Team
# from .forms import Epm_form 
# Create your views here.from django.shortcuts import get_object_or_404
# from .models import Eployee, Team


# from .models import Eployee, Team

# def DisplayEmp(request):
#     form = Epm_form()
#     if request.method == 'GET':
#         return render(request,'company/create_emp.html',{'form':form})
#     if request.method == 'POST':
#         form = Epm_form(request.POST)
#         if form.is_valid():
#             team = Team.objects.filter(pk=request.POST('Team'))
#             Eployee.objects.create(
#                     name=request.POST['name'],
#                     title=request.POST['title'],
#                     salary=request.POST['salary'],
#                     Team=team
#                 )
#         return HttpResponse('Team does not exist')
#     return HttpResponse('hi Hoda')

# # def DisplayEmp(request):
    # form = Epm_form()
    # if request.method == 'GET':
    #     return render(request,'company/create_emp.html',{'form':form})
    # if request.method == 'POST':
    #     form = Epm_form(request.POST)
    #     if form.is_valid():
    #         team_name = request.POST['Team']  # Assuming the input name is 'team'
    #         team = Team.objects.get(name=team_name)
    #         Eployee.objects.create(
    #             name=request.POST['name'],
    #             title=request.POST['title'],
    #             salary=request.POST['salary'],
    #             Team=team
    #         )
    #         return render(request,'company/create_emp.html',{'form':form})
           
    # return HttpResponse('hi Hoda')

# def DisplayEmp(request):
    # form = Epm_form()
    # if request.method == 'GET':
    #     return render(request,'company/create_emp.html',{'form':form})
    # if request.method == 'POST':
    #     form = Epm_form(request.POST)
    #     if form.is_valid():
    #         team = Team.objects.filter(name=Team.name)
    #         Eployee.objects.create(
    #             name=request.POST['name'],
    #             title=request.POST['title'],
    #             salary=request.POST['salary'],
    #             Team=team,
    #         )
    #         return render(request,'company/create_emp.html',{'form':form})
    # return HttpResponse('hi Hoda')

# def DisplayEmp(request):
    # form = Epm_form()
    # if request.method == 'GET':
    #     return render(request, 'company/create_emp.html', {'form': form})
    # if request.method == 'POST':
    #     form = Epm_form(request.POST)
    #     if form.is_valid():
    #         team_name = request.POST.get('team')  
    #         team = Team.objects.filter(name=request.POST['Team'])
    #         Eployee.objects.create(
    #             name=request.POST['name'],
    #             title=request.POST['title'],
    #             salary=request.POST['salary'],
    #             Team=team
    #         )
    #         return render(request, 'company/create_emp.html', {'form': form})
    # return HttpResponse('hi Hoda')



# def DisplayEmp(request):
# form = Epm_form()
#     if request.method == 'GET':
#         return render(request,'company/create_emp.html',{'form':form})
#     if request.method== 'POST':
#         form=Epm_form(request.POST)
#         if form.is_valid() :
#              team=Team.objects.filter(pk=request.POST['Team'])
#              Eployee.objects.create(
#             name=request.POST['name'],
#             title=request.POST['title'],
#             salary=request.POST['salary'],
#             Team=team
#             )
#              return render(request,'company/create_emp.html',{'form':form})
           
#     # print(Eployee.objects.all())
#     return HttpResponse('hi Hoda')    