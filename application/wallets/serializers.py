from rest_framework import serializers
from application import models


class Wallet:

    class Create(serializers.ModelSerializer):
        class Meta:
            model = models.Wallet
            fields = ('id', 'label', 'balance')

    class Update(serializers.ModelSerializer):
        class Meta:
            model = models.Wallet
            fields = ('label', 'balance')

    class List(serializers.ModelSerializer):
        class Meta:
            model = models.Wallet
            fields = ('id', 'label')
            read_only_fields = ('id', 'label')
