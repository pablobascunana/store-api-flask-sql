SWAGGER_CONFIG = {
    "swagger_version": "2.0",
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST, DELETE"),
        ('Access-Control-Allow-Credentials', "true"),
    ],
    "specs": [
        {
            "version": "0.0.1",
            "title": "Flask-MySQL locations API",
            "description": "Example of Restful API with MySQL",
            "endpoint": "/",
            "route": "/",
            "termsOfService": ""
        }
    ]
}
