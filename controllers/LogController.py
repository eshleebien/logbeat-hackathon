import falcon
import json

from util import slack
from util.datetostr import datestr_to_unix
from util.parselogs import parse_log_file
from util.pivotal import add_story

class Resource:
    def on_post(self, req, resp):

        text = req.get_param('text').split()

        q = {
            'project': text[0],
            'from': datestr_to_unix(text[1]),
            'to': datestr_to_unix(text[2]),
        }

        logs = parse_log_file(q['project'])

        attachments = []
        for k, v in logs.items():
            v['project_name'] = q['project']
            v['timestamp'] = k
            attachments.append(slack.format_log_attachments(v))
        response = {
            "text": "",
            "attachments": attachments
        }
        print response

        resp.status = falcon.HTTP_200
        resp.body = (json.dumps(response))
