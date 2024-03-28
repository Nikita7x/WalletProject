"""Wallet and Transaction

Revision ID: 02533577edc3
Revises: 
Create Date: 2024-03-28 13:12:57.854502

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02533577edc3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'wallets',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('label', sa.String(length=255), nullable=False),
        sa.Column('balance', sa.DECIMAL(precision=18, scale=0), nullable=True, default="0"),
    )
    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('txid', sa.String(length=36), nullable=True),
        sa.Column('wallet_id', sa.Integer, sa.ForeignKey('wallets.id'), nullable=False),
        sa.Column('amount', sa.DECIMAL(precision=18, scale=0), nullable=False),
    )

    op.create_index(op.f('idx_wallets_id'), 'wallets', ['id'], unique=False)
    op.create_index(op.f('idx_transactions_id'), 'transactions', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('idx_wallets_id'), table_name='wallets')
    op.drop_table('wallets')
    op.drop_index(op.f('idx_transactions_id'), table_name='transactions')
    op.drop_table('transactions')
