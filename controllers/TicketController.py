import falcon
import json

from util.pivotal import add_story


class Resource:
    def on_post(self, req, resp):
        payload = json.loads(req.get_param('payload'))
        print payload['actions'][0]["value"]

        actions = payload['actions'][0]

        data = {
            "name": actions["value"],
            "description": actions["value"]
        }
        story = add_story(data)
        resp.status = falcon.HTTP_200
        resp.body = (json.dumps("Ticket successfully created:" + story))
