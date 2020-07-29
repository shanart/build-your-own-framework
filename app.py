from api import API

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

app.add_route("/sample", handler)