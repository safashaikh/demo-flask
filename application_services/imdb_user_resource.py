from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service

class IMDBUserResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_by_username_prefix(cls, name_prefix):
        # database, table, column, prefix
        db_service = d_service.RDBService()
        res = db_service.get_by_prefix("imdb_new", "users",
                                      "username", name_prefix)
        return res