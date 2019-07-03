from flask import (
    Flask, request, render_template,
    render_template_string,
    redirect, flash
)
import json
import os
import tempfile

from .utils import (
    clone_repository,
    clear_repository,
    find_dir_content_matches
) 


app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def form_post():
    gitlink = request.form['gitlink']

    f = request.files['file']
    if f.filename == '':
        flash('No selected file')
        return redirect(request.url)

    glob = request.form['glob']

    workdir = tempfile.mkdtemp()
    clone_repository(gitlink, workdir)

    fname = tempfile.mktemp()
    with open(fname, "wb") as g:
        g.write(f.read())

    matches = find_dir_content_matches(workdir, fname, glob)
    out = json.dumps(matches, indent=2)

    clear_repository(workdir)
    os.remove(fname)

    return render_template_string(out)

def run():
    app.run(host="0.0.0.0", port=8000)
