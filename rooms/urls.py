from django.urls import path
from . import views
urlpatterns = [
    path("", views.see_all_rooms),
    # rooms/정수형 => room_pk 로 변수명 할당
    path("<int:room_pk>", views.see_one_room),
] 
