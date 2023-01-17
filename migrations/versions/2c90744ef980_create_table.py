"""create table

Revision ID: 2c90744ef980
Revises: 
Create Date: 2023-01-12 14:03:46.456660

"""
import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c90744ef980'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'rule34_images_info',
        sa.Column('image_url', sa.String, nullable=True),
        sa.Column('image_id', sa.ARRAY(sa.String), nullable=True),
        sa.Column('image_copyrights', sa.ARRAY(sa.String), nullable=True),
        sa.Column('image_character_tag', sa.ARRAY(sa.String), nullable=True),
        sa.Column('image_artists', sa.ARRAY(sa.String), nullable=True),
        sa.Column('image_tags', sa.ARRAY(sa.String), nullable=True),
        sa.Column('image_metadata', sa.ARRAY(sa.String), nullable=True),
        sa.Column('image_path', sa.ARRAY(sa.String), nullable=True),
        sa.Column('image_website', sa.String, nullable=True),
        sa.Column('image_rating', sa.Integer, nullable=True),
        sa.Column('published_at', sa.String, nullable=True),
        sa.Column('parsed', sa.Boolean, nullable=True),
        sa.Column('inserted_at', sa.DateTime, default=str(datetime.datetime.now()))
        )
    op.create_primary_key(
        'pk_image_url',
        'rule34_images_info',
        ['image_url',])


def downgrade() -> None:
    op.drop_table("rule34_images_info")
