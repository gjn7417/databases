from flask import Blueprint, request

from cookshelf import db
from cookshelf.tools.data_models.tool import Tool
from cookshelf.tools.tools_dao import ToolsDAO

tools = Blueprint('tools', __name__)


@tools.route('/get-all-tools')
def get_all_tools():
    tools_dao = ToolsDAO(db)
    return tools_dao.get_all_tools()


@tools.route('/create-tool', methods=['POST'])
def create_tool():
    data = request.get_json()
    tool = Tool(**data)
    tools_dao = ToolsDAO(db)
    return tools_dao.create_tool(tool=tool)


@tools.route('/delete-tool', methods=['DELETE'])
def delete_tool():
    tool_id = int(request.args.get('id'))
    tools_dao = ToolsDAO(db)
    return tools_dao.delete_tool(tool_id=tool_id)


@tools.route('/update-tool', methods=['PUT'])
def update_tool():
    data = request.get_json()
    tool = Tool(**data)
    tools_dao = ToolsDAO(db)
    return tools_dao.update_tool(tool=tool)
