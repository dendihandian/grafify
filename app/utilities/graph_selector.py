from networkx import generators

def graph_selector(graph):
    nx_graph = None

    if (graph == ''):
        return None

    # Small Networks
    elif (graph == 'bull_graph'):
        nx_graph = generators.bull_graph()
    elif (graph == 'chvatal_graph'):
        nx_graph = generators.chvatal_graph()
    elif (graph == 'cubical_graph'):
        nx_graph = generators.cubical_graph()
    elif (graph == 'desargues_graph'):
        nx_graph = generators.desargues_graph()
    elif (graph == 'diamond_graph'):
        nx_graph = generators.diamond_graph()
    elif (graph == 'dodecahedral_graph'):
        nx_graph = generators.dodecahedral_graph()
    elif (graph == 'frucht_graph'):
        nx_graph = generators.frucht_graph()
    elif (graph == 'heawood_graph'):
        nx_graph = generators.heawood_graph()
    elif (graph == 'hoffman_singleton_graph'):
        nx_graph = generators.hoffman_singleton_graph()
    elif (graph == 'house_x_graph'):
        nx_graph = generators.house_x_graph()
    elif (graph == 'icosahedral_graph'):
        nx_graph = generators.icosahedral_graph()
    elif (graph == 'krackhardt_kite_graph'):
        nx_graph = generators.krackhardt_kite_graph()
    elif (graph == 'moebius_kantor_graph'):
        nx_graph = generators.moebius_kantor_graph()
    elif (graph == 'octahedral_graph'):
        nx_graph = generators.octahedral_graph()
    elif (graph == 'pappus_graph'):
        nx_graph = generators.pappus_graph()
    elif (graph == 'sedgewick_maze_graph'):
        nx_graph = generators.sedgewick_maze_graph()
    elif (graph == 'tetrahedral_graph'):
        nx_graph = generators.tetrahedral_graph()
    elif (graph == 'truncated_cube_graph'):
        nx_graph = generators.truncated_cube_graph()
    elif (graph == 'truncated_tetrahedron_graph'):
        nx_graph = generators.truncated_tetrahedron_graph()
    elif (graph == 'tutte_graph'):
        nx_graph = generators.tutte_graph()

    # Social Networks
    elif (graph == 'karate_club_graph'):
        nx_graph = generators.karate_club_graph()
    elif (graph == 'davis_southern_women_graph'):
        nx_graph = generators.davis_southern_women_graph()
    elif (graph == 'florentine_families_graph'):
        nx_graph = generators.florentine_families_graph()
    elif (graph == 'les_miserables_graph'):
        nx_graph = generators.les_miserables_graph()

    # else
    else:
        nx_graph = None

    print(nx_graph)

    return nx_graph
