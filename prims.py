import csv

with open('deliverablefile2.csv', 'r') as csv_file: 
    file_handle = csv.reader(csv_file)
    data = next(file_handle)

number_of_vertices = int(data[0])

graph = [[0 for _ in range(number_of_vertices)] for _ in range(number_of_vertices)]

edges = []
k = 0

for i in range(number_of_vertices):
    for j in range(number_of_vertices):
        k += 1
        graph[i][j] = int(data[k])
        if int(data[k]) != 0 and i != j:
            edges.append((int(data[k]), i, j))

edges.sort()

selected_vertices = set()
start_vertex = 0
selected_vertices.add(start_vertex)
total_weight = 0

# create and open a text file for writing
with open('deliverablefile2.txt', 'w') as output_file:

    # Wwite the number of vertices found to the output file
    output_file.write(f"{number_of_vertices} vertices found.\n")

    while len(selected_vertices) < number_of_vertices:
        # initialize variables to store the minimum-cost edge and its cost
        min_edge = None
        min_cost = float('inf')
        
        # iterate over the edges to find the minimum-cost edge connecting a selected vertex and an unselected vertex
        for cost, u, v in edges:
            # check if one vertex is selected and the other is not
            if (u in selected_vertices and v not in selected_vertices) or (v in selected_vertices and u not in selected_vertices):
                # check if the current edge has a smaller cost than the minimum cost found so far
                if cost < min_cost:
                    # update the minimum-cost edge and its cost
                    min_edge = (cost, u, v)
                    min_cost = cost
        
        # add the minimum-cost edge and the unselected vertex to the set of selected edges and vertices
        if min_edge:
            selected_vertices.add(min_edge[1])
            selected_vertices.add(min_edge[2])
            total_weight += min_edge[0]
            # write the selected edge to the output file
            output_file.write(f"Adding edge ({min_edge[1]}, {min_edge[2]}) with weight {min_edge[0]}.\n")

        # remove the minimum-cost edge from the list of edges
        edges.remove(min_edge)

    # write the total weight of the spanning tree to the output file
    output_file.write(f"\nTotal weight of spanning tree: {total_weight}")
