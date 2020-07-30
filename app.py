from api import API
from middleware import Middleware
app = API()


@app.route('/home/')
def home(request, response):
    response.text = "Hello from the HOME page"


@app.route('/about/')
def about(request, response):
    response.text = "Hello from the ABOUT page"


@app.route("/book/")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Book Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a book"


def handler(req, resp):
    resp.text = "sample"


@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template(
        "index.html",
        context={"name": "Template", "title": "Template body"}
    ).encode()


def custom_exception_handler(request, response, exception_cls):
    response.text = str(exception_cls)


app.add_route("/sample", handler)
app.add_exception_handler(custom_exception_handler)


class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)

    def process_response(self, req, res):
        print("Processing response", req.url)


app.add_middleware(SimpleCustomMiddleware)
