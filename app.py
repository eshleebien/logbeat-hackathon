import falcon

from threads import worker
from config import routes, config


app = falcon.API()
app.req_options.auto_parse_form_urlencoded = True
routes.Router(app)

print(' * ' + config.APP_NAME + ' Initialized')

# worker_thread = worker.WorkerThread()
# worker_thread.start()
