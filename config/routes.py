from controllers import *

class Router:
    def __init__(self, app):
        app.add_route('/logs', LogController.Resource())
        app.add_route('/tickets', TicketController.Resource())
