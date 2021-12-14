from flask import Blueprint, render_template
from datetime import datetime
from app.utilities.graph_selector import graph_selector

networkx_blueprint = Blueprint('networkx_blueprint', __name__,
                        template_folder='templates')

@networkx_blueprint.route('/networkx-graphs')
def nx_graph_list():
    return render_template('networkx-graphs.html', today=datetime.today())

@networkx_blueprint.route('/networkx-graphs/<graph_name>')
def nx_graph_show(graph_name):

    graph = {
        'nodes': [],
        'edges': []
    }

    nx_graph = graph_selector(graph_name)

    if (nx_graph):
        for node in nx_graph.nodes():
            graph['nodes'].append({
                'id': node
            })

        for edge in nx_graph.edges():
            graph['edges'].append({
                'source': edge[0],
                'target': edge[1]
            })

    return render_template('networkx-graph-json.html',
        graph=graph,
        graph_name=graph_name,
        today=datetime.today()
    )

@networkx_blueprint.route('/networkx-graphs/<graph_name>/result')
def nx_graph_result(graph_name):

    graph = {
        'nodes': [],
        'edges': []
    }

    nx_graph = graph_selector(graph_name)

    if (nx_graph):
        for node in nx_graph.nodes():
            graph['nodes'].append({
                'id': node
            })

        for edge in nx_graph.edges():
            graph['edges'].append({
                'source': edge[0],
                'target': edge[1]
            })

    return render_template('result.html',
        graph=graph,
        graph_name=graph_name,
        today=datetime.today()
    )


