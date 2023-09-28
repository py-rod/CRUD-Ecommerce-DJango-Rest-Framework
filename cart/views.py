from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes

from .serializer import OrderItemSerializer, OrderSerializer, ShippingAddressSerializer

from .models import Order, OrderItem, ShippingAddress
from products.models import Product
from datetime import datetime
# Create your views here.


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_order_item(request):
    user = request.user
    data = request.data
    order_item = data["orderItems"]
    if order_item and len(order_item) == 0:
        return Response({"message": "No order items"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        order = Order.objects.create(
            user=user,
            payment_method=data["payment_method"],
            tax_price=data["tax_price"],
            shipping_price=data["shipping_price"],
            total_price=data["total_price"],
        )

        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city=data['shippingAddress']['city'],
            postal_code=data['shippingAddress']['postal_code'],
            country=data['shippingAddress']['country'],
        )

        for i in order_item:
            product = Product.objects.get(id=i["product"])
            item = OrderItem.objects.create(
                product=product,
                order=order,
                title=product.title,
                qty=i["qty"],
                price=i["price"],
                image=product.image.url,
            )

            product.stock -= item.qty
            product.save()
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_orders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_orders(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_order_to_paid(request, pk):
    order = Order.objects.get(id=pk)
    order.is_paid = True
    order.paid_at = datetime.now()
    order.save()
    return Response({"message": "Order was paid"})


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def update_order_to_delivered(request, pk):
    order = Order.objects.get(id=pk)
    order.is_delivered = True
    order.delivered_at = datetime.now()
    order.save()

    return Response({"message":  "Order was delivered"})
