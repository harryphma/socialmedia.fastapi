"""add content to posts table

Revision ID: a087a86a367c
Revises: 2c0cdaf10714
Create Date: 2024-05-18 15:16:50.862669

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a087a86a367c'
down_revision: Union[str, None] = '2c0cdaf10714'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
