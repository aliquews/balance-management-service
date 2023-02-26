from sqlalchemy import update, delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from src.db.database import get_async_session


class BaseDBManager:
    '''
    Simple CRUD DB manager for any structures
    '''

    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        self.session = session

    async def _create(self, **kwargs):
        pass

    async def _read(self):
        pass

    async def _update(self, **kwargs):
        pass

    async def _delete(self):
        pass
