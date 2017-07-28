import falcon
import json

from util import slack
from util.parselogs import parse_log_file
from util.datetostr import datestr_to_unix


class Resource:
    def on_post(self, req, resp):

        resp.status = falcon.HTTP_200
        resp.body = (json.dumps('hey yo'))
