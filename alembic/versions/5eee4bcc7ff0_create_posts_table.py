"""create_posts_table


Revision ID: 5eee4bcc7ff0
Revises: 
Create Date: 2022-03-08 20:58:49.905434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5eee4bcc7ff0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )


def downgrade():
    op.drop_table('posts')
