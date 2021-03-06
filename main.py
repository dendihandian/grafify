import json
from datetime import datetime
from networkx import convert, Graph, generators
from flask import Flask, render_template, request, jsonify, flash, redirect

from app.blueprints.nx_generators import nx_generators
from config.app import APP_DEBUG, APP_SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = APP_SECRET_KEY

@app.route("/")
def home():
    return render_template('index.html', today=datetime.today())


@app.route("/graph", methods=['GET', 'POST'])
def graph():

    graph_data_json = request.form.get('graph_json')

    try:
        graph_data_dict = json.loads(graph_data_json)
    except:
        flash('Invalid JSON format or syntax')
        return redirect('/')

    graph_title = request.form.get('graph_title')
    nodes_size = request.form.get('nodes_size')
    nodes_color = request.form.get('nodes_color')
    edges_size = request.form.get('edges_size')
    edges_color = request.form.get('edges_color')

    return render_template('graph.html', 
        graph=graph_data_dict,
        graph_name=graph_title,
        nodes_size=nodes_size,
        nodes_color=nodes_color,
        edges_size=edges_size,
        edges_color=edges_color,
        networkx=False, 
        today=datetime.today()
    )


app.register_blueprint(nx_generators)

if __name__ == "__main__":
    app.run(debug=APP_DEBUG)
