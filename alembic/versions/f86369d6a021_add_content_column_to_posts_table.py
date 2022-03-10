"""add_content_column_to_posts_table

Revision ID: f86369d6a021
Revises: 5eee4bcc7ff0
Create Date: 2022-03-09 05:15:33.770011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f86369d6a021'
down_revision = '5eee4bcc7ff0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
