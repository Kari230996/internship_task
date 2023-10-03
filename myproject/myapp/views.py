
from rest_framework import generics
from .models import LessonView, Lesson, Product, Access, User
from .serializers import LessonViewSerializer, LessonSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

class LessonViewList(generics.ListAPIView):
    serializer_class = LessonViewSerializer

    def get_queryset(self):
        user = self.request.user  # текущий ползователь
        return LessonView.objects.filter(user=user)
    


class LessonListByProduct(generics.ListAPIView):
    serializer_class = LessonSerializer
    
    def get_queryset(self):
        user = self.request.user # текущий пользователь
        product_id = self.kwargs['product_id'] # получнеие продуст ай-ди из URL
        return Lesson.objects.filter(product__access__user=user, product__id=product_id)
    

@api_view(['GET'])
def product_stats(request):
    products = Product.objects.all()
    stats = []

    for product in products:
        product_info = {}
        product_info['product_name'] = product.product_name
        product_info['total_lessons_viewed'] = LessonView.objects.filter(lesson__product=product).count()
        product_info['total_time_spent'] = LessonView.objects.filter(lesson__product=product).aggregate(total_time=models.Sum('view_time_seconds'))['total_time'] or 0
        product_info['total_users'] = Access.objects.filter(product=product).count()
        product_info['purchase_percentage'] = (Access.objects.filter(product=product).count() / User.objects.count()) * 100 if User.objects.count() > 0 else 0

        stats.append(product_info)

    return Response(stats)
