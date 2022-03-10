"""add last few columns to posts table

Revision ID: 9cf24c881583
Revises: d04e7915daaa
Create Date: 2022-03-09 06:34:33.321037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cf24c881583'
down_revision = 'd04e7915daaa'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column(
            'published',
            sa.Boolean(),
            nullable=False,
            server_default='True'
        ),
    )
    op.add_column(
        'posts',
        sa.Column(
            'created_at',
            sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')
        )
    )


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
