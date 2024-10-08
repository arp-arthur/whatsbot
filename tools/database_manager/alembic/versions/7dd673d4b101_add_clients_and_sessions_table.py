"""

Revision ID: 7dd673d4b101
Revises: a3a6902af95d
Create Date: 2024-08-05 18:54:06.098823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '7dd673d4b101'
down_revision: Union[str, None] = 'a3a6902af95d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('message_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('message_text', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.create_table('client_sessions',
    sa.Column('client_session_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('interaction_date', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('is_last_message', sa.Boolean(), server_default='TRUE', nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.client_id'], ),
    sa.ForeignKeyConstraint(['message_id'], ['messages.message_id'], ),
    sa.PrimaryKeyConstraint('client_session_id')
    )
    op.add_column('clients', sa.Column('reference_date', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False))
    op.alter_column('clients', 'name',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.drop_column('clients', 'reference_data')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients', sa.Column('reference_data', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    op.alter_column('clients', 'name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    op.drop_column('clients', 'reference_date')
    op.drop_table('client_sessions')
    op.drop_table('messages')
    # ### end Alembic commands ###
