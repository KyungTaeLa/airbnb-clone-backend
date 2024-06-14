from django.db import models

# Create your models here.
class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 이게 없으면 Common이라는 Table을 만들게 될거다
    # 공통 Model로 사용하기 위해 추상화를 해준다면 DB는 테이블을 만들지 않는다.
    class Meta:
        abstract = True