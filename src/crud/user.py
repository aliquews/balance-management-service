from .base import BaseDBManager


class UserDB(BaseDBManager):
    async def _create(self, **kwargs):
        pass

    async def _read(self):
        pass

    async def _delete(self):
        return await super()._delete()

    async def _update(self, **kwargs):
        return await super()._update(**kwargs)
