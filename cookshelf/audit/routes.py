from flask import jsonify, Blueprint

from cookshelf import db
from cookshelf.audit.audit_dao import AuditDao

audit = Blueprint('audit', __name__)


@audit.route('/audit_records', methods=['GET'])
def get_audit_records():
    audit_dao = AuditDao(db)
    audit_records = audit_dao.get_audit_records()
    return jsonify([record.to_dict() for record in audit_records])
