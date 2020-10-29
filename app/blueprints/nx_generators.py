from flask import Blueprint, render_template
from datetime import datetime
from app.blueprints.graph_selector import graph_selector

nx_generators = Blueprint('nx_generators', __name__,
                        template_folder='templates')

@nx_generators.route('/networkx/generators')
def nx_graph_list():
    return render_template('nx/index.html', today=datetime.today())

@nx_generators.route('/networkx/generators/<graph_name>')
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

    return render_template('graph.html', 
        graph=graph, 
        graph_name=graph_name, 
        networkx=True,
        today=datetime.today()
    )


