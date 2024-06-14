from django.contrib import admin
from .models import Room, Amenity

# model_admin: RoomAdmin class 정보를 가지고 있음 
# request: 호출한 user의 정보를 가지고 있음
# rooms: action에서 선택한 records의 정보를 가지고 있음 
@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms:
        # 선택한 room 의 price 초기화
        room.price = 0
        # 저장
        room.save();


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # action
    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    search_fields = (
		# 기본 = contains
        "name",
        # startwith
        "^price",
        # = : 같은 값, room owner 의 이름으로 완전 일치
        "=owner__username",
    )



@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
