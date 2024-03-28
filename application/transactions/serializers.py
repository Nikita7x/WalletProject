from rest_framework import serializers
from application import models


class InlineFields:

    class Wallet(serializers.ModelSerializer):
        class Meta:
            model = models.Wallet
            fields = ('id', 'label',)


class Transaction:

    class Create(serializers.ModelSerializer):
        class Meta:
            model = models.Transaction
            fields = ('id', 'wallet', 'txid', 'amount')
            read_only_fields = ('txid',)

    class Update(serializers.ModelSerializer):
        class Meta:
            model = models.Transaction
            fields = ('id', 'wallet', 'txid', 'amount')
            read_only_fields = ('txid',)

    class List(serializers.ModelSerializer):
        wallet = InlineFields.Wallet(read_only=True)

        class Meta:
            model = models.Transaction
            fields = ('id', 'wallet', 'txid', 'amount')
            read_only_fields = ('txid',)