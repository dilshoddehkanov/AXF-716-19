from loader import dp
from .chat_filters import IsGroup, IsPrivate
from .admins import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(AdminFilter)
