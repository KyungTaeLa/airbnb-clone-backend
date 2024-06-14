from django.contrib import admin
from .models import Review

# custom filter
# 지정한 글자가 포함 되어있는 리뷰만 필터링
# admin.SimpleListFilter : title을 필수로 함
class WordFilter(admin.SimpleListFilter):

    # filter 명
    title = "Filter by words!"

    # 
    parameter_name = "word"

    # 필터링 할 항목들 리스트 오버라이딩 함수 (필수)
    # request: 호출한 user 정보
    # model_admin: 이 filter를 사용한 model 정보 
    def lookups(self, request, model_admin):
        return [
            # 검색어, 노출명
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    # 커스텀한 필터링 방식을 거친 후 객체를 반환하는 오버라이딩 함수 (필수)
    # request: 호출한 user 정보 
    # reviews: filtering 대상이 되는 객체
    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        # custom filter 추가
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )