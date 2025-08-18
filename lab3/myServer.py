from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def show_params():
    html = """<!DOCTYPE html>
<html><head><title>Request Parameters</title></head><body>
<h2>GET Parameters</h2>"""
    
    if request.args:
        for key in request.args.keys():
            values = request.args.getlist(key)  # Use getlist to get all values
            if len(values) == 1:
                html += f"<p><strong>{escape(key)}</strong>: {escape(values[0])}</p>"
            else:
                html += f"<p><strong>{escape(key)}</strong>: {escape(', '.join(values))}</p>"
    else:
        html += "<p><em>No GET parameters found.</em></p>"
    
    html += "<h2>POST Parameters</h2>"
    
    if request.method == 'POST' and request.form:
        for key in request.form.keys():
            values = request.form.getlist(key)  # Use getlist for POST too
            if len(values) == 1:
                html += f"<p><strong>{escape(key)}</strong>: {escape(values[0])}</p>"
            else:
                html += f"<p><strong>{escape(key)}</strong>: {escape(', '.join(values))}</p>"
    else:
        html += "<p><em>No POST parameters found.</em></p>"
    
    html += "</body></html>"
    return html

if __name__ == '__main__':
    app.run(debug=True)