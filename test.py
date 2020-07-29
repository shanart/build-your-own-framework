import pytest


def test_basic_route_adding(api):
    @api.route('/home')
    def home(req, resp):
        resp.text = 'YOLO'


def test_route_overlap_throws_exception(api):
    @api.route('/home')
    def home(req, resp):
        resp.text = 'Test'

    with pytest.raises(AssertionError):
        @api.route('/home')
        def home2(req, resp):
            resp.text = 'Test'


def test_client_can_send_requests(api, client):
    response_text = "this is test message"

    @api.route('/test')
    def test(req, resp):
        resp.text = response_text

    assert client.get('http://testserver/test').text == response_text


def test_parametrized_route(api, client):
    @api.route("/{name}")
    def test(req, resp, name):
        resp.text = f"test {name}"

    assert client.get('http://testserver/test').text == 'test test'
    assert client.get('http://testserver/test2').text == 'test test2'


def test_default_404_response(client):
    response = client.get("http://testserver/doesnotexist")

    assert response.status_code == 404
    assert response.text == "Not found."


def test_class_based_handler_get(api, client):
    response_text = "this is a get request"

    @api.route('/book')
    class BookResourse:
        def get(self, req, resp):
            resp.text = response_text

    assert client.get('http://testserver/book').text == response_text


def test_class_based_handler_post(api, client):
    response_text = "this is a post request"

    @api.route('/book')
    class BookResourse:
        def post(self, req, resp):
            resp.text = response_text

    assert client.post('http://testserver/book').text == response_text


def test_class_based_handler_not_allowed_method(api, client):
    @api.route('/book')
    class BookResourse:
        def post(self, req, resp):
            resp.text = "test"

    with pytest.raises(AttributeError):
        client.get('http://testserver/book')


def test_alternative_route(api, client):
    response_text = "Alternative way to add a route"

    def home(req, resp):
        resp.text = response_text
    
    api.add_route("/alternative", home)
    assert client.get("http://testserver/alternative").text == response_text


def test_template(api, client):
    
    @api.route('/html')
    def html_handler(req, resp):
        resp.body = api.template(
            'index.html',
            context={
                "title": "Some Title",
                "name": "Some Name"
            }
        ).encode()
    
    response = client.get("http://testserver/html")

    assert "text/html" in response.headers["Content-Type"]
    assert "Some Title" in response.text
    assert "Some Name" in response.text
