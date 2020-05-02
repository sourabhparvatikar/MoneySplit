from backend.views import HelloWorld


def add_resource(api):
    api.add_resource(HelloWorld, '/')
