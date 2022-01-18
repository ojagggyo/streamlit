from flask import Flask, Response, json
application = Flask(__name__)

@application.route("/")
def index():
#    return "aplication working!"
    return Response(
        "%s(%s);" %("callback", json.dumps({"name":"hogehoge"} )),
        mimetype="text/javascript"
        )

#if __name__ == "__main__":
#    application.run()