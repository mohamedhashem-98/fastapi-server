"""Second

Revision ID: 19213204ffbc
Revises: 7c42dd0ec704
Create Date: 2022-01-02 11:36:01.639280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19213204ffbc'
down_revision = '7c42dd0ec704'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
