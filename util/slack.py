def get_log_color(log_level):
    colors = {
            'DEBUG': '#45455',
            'INFO': '#34344',
            'ERROR': '#b20000',
    }

    return colors[log_level]


def format_log_attachments(p):
    attachments = [
              {
                 "author_name": p.name,
                 "color": self.get_log_color(p.log_level),
                 "text": p.message,
                 "attachment_type": "default",
                 "ts": p.timestamp,
                 "actions": [
                    {
                       "name": "create",
                       "text": "File a Ticket",
                       "type": "button",
                       "value": p.message,
                    },
                    {
                       "name": "ignore",
                       "text": "Ignore",
                       "type": "button",
                       "style": "danger",
                       "value": "1",
                    }
                 ]
              }
           ]
    return attachments
