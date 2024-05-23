from flask import Flask, render_template, request, send_from_directory
#from guutzcode.telescope_control import Caltech6m
from caltech6m_stud import Caltech6m

# WEB SERVER SETUP
app = Flask(__name__)   # Flask app instance


# DISH CONTROL SETUP
caltech6m = Caltech6m() # Telescope control instance


# WEB SERVER ROUTES

@app.route('/1')
def boys():
    return render_template('boys.html')

@app.route('/2')
def walle():
    return render_template('walle.html')

@app.route('/point', methods=['POST'])
def point():
    json = request.get_json()
    az = float(json['az'])
    el = float(json['el'])
    caltech6m.point(az, el)
    print(f"Pointing to {az}, {el}")

    return "OK"

@app.route('/status')
def status():
    az, el = caltech6m.status()
    return f"{az}, {el}"

@app.route("/assets/<path:path>")
def send_assets(path):
    """Serve static assets (css, js, images, etc.)"""
    return send_from_directory("assets", path)

if __name__ == '__main__':
    app.run()