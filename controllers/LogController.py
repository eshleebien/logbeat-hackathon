import falcon
import json

from util import slack
from util.parselogs import parse_log_file
from util.datetostr import datestr_to_unix


class Resource:
    def on_post(self, req, resp):

        text = req.get_param('text').split()

        q = {
                'project': text[0],
                'from': datestr_to_unix(text[1]),
                'to': datestr_to_unix(text[2]),
        }

        print(q)

        logs = parse_log_file(q['project'])

        attachments = []
        for log in logs:
            attachments.append(slack.format_log_attachments(log))

        response = {
                "text": "",
                "attachments": attachments
            }

        resp.status = falcon.HTTP_200
        resp.body = (json.dumps(response))
