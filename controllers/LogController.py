import falcon
import json

from util import parselogs, slack


class Resource:
    def on_post(self, req, resp):

        text = req.get_param('text').split()

        q = {
                'project': text[0],
                'from': text[1],
                'to': text[2]
        }

        print(q)

        resp.body = 'hello world'
        # query logs here
        logs = parselogs.parse_log_file(q['project'])

        attachments = []
        for log in logs:
            attachments.append(slack.format_log_attachments(log))

        response = {
                "text": "",
                "attachments": attachments
            }

        # dummy lines, to prevent pylint from complaining that we don't use these
        d_message_body
        logs

        resp.status = falcon.HTTP_200
        resp.body = (json.dumps(response))
