import logging

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger('console.log')
loggers = {'info': logger.info, 'error': logger.error}


class JsLoggerApi(APIView):
    @staticmethod
    def post(request: Request) -> Response:
        """
        Receives logs from the client, which we re-log with a python logger.
        """
        if 'msg' in request.data and 'type' in request.data:
            loggers[request.data['type']](request.data['msg'])
        else:
            logger.warning('Received bad data.')
        return Response()
