import json
from datetime import datetime
from networkx import Graph, degree_centrality, closeness_centrality, eigenvector_centrality
from flask import Flask, render_template, request, jsonify, flash, redirect

from app.blueprints.networkx_blueprint import networkx_blueprint
from config.app import APP_DEBUG, APP_SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = APP_SECRET_KEY

@app.route("/")
def home():
    return render_template('form.html', today=datetime.today())


@app.route("/result", methods=['GET', 'POST'])
def result():

    centrality = request.form.get('centrality')
    graph_data_json = request.form.get('graph_json')

    try:
        graph_data_dict = json.loads(graph_data_json)
    except:
        flash('Invalid JSON format or syntax')
        return redirect('/')

    if (centrality in ['degree_centrality', 'closeness_centrality', 'eigenvector_centrality']):
        nx_graph = Graph()
        nx_graph.add_nodes_from([d['id'] for d in graph_data_dict['nodes']])
        nx_graph.add_edges_from([(d['source'], d['target']) for d in graph_data_dict['edges']])

        if (centrality == 'degree_centrality'):
            graph_data_dict['centrality'] = degree_centrality(nx_graph)
        elif (centrality == 'closeness_centrality'):
            graph_data_dict['centrality'] = closeness_centrality(nx_graph)
        elif (centrality == 'eigenvector_centrality'):
            graph_data_dict['centrality'] = eigenvector_centrality(nx_graph)


    graph_name = request.form.get('graph_name')
    nodes_color = request.form.get('nodes_color')
    edges_color = request.form.get('edges_color')
    # nodes_size = request.form.get('nodes_size')
    # edges_size = request.form.get('edges_size')

    return render_template('result.html',
        graph=graph_data_dict,
        graph_name=graph_name,
        nodes_color=nodes_color,
        edges_color=edges_color,
        # nodes_size=nodes_size,
        # edges_size=edges_size,
        today=datetime.today()
    )


app.register_blueprint(networkx_blueprint)

if __name__ == "__main__":
    app.run(debug=APP_DEBUG)
