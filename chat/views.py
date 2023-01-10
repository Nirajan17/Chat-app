from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request,room):
    username = request.GET['username']
    room_details = Room.objects.get(room_name = room)
    context = {
        'username':username,
        'room':room,
        'room_details':room_details
    }
    return render(request, 'room.html',context)

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(room_name = room).exists():
        return redirect('/'+room+'/?username='+username) 
    else:
        new_room = Room.objects.create(room_name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    new_message = Message.objects.create(value=message,username=username,room_to_send=room_id)
    return HttpResponse("Message sent succesfully.")

def getmessages(request,room):
    room_details = Room.objects.get(room_name=room)
    messages = Message.objects.filter(room_to_send=room_details.id)
    return JsonResponse({'messages':list(messages.values())})