from queue import Queue


class Node:
    #very simple node class for name and respective countries 
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def _initialize_neighbors(self):
        # Create all of the countries
        usa = Node("USA")
        canada = Node("CAN")
        mexico = Node("MEX")
        belize = Node("BLZ")
        guatemala = Node("GTM")
        el_salvador = Node("SLV") 
        honduras = Node("HND")
        nicaragua = Node("NIC")
        costa_rica = Node("CRI")
        panama = Node("PAN")

        # Define all of the neighbors for each country,  this is supposed to be a graph representation of the countries 
        usa.add_neighbor(canada)
        usa.add_neighbor(mexico)

        mexico.add_neighbor(usa)
        mexico.add_neighbor(belize)
        mexico.add_neighbor(guatemala)

        guatemala.add_neighbor(mexico)
        guatemala.add_neighbor(belize)
        guatemala.add_neighbor(el_salvador)
        guatemala.add_neighbor(honduras)

        honduras.add_neighbor(guatemala)
        honduras.add_neighbor(el_salvador)
        honduras.add_neighbor(nicaragua)

        nicaragua.add_neighbor(honduras)
        nicaragua.add_neighbor(costa_rica)

        costa_rica.add_neighbor(nicaragua)
        costa_rica.add_neighbor(panama)

        panama.add_neighbor(costa_rica)

        #creates a dict that maps country code to their node for convenience  
        return {
            country.name: country
            for country in (
                usa, canada, mexico, belize, guatemala,
                el_salvador, honduras, nicaragua, costa_rica, panama,
            )
        }

    #adds neighbors to node's list, effectively adding an edge
    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)
        #breath first search algo to find shortest path between us to target country 
    def find_path(self, target_name):
        #just to normalize the input to uppercase
        target_name = target_name.upper()

        #create the countries and their neighbors
        countries = self._initialize_neighbors()

        #check for valid input 
        if target_name not in countries:
            return "Invalid country code"
        #we always start from usa
        start = countries["USA"]

        # Each queue item contains a country and the path used to reach it.
        queue = Queue()
        queue.put((start, [start.name]))

        # keep track of seen countries so we arent accidentally looping 
        visited = {start.name}

        #while queue isint empty
        while not queue.empty():    
            current, current_path = queue.get()
            
            if current.name == target_name:
                return current_path
            #add all unvisited neighbors to the queue
            for neighbor in current.neighbors:
                if neighbor.name not in visited:
                    #add to visited, and add the new neighbor to the queue and add them to the existing path 
                    visited.add(neighbor.name)
                    queue.put((neighbor, current_path + [neighbor.name]))

        # here in case of catastophic error return no path was found. should never happen
        return "No path found"

    





        



