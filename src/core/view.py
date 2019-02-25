from flask import jsonify, Response
from flask_restful import Resource


class BaseView(Resource):

    def render_json_response(self,
                             status_code: int = 200,
                             res: str = '', **kwargs) -> tuple:
        response = {'res': res} if res else dict()
        response.update(kwargs)
        return response, status_code

    def render_template_response(self,
                                 template_name: str,
                                 mimetype: str = 'text/html',
                                 **kwargs) -> Response:
        return Response(render_template(template_name), mimetype=mimetype)
