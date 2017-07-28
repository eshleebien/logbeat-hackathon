import falcon
import json
import logging

from util import sqs
from util.parselogs import parse_log_file
from util.datetostr import datestr_to_unix
from config import config


class Resource:
    def on_post(self, req, resp):

        text = req.get_param('text').split();

        q = {
                'project': text[0],
                'from': datestr_to_unix(text[1]),
                'to': datestr_to_unix(text[2]),
        }

        print(q);

        logs = parse_log_file(q['project'])

        resp.body = 'hello world'
        d_message_body = {
            #"text": log.text,
            "text": "test",
            "attachments": [
                {
                    "text": "Todo next",
                    #"fallback": "You are unable to choose a game",
                    #"callback_id": "wopr_game",
                    #"color": "#3AA3E3",
                    "attachment_type": "default",
                    "actions": [
                        {
                            "name": "create",
                            "text": "Create Ticket",
                            "type": "button",
                            "value": "1",
                            "confirm": {
                                "title": "Are you sure?",
                                "text": "Wouldn't you prefer a good game of chess?",
                                "ok_text": "Yes",
                                "dismiss_text": "No"
                            }
                        },
                    ]
                }
            ]
        }

        #dummy lines, to prevent pylint from complaining that we don't use these
        d_message_body
        logs

        resp.status = falcon.HTTP_200
