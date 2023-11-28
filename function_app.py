import azure.functions as func
from jinja2 import Template
import logging

app = func.FunctionApp(
    http_auth_level=func.AuthLevel.ANONYMOUS
)


@app.route(route="index")
def index(
    req: func.HttpRequest,
) -> func.HttpResponse:
    route = req.route_params.get('route')
    logging.info(f"GET {route}")
    index_template = Template(
        f"""<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
</html>"""
    )
    index = index_template.render(title="Joel Vandiver")
    return func.HttpResponse(
        index,
        status_code=200,
        headers={"Content-Type": "text/html"},
    )
