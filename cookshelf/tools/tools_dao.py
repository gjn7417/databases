from flask import jsonify
from sqlalchemy import text

from cookshelf.tools.data_models.tool import Tool


class ToolsDAO:
    def __init__(self, db):
        self.db = db

    def get_all_tools(self):
        sql = text("SELECT * FROM Tools")
        result = self.db.session.execute(sql).fetchall()
        self.db.session.commit()

        return_dict = [Tool.from_db_row(row).__dict__ for row in result]

        return jsonify(return_dict)

    def create_tool(self, tool: Tool):
        sql = text(f"""
                INSERT INTO Tools (name, brand)
                VALUES (:name, :brand)
            """)
        try:
            self.db.session.execute(sql, {'name': tool.name, 'brand': tool.brand})
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def delete_tool(self, tool_id: int):
        sql = text(f"""
                CALL DeleteTool(:id)
            """)
        try:
            self.db.session.execute(sql, {'id': tool_id})
            self.db.session.commit()
            return jsonify({"success": True}), 204
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def update_tool(self, tool: Tool):
        sql = text(f"""
                UPDATE Tools
                SET 
                name = :name, 
                brand = :brand
                WHERE id = :id
            """)
        try:
            self.db.session.execute(sql, {'id': tool.id, 'name': tool.name, 'brand': tool.brand})
            self.db.session.commit()
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def get_tools_by_id(self, tool_ids: list[int]):
        sql = text(f"""
                SELECT * FROM Tools
                WHERE id IN :tool_ids
            """)
        result = self.db.session.execute(sql, {'tool_ids': tool_ids}).fetchall()
        self.db.session.commit()
        return_dict = [Tool.from_db_row(row).__dict__ for row in result]
        return jsonify(return_dict)
