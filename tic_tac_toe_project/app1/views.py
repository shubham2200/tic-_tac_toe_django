from asyncio import exceptions
from email import message
from django.shortcuts import render ,redirect
from .models import *
from django.http.response import JsonResponse
from django.contrib.messages import *
from django.contrib import messages

# Create your views here.



def home(requets):
    if requets.method == "POST":
        room_name= requets.POST.get('room_name')
        player_1 = requets.POST.get('player1')
        player_2 = requets.POST.get('player2')
        if room_name and player_1 and player_2:
            Room(Room_Name = room_name ,Player_1 = player_1,Player_2 = player_2).save()
    # context = { 'room': x}
    
        context=list(Room.objects.values())
    
            
    return render(requets , 'home.html' ,{'context':context} )


def room(request):
    return render(request , 'room.html')

def check_room(request):
   
    data=''
    if request.method == "POST":
        check = request.POST.get('check')
        print(check)
        print(room)
        for i in check:
            print(i.room_name)
            if i.room_name == check:
                data ='this name is already taken'
            else:
                print('this room is alreaady use create another')
       
    print(data)
    return JsonResponse({'status': 'save'})
    
  