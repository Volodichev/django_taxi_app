from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveUpdateAPIView

from .models import Car
from .serializers import CarsListSerializer, CarSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly  # , IsOwnerOrReadOnly

# from rest_framework.settings import api_settings
# from rest_framework_csv import renderers as r
#
#
# class MyView(APIView):
#     renderer_classes = (r.CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
#     ...


class CarsListView(APIView):
    """Вывод списка ТС"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        cars = Car.objects.all()
        serializer = CarsListSerializer(cars, many=True)
        return Response({"cars": serializer.data})


class CarView(APIView):
    """Работа с данными ТС"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        car = Car.objects.get(id=pk)
        serializer = CarSerializer(car)
        return Response({"car": serializer.data})


class CarCreateView(CreateAPIView):
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly,)

    # def post(self, request):
    #     car = request.data.get('cars')
    #     serializer = CarSerializer(data=car)
    #     if serializer.is_valid(raise_exception=True):
    #         car_saved = serializer.save()
    #
    #     return Response({"success": "Cat '{}' created successfully".format(car_saved.title)})
