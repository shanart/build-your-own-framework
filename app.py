from api import API

app = API()


@app.route("/home/")
def home(request, response):
    response.text = "This is Home page"


@app.route("/about/")
def about(request, response):
    response.text = "This is About page"


@app.route("/hello/{name}/")
def hello(request, response, name):
    response.text = f"Hello, {name}"


@app.route("/products/{ID:d}/")
def product_by_id(request, response, ID):
    response.text = "This is product number: {}".format(ID)
