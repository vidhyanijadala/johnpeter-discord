"""unique

Revision ID: f8d270b5e270
Revises: 5d947b80859f
Create Date: 2020-08-11 16:50:23.205042

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f8d270b5e270'
down_revision = '5d947b80859f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'team', ['team_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'team', type_='unique')
    # ### end Alembic commands ###