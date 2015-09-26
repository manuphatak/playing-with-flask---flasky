"""empty message

Revision ID: 29c2ca0e29f
Revises: 16c81c2cd9b
Create Date: 2015-09-26 18:37:42.397328

"""

# revision identifiers, used by Alembic.
revision = '29c2ca0e29f'
down_revision = '16c81c2cd9b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###