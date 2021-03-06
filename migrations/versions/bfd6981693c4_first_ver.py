"""First ver

Revision ID: bfd6981693c4
Revises: 
Create Date: 2021-02-05 13:55:07.516496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfd6981693c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('simcards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_provider', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('services', sa.JSON(), nullable=True),
    sa.Column('balance', sa.String(length=15), nullable=True),
    sa.Column('rate', sa.String(length=50), nullable=True),
    sa.Column('minute_remain', sa.String(length=10), nullable=True),
    sa.Column('minute_total', sa.String(length=10), nullable=True),
    sa.Column('accured', sa.String(length=15), nullable=True),
    sa.Column('subscr_fee', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('simcards')
    # ### end Alembic commands ###
