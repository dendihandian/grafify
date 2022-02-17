from networkx import generators

"""
    NetworkX Generator Graphs: https://networkx.org/documentation/stable/reference/generators.html
"""

def graph_selector(graph_name, request_parameters = {}):
    nx_graph = None

    if (graph_name == ''):
        return None

    generator_graphs = {

        # small networks
        "bull_graph" : generators.bull_graph(),
        "chvatal_graph" : generators.chvatal_graph(),
        "cubical_graph" : generators.cubical_graph(),
        "desargues_graph" : generators.desargues_graph(),
        "diamond_graph" : generators.diamond_graph(),
        "dodecahedral_graph" : generators.dodecahedral_graph(),
        "frucht_graph" : generators.frucht_graph(),
        "heawood_graph" : generators.heawood_graph(),
        "hoffman_singleton_graph" : generators.hoffman_singleton_graph(),
        "house_x_graph" : generators.house_x_graph(),
        "icosahedral_graph" : generators.icosahedral_graph(),
        "krackhardt_kite_graph" : generators.krackhardt_kite_graph(),
        "moebius_kantor_graph" : generators.moebius_kantor_graph(),
        "octahedral_graph" : generators.octahedral_graph(),
        "pappus_graph" : generators.pappus_graph(),
        "sedgewick_maze_graph" : generators.sedgewick_maze_graph(),
        "tetrahedral_graph" : generators.tetrahedral_graph(),
        "truncated_cube_graph" : generators.truncated_cube_graph(),
        "truncated_tetrahedron_graph" : generators.truncated_tetrahedron_graph(),
        "tutte_graph" : generators.tutte_graph(),

        # social networks
        "karate_club_graph" : generators.karate_club_graph(),
        "davis_southern_women_graph" : generators.davis_southern_women_graph(),
        "florentine_families_graph" : generators.florentine_families_graph(),
        "les_miserables_graph" : generators.les_miserables_graph(),

        # others
        "caveman_graph" : generators.caveman_graph(l=2, k=3),
        "graph_atlas_g" : generators.graph_atlas_g()[0],

    }

    try:
        nx_graph = generator_graphs[graph_name]
    except:
        pass


    return nx_graph
