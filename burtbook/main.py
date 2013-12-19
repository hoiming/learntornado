import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path

from tornado.options import define, options
define("port", default=8000, help = "run on the given port",type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                (r"/", RecommendedHandler),
                ]
        settings = dict(
                template_path=os.path.join(os.path.dirname(__file__),"templates"),
                static_path=os.path.join(os.path.dirname(__file__), "static"),
                ui_modules={'Hello': HelloModule,'Book':BookModule},
                )
        super(Application, self).__init__(handlers, **settings)

class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string('modules/book.html', book=book)
class HelloModule(tornado.web.UIModule):
    def render(self):
        return '<h1>Hello, world!</h1>'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
                "index.html",
                page_title = "Burt's Books | Home",
                header_text = "Welcome to Burt's Books!",
                )
class RecommendedHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
                "recommended.html",
                page_title="Burt's Books | Recommended Reading",
                header_text="Recommended Reading",
                books=[
                    {
                        "title":"Programming collective Intelligence",
                        "subtitle":"Building Smart Web 2.0 Applications",
                        "image":"/static/images/collective_intelligence.gif",
                        "author":"Toby Segaran",
                        "date_added":1310248056,
                        "date_released":"August 2007",
                        "isbn":"978-0-596-52932-1",
                        "description":"<p>This is lahblah.</p>"
 }
 ]
                )

           
if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
