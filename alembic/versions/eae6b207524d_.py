"""empty message

Revision ID: eae6b207524d
Revises: 
Create Date: 2023-10-14 15:38:11.337754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eae6b207524d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offer',
    sa.Column('title', sa.TEXT(), nullable=False),
    sa.Column('text', sa.TEXT(), nullable=False),
    sa.Column('city', sa.VARCHAR(length=64), nullable=True),
    sa.Column('slug', sa.VARCHAR(length=64), nullable=False),
    sa.Column('owner', sa.VARCHAR(length=64), nullable=False),
    sa.Column('cost', sa.NUMERIC(), nullable=False),
    sa.Column('is_activated', sa.BOOLEAN(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('user',
    sa.Column('id', sa.CHAR(length=26), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('email', sa.VARCHAR(length=256), nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('offer')
    # ### end Alembic commands ###
