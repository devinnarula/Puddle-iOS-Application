from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

items = []

class TodoItems(RequestHandler):
  def get(self):
    self.write({'items': items})


class TodoItem(RequestHandler):
  def post(self,id):
    self.args = json_decode(self.request.body)
    self.write({'message': self.request.body})

def make_app():
  urls = [
    ("/", TodoItems),
    ("/api/item/", TodoItem)
  ]
  return Application(urls, debug=True)
  
if __name__ == '__main__':
  app = make_app()
  app.listen(3000)
  IOLoop.instance().start()