from django.db import models
from common.models import CommonModel

# 사진
class Photo(CommonModel):

    # 이미지
    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"

# 동영상
class Video(CommonModel):

    # 파일 (vedio file은 따로 없음)
    file = models.FileField()

    # One to one 1:1 관계
    # 한 비디오는 한 활동과만 관계를 가질 수 있음
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    def __str__(self):
        return "Video File"