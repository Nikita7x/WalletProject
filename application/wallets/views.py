from rest_framework import viewsets
from application.wallets import serializers
from application import models


class WalletViewSet(viewsets.ModelViewSet):
    queryset = models.Wallet.objects.all()
    search_fields = ('label',)
    filterset_fields = ('label', 'balance')

    class Meta:
        model = models.Wallet

    def get_serializer_class(self):

        if self.action in ('list',):
            return serializers.Wallet.List
        elif self.action in ('update', 'partial_update'):
            return serializers.Wallet.Update
        else:
            return serializers.Wallet.Create
