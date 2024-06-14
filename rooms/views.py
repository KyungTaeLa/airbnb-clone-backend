from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Room

def see_all_rooms(request):
    # 모든 room
    rooms = Room.objects.all()
    # all_rooms.html 로 렌더링
    return render(
        request,
        "all_rooms.html",
        {
            "rooms": rooms,
            "title": "Hello! this title comes from django!",
        },
    )

# path("<int:room_id>", views.see_one_room),
# 을 통해 room_id로 url parameter를 전달 받음
def see_one_room(request, room_pk):
    try:
        room = Room.objects.get(pk=room_pk)
        return render(
            request,
            "room_detail.html",
            {
                "room": room,
            },
        )
    except Room.DoesNotExist:
        return render(
            request,
            "room_detail.html",
            {
                "not_found": True,
            },
        )