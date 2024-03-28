from django.urls import path, include
from rest_framework.routers import SimpleRouter

from application.transactions import views as TransactionsViews
from application.wallets import views as WalletsViews

router = SimpleRouter()
router.register(r'transactions', TransactionsViews.TransactionViewSet, basename='transactions')
router.register(r'wallets', WalletsViews.WalletViewSet, basename='wallets')
