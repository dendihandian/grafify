from datetime import datetime
from networkx import convert, Graph, generators
from flask import Flask, render_template

from config.app import APP_DEBUG

app = Flask(__name__)


@app.route("/")
def home():

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

    return render_template('index.html', graph=graph, today=datetime.today())


if __name__ == "__main__":
    app.run(debug=APP_DEBUG)
