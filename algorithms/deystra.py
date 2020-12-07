"""
Deystra's alhorithm
"""


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for n in costs:
        cost = costs[n]
        if cost < lowest_cost and n not in proccesed:
            lowest_cost = cost
            lowest_cost_node = n
    return lowest_cost_node



graph = {
    'start': {'a': 6, 'b': 2},
    'a': {'fin': 1},
    'b': {'a': 3, 'fin': 5},
    'fin': {},
}

infinity = float("inf")
costs = {
    'a': 6,
    'b': 2,
    'fin': infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None,
}

proccesed = []

node = find_lowest_cost_node(costs)  # 'b'
while node:
    cost = costs.get(node)  # 2
    neighbors = graph[node]  # {'a': 3, 'fin': 5}
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]  # цена до текущего узла + стоимость до след.
        if costs[n] > new_cost:  # если текущая цена больше новой
            costs[n] = new_cost  # то обновить цену, на новую
            parents[n] = node  # и сделать текущую ноду родителем соседа
    proccesed.append(node)  # добавить ноду в список отработанных
    node = find_lowest_cost_node(costs)  # найти новую ноду
    
