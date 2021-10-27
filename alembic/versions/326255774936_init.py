"""init

Revision ID: 326255774936
Revises: 
Create Date: 2021-10-28 00:19:04.945584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '326255774936'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'address',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('house',sa.String,nullable=False),
        sa.Column('street',sa.String,nullable=False),
        sa.Column('area',sa.String,nullable=False),
        sa.Column('landmark',sa.String,nullable=False),
        sa.Column('village',sa.String,nullable=False),
        sa.Column('pincode',sa.BigInteger,nullable=False),
        sa.Column('subdistrict',sa.String,nullable=False),
        sa.Column('district',sa.String,nullable=False),
        sa.Column('state',sa.String,nullable=False)
    )


def downgrade():
    op.drop_table('address')
