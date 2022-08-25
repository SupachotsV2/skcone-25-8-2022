from asyncio.windows_events import NULL
from atexit import register
from itertools import count
from os import system
from pickle import TRUE
import re
from urllib import response
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
import requests
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import testRequest
from .serializer import TaskSerializers
from django.http import HttpResponse
from django.db.models.functions import Lower
from django.db.models import Count

ms_identity_web = settings.MS_IDENTITY_WEB

# @ms_identity_web.login_required
def index(request,status='w'):
    if request.identity_context_data.authenticated:
        # print('Logged in')
        all_Request = testRequest.objects.all()
        status_wait= all_Request.filter(docStatus__startswith='w')
        # print(results[0]['picture_url'])
        # status = request.POST['status']
        print(status)
        pic_url = url_pic(request)
        return render(request, 'auth/inbox.html', {'all_Request': status_wait,'pic_url' : pic_url,'status':status})
    else:
        print('index page')
        return redirect('sign_in')
def url_pic(request):
        ms_identity_web.acquire_token_silently()
        Username = "SKCone"
        Password = "OneApi2022*"
        token_url ='https://p701apsi01-la02skc.azurewebsites.net/skcapi/token'
        body ={
            "UserName" : Username,
            "Password" : Password
        }
        result1 = requests.post(token_url,json=body).json()
        token = result1['accessToken']
        graph = 'https://graph.microsoft.com/v1.0/me?$select=employeeId'        
        authZ = f'Bearer {ms_identity_web.id_data._access_token}'
        result2 = requests.get(graph, headers={'Authorization': authZ}).json()
        if result2['employeeId'] != None:
            empid = result2['employeeId'] #15856
        else:
            empid = '00000'
        # empid = '15856'
        empid_url = 'https://p701apsi01-la01skc.azurewebsites.net/skcapi/empid/' + empid
        authZ = f'Bearer {token}'
        results = requests.get(empid_url, headers={'Authorization': authZ}).json()
        if type(results) == list:
            pic_url = results[0]['picture_url']
        else:
            pic_url = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'
        return pic_url

# @ms_identity_web.login_required
def token_details(request):
    if request.identity_context_data.authenticated:
        print("this token.html")
        return render(request, 'auth/token.html')
    else:
        print("else token_detail")
        return redirect('/')


@ms_identity_web.login_required
def call_ms_graph(request):
    ms_identity_web.acquire_token_silently()
        # graph = 'https://graph.microsoft.com/v1.0/users'
    graph = 'https://graph.microsoft.com/v1.0/me?$select=id,employeeId,displayName,mail,Department,officeLocation,lastPasswordChangeDateTime'        
    authZ = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graph, headers={'Authorization': authZ}).json()

    print(type(results))
        # print(results)
        # print(results['value'][:1])

        # json_object = json.dumps(results, indent = 4) 
        # print(json_object)

        # trim the results down to 5 and format them.
    if 'value' in results:
        results ['num_results'] = len(results['value'])
        results['value'] = results['value'][:5]
            # print(json.dumps(results['value'], indent = 4))
            # print(dict(results=results))       
    else:
        results['value'] =[{'displayName': 'call-graph-error', 'id': 'call-graph-error'}]
            # print(dict(results=results)) 
            # print(json.dumps(results, indent = 4))
    return render(request, 'auth/call-graph.html', context=dict(results=results))

def login(request):
    if request.identity_context_data.authenticated:
        return redirect('index')
    else:
        print('index page')
        return redirect('sign_in')
# def login(request):
#     if request.identity_context_data.authenticated:
#         return render(request, 'auth/inbox.html')
#     else:
#         print('index page')
#         return render(request, 'login.html')

def history(request):
    if request.identity_context_data.authenticated:
        all_Request = testRequest.objects.all()
        status_test= all_Request.filter(docStatus__startswith='a' ) | all_Request.filter(docStatus__startswith='r' )
        pic_url = url_pic(request)
        return render(request, 'auth/history.html', {'all_Request': status_test,'pic_url' : pic_url})
    else:
        print('index page')
        return redirect('sign_in')

def dashboard(request):
    if request.identity_context_data.authenticated:
        pic_url = url_pic(request)
        return render(request, 'auth/dashboard.html',{'pic_url' : pic_url})
    else:
        return redirect('sign_in')

def contact(request):
    if request.identity_context_data.authenticated:
        pic_url = url_pic(request)
        return render(request, 'auth/contact.html',{'pic_url' : pic_url})
    else:
        return redirect('sign_in')

URL = "http://localhost:8000/api"

@api_view(['GET'])
def apiList(request):
    api_urls = {
        'List': URL +'/testRequest-list',
        'Detail View': URL + '/testRequest-detail/<str:pk>',
        'Update': URL +'/testRequest-update/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def testRequestlist(request):
    tasks = testRequest.objects.all()
    count_task = len(tasks)
    serializer = TaskSerializers(tasks,many=True)
    # print(serializer.data[1])
    for i in range(count_task):
        if serializer.data[i]['system'] == 1 :
            serializer.data[i]['system'] = "myDAS"
        elif serializer.data[i]['system'] == 2:
            serializer.data[i]['system'] = "e-Inventory"
        elif serializer.data[i]['system'] == 3:
            serializer.data[i]['system'] = "e-Procurment"
        if serializer.data[i]['requestDate'] != None:
            date = serializer.data[i]['requestDate'].split("T")
            dd = date[0].split("-")
            time = date[1].split(":")
            day_time = dd[2]+"/" + dd[1]+"/" + dd[0] + " (" + time[0] + ":" + time[1] +")"
            serializer.data[i]['requestDate'] = day_time
        if serializer.data[i]['lastUpdate'] != None:
            date2 = serializer.data[i]['lastUpdate'].split("T")
            dd2 = date2[0].split("-")
            time2 = date2[1].split(":")
            day_time2 = dd2[2]+"/" + dd2[1]+"/" + dd2[0] + " (" + time2[0] + ":" + time2[1] +")"
            serializer.data[i]['lastUpdate'] = day_time2
        else :
            serializer.data[i]['lastUpdate'] = "-"
        if serializer.data[i]['attachment'] == TRUE:
            serializer.data[i]['attachment'] = "✔"
        else:
            serializer.data[i]['attachment'] = "✖"
        serializer.data[i]['approve_func'] = 'function'
    return Response(serializer.data)

@api_view(['GET'])
def testRequestdetail(request,pk):
    tasks = testRequest.objects.get(id=pk)
    serializer = TaskSerializers(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def testRequestupdate(request,pk):
# pk = id 
    task = testRequest.objects.get(id=pk) #เอาช้อมูลของแถวนั้นมา
    # print("request data",request.data)
    # print("Before request data",request.data['docStatus'])
    task.docStatus = request.data['docStatus'] # เปลี่ยนStatus
    # print("After change request data",task.docStatus)
    task.save()
    # serializer = TaskSerializers(instance=task, data=request.data)
    # print("This is task in view.py",task)
    # print("This is serializer in view.py",serializer)
    # if serializer.is_valid():
    #     serializer.save()
    #     print("Update Now")
    return Response()

@api_view(['GET'])
def chartSystems(request):
    all_request = testRequest.objects.all().values('system').annotate(total=Count('system')).order_by('total')
    reQuests_lest = list(all_request)
    # print("This reQuest_list",len(reQuests_lest))
    for i in range(len(reQuests_lest)):
        if reQuests_lest[i]['system']==1:
            reQuests_lest[i]['system'] = 'myDas'
        elif reQuests_lest[i]['system'] == 2 :
            reQuests_lest[i]['system'] = 'e-Inventory'
        elif reQuests_lest[i]['system'] == 3 :
            reQuests_lest[i]['system'] = 'e-Procurement'
    # print("New",reQuests_lest)
    return Response(reQuests_lest)

@api_view(['GET'])
def chartDocstatus(request):
    # all_request = testRequest.objects.all().values('system').annotate(docStatus=Lower('docStatus'),total=Count('docStatus'))
    # all_request_count = testRequest.objects.all()
    request_use = count_request()
    reQuest_lest1 = list(request_use)
    for i in range(len(reQuest_lest1)):
        if reQuest_lest1[i]['system']==1:
            reQuest_lest1[i]['system'] = 'myDas'
        elif reQuest_lest1[i]['system'] == 2 :
            reQuest_lest1[i]['system'] = 'e-Inventory'
        elif reQuest_lest1[i]['system'] == 3 :
            reQuest_lest1[i]['system'] = 'e-Procurement'
    return Response(reQuest_lest1)

def count_request():
    all_request_count = testRequest.objects.all()#get all object value
    all_request_count_test = all_request_count.order_by('system').values('system').distinct()
    for i in range(len(all_request_count_test)):
        all_request_count_test[i]['Approved'] = 0
        all_request_count_test[i]['Reject'] = 0
        all_request_count_test[i]['Wait'] = 0
    
    all_request_count_approve = all_request_count.filter(docStatus__istartswith='a').values('system').annotate(Approved=Count('docStatus'))
    all_request_count_reject = all_request_count.filter(docStatus__istartswith='r').values('system').annotate(Reject=Count('docStatus'))
    all_request_count_wait = all_request_count.filter(docStatus__istartswith='w').values('system').annotate(Wait=Count('docStatus'))
    for i in range(len(all_request_count_test)):
        for j in range(len(all_request_count_approve)):
            if all_request_count_test[i]['system'] == all_request_count_approve[j]['system']:
                all_request_count_test[i]['Approved'] = all_request_count_approve[j]['Approved']
        for j in range(len(all_request_count_reject)):
            if all_request_count_test[i]['system'] == all_request_count_reject[j]['system']:
                all_request_count_test[i]['Reject'] = all_request_count_reject[j]['Reject']
        for j in range(len(all_request_count_wait)):
            if all_request_count_test[i]['system'] == all_request_count_wait[j]['system']:
                all_request_count_test[i]['Wait'] = all_request_count_wait[j]['Wait']
    return all_request_count_test