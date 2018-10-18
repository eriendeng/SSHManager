from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render, HttpResponse

# Create your views here.
from ssh import models
import paramiko


def create(request):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=request.POST['ip_address'], port=22, username=request.POST['username'],
                    password=request.POST['password'])
        ssh.exec_command("ifconfig")

        models.ssh.objects.create(ip_address=request.POST['ip_address'], username=request.POST['username'],
                                  password=request.POST['password'], introduction=request.POST['introduction'])
        return HttpResponse(
            '{"message":"ok","status":200}'
        )
    except:
        return HttpResponseNotAllowed(permitted_methods="POST", content= '{"message":"fail","status":405}')
    finally:
        ssh.close()


def update(request):
    try:
        obj = models.ssh.objects.get(ip_address=request.POST['ip_address'])
    except:
        return HttpResponseNotAllowed(permitted_methods="POST", content='{"message":"host not found","status":405}')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=request.POST['ip_address'], port=22, username=request.POST['username'],
                    password=request.POST['password'])
        ssh.exec_command("ifconfig")
        obj.ip_address = request.POST['ip_address']
        obj.username = request.POST['username']
        obj.password = request.POST['password']
        obj.introduction = request.POST['introduction']
        obj.save()
        return HttpResponse(
            '{"message":"ok","status":200}'
        )
    except:
        return HttpResponseNotAllowed(permitted_methods="POST", content= '{"message":"fail","status":405}')
    finally:
        ssh.close()