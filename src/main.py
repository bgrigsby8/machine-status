import asyncio
from viam.module.module import Module
try:
    from models.online_status import OnlineStatus
except ModuleNotFoundError:
    # when running as local module with run.sh
    from .models.online_status import OnlineStatus


if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
