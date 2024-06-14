from django.db import models
from common.models import CommonModel

# Create your models here.
class Room(CommonModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(
        max_length=180,
        default="",
    )
    country = models.CharField(max_length=50, default="korea",)
    city = models.CharField(max_length=80, default="seoul",)
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField(blank=True,)
    address = models.CharField(max_length=250,)
    pet_friendly = models.BooleanField(default=True,)
    kind = models.CharField(max_length=20, choices=RoomKindChoices,)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="rooms",)
    amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms",)
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
    )

    # 이 room 에 해당하는 amenites 갯수
    def total_amenities(self):
        return self.amenities.count()

    def __str__(self) -> str:
        return self.name

    # 이 room 에 해당하는 review 평점
    def rating(self):
        count = self.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0;
            # all() 을 하면 모든것을 가져오므로 필요한 rating만 가져옴
            for review in self.reviews.all().values("rating"):
                # dictionary 타입으로 반환됨
                total_rating += review['rating']
        
        return round(total_rating / count, 2)
    
    



class Amenity(CommonModel):
    
    """ Amenity Definition """

    name = models.CharField(max_length=150,)
    description = models.CharField(max_length=150, null=True,)

    def __str__(self) -> str:
        return self.name
        
    class Meta:
        verbose_name_plural = "Amenities"
