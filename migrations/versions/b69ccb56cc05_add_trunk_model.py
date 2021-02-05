"""add Trunk model

Revision ID: b69ccb56cc05
Revises: bfd6981693c4
Create Date: 2021-02-05 16:50:28.250675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b69ccb56cc05'
down_revision = 'bfd6981693c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(length=20), nullable=True),
    sa.Column('obj', sa.String(length=30), nullable=True),
    sa.Column('trunk_username', sa.String(length=20), nullable=True),
    sa.Column('trunk_password', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('attributes', sa.JSON(), nullable=True),
    sa.Column('lines', sa.Integer(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vats')
    # ### end Alembic commands ###
