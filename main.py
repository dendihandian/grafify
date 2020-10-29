from datetime import datetime
from networkx import convert, Graph, generators
from flask import Flask, render_template, request, jsonify

from app.blueprints.nx_generators import nx_generators
from config.app import APP_DEBUG

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', today=datetime.today())


@app.route("/graph", methods=['GET', 'POST'])
def graph():

    # data = request.get_data()
    # # data = request.form

    # print(data)

    # return jsonify(data)

    k = generators.krackhardt_kite_graph()

    graph = {
        'nodes': [],
        'edges': []
    }

    for node in k.nodes():
        graph['nodes'].append({
            'id': node
        })

    for edge in k.edges():
        graph['edges'].append({
            'source': edge[0],
            'target': edge[1]
        })

    return render_template('graph.html', graph=graph, today=datetime.today())


app.register_blueprint(nx_generators)

if __name__ == "__main__":
    app.run(debug=APP_DEBUG)
