"""empty message

Revision ID: 9d8020e1ba06
Revises: 
Create Date: 2022-05-08 23:19:19.026313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d8020e1ba06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dealer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('dealer_name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('address', sa.TEXT(), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dealer_name'),
    sa.UniqueConstraint('id')
    )
    op.create_table('car',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('model', sa.VARCHAR(length=255), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('color', sa.VARCHAR(length=10), nullable=True),
    sa.Column('mileage', sa.Integer(), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=8, scale=2), nullable=True),
    sa.Column('dealer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dealer_id'], ['dealer.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    op.drop_table('dealer')
    # ### end Alembic commands ###