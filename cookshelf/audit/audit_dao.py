from sqlalchemy import text
from cookshelf.audit.data_models.user_audit import UsersAudit


class AuditDao:
    def __init__(self, db):
        self.db = db

    def get_audit_records(self):
        sql = text("SELECT * FROM Users_Audit")
        result = self.db.session.execute(sql).fetchall()
        self.db.session.commit()

        return [UsersAudit.from_db_row(row) for row in result]
