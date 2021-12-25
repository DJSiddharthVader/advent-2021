from collections import defaultdict
from collections import Counter


def read_input(infile):
    edges = [tuple(x.strip('\n').split('-')) for x in open(infile).readlines()]
    return edges


def make_edge_dict(edge_list):
    nodes = set([x for edge in edge_list for x in edge])
    edge_dict = defaultdict(list)
    for node in nodes:
        for edge in edge_list:
            if node == edge[0]:
                edge_dict[node].append(edge[-1])
            elif node == edge[-1]:
                edge_dict[node].append(edge[0])
    cleaned = {node: [x for x in adjacents if x not in ['start', node]]
               for node, adjacents in edge_dict.items()}
    cleaned['end'] = []
    return cleaned


def enumerate_paths(paths, edges):
    endpoints = set([path[-1] for path in paths])
    if endpoints == set(['end']):
        return paths
    else:
        new_paths = []
        for path in paths:
            if path[-1] == 'end':
                new_paths.append(path)
            else:
                for next_cave in edges[path[-1]]:
                    if not (next_cave.islower() and next_cave in path):
                        new_paths.append(path + [next_cave])
        return enumerate_paths(new_paths, edges)


def star1(edge_list):
    edges = make_edge_dict(edge_list)
    paths = enumerate_paths([['start']], edges)
    print(len(paths))


def multi_visited_cave(path):
    for cave, visits in dict(Counter(path)).items():
        if visits > 1:
            return True
    return False


def enumerate_paths2(paths, edges):
    endpoints = set([path[-1] for path in paths])
    if endpoints == set(['end']):
        return paths
    else:
        new_paths = []
        for path in paths:
            if path[-1] == 'end':
                new_paths.append(path)
            else:
                if multi_visited_cave(path):
                    for next_cave in edges[path[-1]]:
                        if not (next_cave.islower() and next_cave in path):
                            new_paths.append(path + [next_cave])
                else:
                    for next_cave in edges[path[-1]]:
                        new_paths.append(path + [next_cave])
        return enumerate_paths(new_paths, edges)


def star2(edge_list):
    edges = make_edge_dict(edge_list)
    paths = enumerate_paths2([['start']], edges)
    print(len(paths))


if __name__ == '__main__':
    infile = '../inputs/P12.txt'
    inputs = read_input(infile)
    print('Star 1 result')
    star1(inputs)
    print('Star 2 result')
    star2(inputs)
