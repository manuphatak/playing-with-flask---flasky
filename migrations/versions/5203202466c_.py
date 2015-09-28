"""empty message

Revision ID: 5203202466c
Revises: 19f404c65f
Create Date: 2015-09-27 01:41:22.660351

"""

# revision identifiers, used by Alembic.
revision = '5203202466c'
down_revision = '19f404c65f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###