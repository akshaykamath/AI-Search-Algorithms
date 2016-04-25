__author__ = 'Akshay'

from GraphDiscovery.Dfs import Dfs
from GraphDiscovery.Bfs import Bfs
from GraphDiscovery.Ids import Ids
from GraphDiscovery.GraphBuilder import GraphBuilder


def main():
    file_path_3 = 'Graphs/graph3'
    file_path_2 = 'Graphs/graph2'
    file_path_1 = 'Graphs/graph1'
    file_path_4 = 'Graphs/graph4'

    # 1. Get the user input and run the corresponding search.
    print "Search strategy could be : DFS, BFS, IDS. If anything other than these values are provided,"
    print "Breadth first search or BFS is performed.\n"

    user_input = raw_input("Enter 2 cities and search strategy in format (source_city_name destination_city_name search_type): \n")
    ui = user_input.strip().lower().split(' ')
    print user_input

    # 2. Generate the adjacency list
    adj_dict = GraphBuilder.generate_adjacency_list(file_path_4)

    # 3. Perform Validations: the count in the split array should be 3 - 2 cities and 1 search strategy
    if ui.__len__() is not 3:
        print "Input is not in a correct format.\n"
        print "Try something like this: Oradea Arad DFS\n"
        return

    else:
        print "Finding path from :", ui[0], " to ", ui[1]

    source = ui[0]
    destination = ui[1]

    # 4. Invoke the corresponding search

    if ui[2] == "dfs":
        print "######### DFS - Depth First #######"
        dfs = Dfs(adj_dict, source, destination)
        dfs.perform_dfs()
        dfs.print_path()

    elif ui[2] == "ids":
        print "######### IDS - Iterative deepening  #######"
        idfs = Ids(adj_dict, source, destination)
        idfs.perform_searching()
        idfs.print_path()

    else:
        print "######### BFS - Breadth First #######"
        bfs = Bfs(adj_dict, source, destination)
        bfs.perform_bfs()
        bfs.print_path()

    print "######## Exit ###########"

if __name__ == "__main__":
    main()
