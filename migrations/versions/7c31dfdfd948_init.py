"""init

Revision ID: 7c31dfdfd948
Revises: 
Create Date: 2023-11-02 21:28:27.593991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c31dfdfd948'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=16), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('gender', sa.String(length=8), nullable=True),
    sa.Column('career', sa.String(length=32), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=16), nullable=True),
    sa.Column('password', sa.String(length=512), nullable=True),
    sa.Column('key', sa.String(length=2048), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_users_phone'), ['phone'], unique=True)
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=True)

    op.create_table('avatar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=512), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('author', sa.String(length=128), nullable=True),
    sa.Column('release_year', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book', sa.String(length=512), nullable=True),
    sa.Column('key', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=512), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    op.drop_table('books')
    op.drop_table('avatar')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.drop_index(batch_op.f('ix_users_phone'))
        batch_op.drop_index(batch_op.f('ix_users_email'))

    op.drop_table('users')
    # ### end Alembic commands ###
