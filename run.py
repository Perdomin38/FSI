# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

og = search.GPSProblem('O', 'G'
                       , search.romania)

ch = search.GPSProblem('C', 'H'
                       , search.romania)

lu = search.GPSProblem('L', 'U'
                       , search.romania)

print(search.ramificacion_graph_search(ab).path())
print("-----------------------------")

print(search.ramificacion_subestimacion_graph_search(ab).path())

