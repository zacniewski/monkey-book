""" Migration #9 class Follow added

Revision ID: 4ef8d58a83a1
Revises: 3c0783aa9966
Create Date: 2014-04-08 21:31:48.615228

"""

# revision identifiers, used by Alembic.
revision = '4ef8d58a83a1'
down_revision = '3c0783aa9966'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['monkeys.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['monkeys.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    op.drop_table('friends')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friends',
    sa.Column('monkey_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('friend_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    mysql_default_charset=u'latin2',
    mysql_engine=u'MyISAM'
    )
    op.drop_table('follows')
    ### end Alembic commands ###
