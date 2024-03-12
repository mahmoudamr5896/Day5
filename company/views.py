from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .forms import Epm_form ,Team_form
from .models import Epmloyee, TeamLeader



def DisplayEmp(request):
    form = Epm_form()
    if request.method == 'GET':
        return render(request,'company/create_emp.html',{'form':form})
    if request.method == 'POST':
        form = Epm_form(request.POST)
        if form.is_valid():
            team = TeamLeader.objects.filter(pk=request.POST['team'])[0]
            print(team)
            Epmloyee.objects.create(
                    name=request.POST['name'],
                    title=request.POST['title'],
                    salary=request.POST['salary'],
                    team=team
                )
    return HttpResponse('hi Hoda')


# def DisplayTeam(request):
#     form = Team_form()
#     if request.method == 'GET':
#         return render(request,'company/create_team.html',{'form':form})
#     if request.method == 'POST':
#         form = Epm_form(request.POST)
#         if form.is_valid():
#             team = Epmloyee.objects.filter(pk=request.POST['name'])[0]
#             print(team)
#             TeamLeader.objects.create(
#                     name=request.POST['name'],
#                     manager=team
#                 ) 
#     return HttpResponse('hi Hoda')

def DisplayTeam(request):
    form = Team_form()
    if request.method == 'GET':
        return render(request, 'company/create_team.html', {'form': form})
    if request.method == 'POST':
        form = Team_form(request.POST)
        if form.is_valid():
            team = Epmloyee.objects.filter(name=request.POST['name']).first()
            print(team)
            TeamLeader.objects.create(
                    name=request.POST['name'],
                    manger=team  # Corrected 'manger' to 'manager'
                )

    return HttpResponse('hi Hoda')



def show_employees(request):
    employees = Epmloyee.objects.all()
    return render(request, 'company/employees.html', {'employees': employees})












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
