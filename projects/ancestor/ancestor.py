import collections

def earliest_ancestor(ancestors, starting_node):

    parents_by_child = {}

    for parent, child in ancestors:
        if child in parents_by_child:
            parents_by_child[child].append(parent)
        else:
            parents_by_child[child] = [parent]

    # Early exit if the starting node has no parents
    if starting_node not in parents_by_child:
        return -1

    path_queue = collections.deque() # doubly ended queue

    last_path = [starting_node] # this will let us save the last path dequeued

    path_queue.append(last_path)

    while len(path_queue) > 0:
        last_path = path_queue.popleft()
        oldest_ancestor = last_path[-1]

        if oldest_ancestor in parents_by_child:
            parents_by_child[oldest_ancestor].sort(reverse=True) # make sure lowest id goes in queue last
            for parent in parents_by_child[oldest_ancestor]:
                new_path = last_path.copy()
                new_path.append(parent)

                path_queue.append(new_path)

    return last_path[-1]