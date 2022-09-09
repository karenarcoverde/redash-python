from .base import BaseService
from .mixins import CommonMixin, NameMixin, PrintMixin


class QSnipsService(CommonMixin, NameMixin, PrintMixin):
    def __init__(self, base: BaseService) -> None:
        CommonMixin.__init__(self, base)
        self.endpoint = "/api/query_snippets"