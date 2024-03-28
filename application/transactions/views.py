from django_filters import rest_framework as filters
from rest_framework import viewsets, response, status
from application.transactions import serializers
from application import models
from django.db import transaction


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    search_fields = ('txid', )
    filterset_fields = ('txid', 'wallet', 'amount')

    class Meta:
        model = models.Transaction

    def get_serializer_class(self):

        if self.action in ('list',):
            return serializers.Transaction.List
        elif self.action in ('update', 'partial_update'):
            return serializers.Transaction.Update
        else:
            return serializers.Transaction.Create

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            wallet = models.Wallet.objects.select_for_update().get(id=request.data['wallet'])

            saved_transaction = serializer.save()

            wallet.balance += saved_transaction.amount
            wallet.save(update_fields=['balance'])

        return response.Response(self.get_serializer(saved_transaction).data, status=status.HTTP_201_CREATED)
