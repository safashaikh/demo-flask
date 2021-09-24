from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service


class IMDBArtistResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_by_name_prefix(cls, name_prefix):
        # database, table, column, prefix
        db_service = d_service.RDBService()
        res = db_service.get_by_prefix("imdb_new", "name_basics",
                                      "primaryName", name_prefix)
        return res