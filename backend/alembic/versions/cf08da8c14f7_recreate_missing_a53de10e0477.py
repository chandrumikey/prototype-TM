"""recreate missing a53de10e0477

Revision ID: cf08da8c14f7
Revises: 330e5d111481
Create Date: 2025-09-12 14:15:32.928837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf08da8c14f7'
down_revision: Union[str, Sequence[str], None] = '330e5d111481'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
