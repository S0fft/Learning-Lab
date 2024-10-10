from datetime import datetime, timezone

from sqlalchemy import JSON, TIMESTAMP, Boolean, Column, ForeignKey, Integer, MetaData, String, Table

metadata = MetaData()

role = Table(
    'role',

    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON),
)

user = Table(
    'user',

    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('password', String, nullable=True),
    Column('registered_at', TIMESTAMP, default=lambda: datetime.now(timezone.utc)),
    Column('role_id', Integer, ForeignKey('role.id')),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False)
)
