from flask import Flask, request, redirect, send_from_directory
from jinja2 import Environment, FileSystemLoader
from urllib.parse import urlparse
from colorama import init, Fore, Back, Style
import data
import json
import os

init()

app = Flask(__name__)

environment = Environment(loader=FileSystemLoader("template/"))
not_found_template = environment.get_template("not_found.html")
redirect_self_error = environment.get_template("redirect_self_error.html")

# We need to know the current site to capture loops where this
# site is re-directing itself to itself
CURRENT_DOMAIN = "5000-sg3141592-35e3t4e4uq-3kiw8bkjrk6.ws-eu63.gitpod.io"

# We need to explicitly ignore favicon routes
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Add site
@app.route("/api/addSite", methods=["POST"])
def add_site()
    data.addSite(request.json.url, request.json.target)
    return Response("OK", status=200)

# Redirect service
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def entry_point(path):
    ref_url = urlparse(request.headers.get("Referer")).netloc
    target_url = data.lookupSite(ref_url)
    
    # Debug text
    print(Style.DIM + "ref_url: " + ref_url)
    print(Fore.CYAN + "target_url: " + target_url)
    print(Style.RESET_ALL)

    if(target_url == CURRENT_DOMAIN):
        return redirect_self_error.render(
            ref_url=ref_url
        )
    elif(target_url):
        return redirect(target_url)
    else:
        return not_found_template.render(
            ref_url=ref_url
        )

if __name__ == '__main__':
    app.run(debug=True)