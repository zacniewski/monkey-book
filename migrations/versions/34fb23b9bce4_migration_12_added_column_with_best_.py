""" Migration #12 Added column with best friend name

Revision ID: 34fb23b9bce4
Revises: c9adfcdaae6
Create Date: 2014-04-11 00:35:47.493747

"""

# revision identifiers, used by Alembic.
revision = '34fb23b9bce4'
down_revision = 'c9adfcdaae6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('best_friends', sa.Column('best_friend_name', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('best_friends', 'best_friend_name')
    ### end Alembic commands ###
