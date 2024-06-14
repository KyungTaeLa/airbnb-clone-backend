from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()



# from rest_framework.exceptions import NotFound
# from rest_framework.response import Response
# from rest_framework.status import HTTP_204_NO_CONTENT
# from rest_framework.views import APIView
# from .models import Category
# from .serializers import CategorySerializer

# class Categories(APIView):
#     # 카테고리 전체 조회
#     def get(self, request):
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True,)
#         return Response(serializer.data)

#     # 카테고리 생성
#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             new_category = serializer.save()
#             return Response(
#                 CategorySerializer(new_category).data,
#             )
#         else:
#             return Response(serializer.errors)

# class CategoryDetail(APIView):
#     # 카테고리 단건 조회 쿼리
#     def get_object(self,pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise NotFound

#     # 카테고리 단건 조회
#     def get(slef, request, pk):
        
#         serializer = CategorySerializer(slef.get_object(pk))
#         print(serializer)
#         return Response(serializer.data)

#     # 카테고리 수정
#     def post(slef, request, pk):

#         # 원본 instance와 변경할 category 데이터가 있으면
#         # 반환받은 serializer는 save 시 create 함수를 호출하지 않고 update 함수를 호출한다
#         serializer = CategorySerializer(
#             slef.get_object(pk),
#             data=request.data,
#             partial=True,
#         )
#         if serializer.is_valid():
#             updated_category = serializer.save()
#             return Response(CategorySerializer(updated_category).data)
#         else:
#             return Response(serializer.errors)

#     # 카테고리 삭제
#     def delete(slef, request, pk):
#         slef.get_object(pk).delete()
#         return Response(status=HTTP_204_NO_CONTENT)
