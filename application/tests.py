from django.test import TestCase
from application import models
from rest_framework.test import APIClient
from application import transactions


class TestTransactions(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.view = transactions.views.TransactionViewSet()

        self.wallet = models.Wallet.objects.create(balance=1000, label='auto_created1')

        self.transaction = models.Transaction.objects.create(
            wallet=self.wallet,
            amount=200
        )

    def test_transaction_create(self):
        data = {
            'wallet': self.wallet.id,
            'amount': 500,
        }

        response = self.client.post('/api/transactions/', data)

        self.assertEqual(response.status_code, 201)

    def test_transaction_retrieve(self):
        response = self.client.get(f'/api/transactions/{self.transaction.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.transaction.id)

    def test_transaction_list(self):
        response = self.client.get('/api/transactions/')

        self.assertEqual(response.status_code, 200)

    def test_transaction_update(self):
        data = {
            'amount': 400,
        }

        response = self.client.put(f'/api/transactions/{self.transaction.id}/', data)


class TestWallets(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.wallet = models.Wallet.objects.create(balance=1000, label='auto_created')

    def test_wallet_retrieve(self):
        response = self.client.get(f'/api/wallets/{self.wallet.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.wallet.id)
        self.assertEqual(response.data['balance'],
                         str(self.wallet.balance))

    def test_wallet_create(self):
        data = {
            'balance': 500,
            'label': 'test-created'
        }

        response = self.client.post('/api/wallets/', data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['balance'], str(data['balance']))

    def test_wallet_update(self):
        data = {
            "label": "updated label",
            'balance': 3000
        }

        response = self.client.put(f'/api/wallets/{self.wallet.id}/', data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['balance'], str(data['balance']))

    def test_wallet_partial_update(self):
        data = {
            'balance': 2000
        }

        response = self.client.patch(f'/api/wallets/{self.wallet.id}/', data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['balance'], str(data['balance']))

    def test_wallet_delete(self):
        response = self.client.delete(f'/api/wallets/{self.wallet.id}/')

        self.assertEqual(response.status_code, 204)
        self.assertEqual(models.Wallet.objects.filter(id=self.wallet.id).exists(), False)