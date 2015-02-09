__author__ = 'zhangnan'

#   Artificial Intelligence
#   Homework_1_graph_search.py

#Created by zhangnan on 1/27/15.

import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbor = []


class Graph:

    def __init__(self):
        self.__nodes = []
        self.__paths = []

    def nodes(self):
        return self.__nodes
    def paths(self):
        return self.__paths

    def add_node(self,a):
        if a not in self.__nodes:
            self.__nodes.append(a)

    def add_path(self, a, b):
        if a == None or b == None:
            return
        self.add_node(a)
        self.add_node(b)

        if (a,b) not in self.__paths and (b,a) not in self.__paths:
            self.__paths.append((a,b))

    def path_exist(self, p):
        if len(2)!= 2:
            print 'invalid path'
            return False
        if p in self.__paths or (p[1],p[0]) in self.__paths:
            return True
        return False

# class Tree:

class State:
    def __init__(self, name, path_left):
        self.name = name
        self.path_left = path_left
        self.sub_states = []
        self.parent_state = None


class AI_search_graph:
    def __init__(self, g, start_node):
        self.__graph = g
        if start_node not in g.nodes():
            print 'start node invalid'
            return
        self.__start = start_node
        self.solutions = []

    def generate_search_space(self, left_path, node):
        if len(left_path) == 0:
            return None
        s = State(node.name,left_path)
        for index, p in enumerate(left_path):
            if node in p:
                id = p.index(node)
                new_node = p[1-id]
                new_list = list(left_path[0:index]+left_path[index+1:])
                sub_s = self.generate_search_space(new_list,new_node)
                if len(new_list) == 0:
                    new_s = State(new_node.name,new_list)
                    new_s.parent_state = s
                    s.sub_states.append(new_s)
                if sub_s != None:
                    sub_s.parent_state = s
                    s.sub_states.append(sub_s)
        return s


    def find_solution_bfs(self, s, goal):
        queue = []
        queue.append(s)
        while len(queue) > 0:
            first = queue[0]
            for i in first.sub_states:
                queue.append(i)
            if len(first.path_left) == 0:
                if (goal and goal.lower() == first.name) or goal == None:
                    parent = first.parent_state
                    goal_list = [first.name.upper()]
                    while parent:
                        goal_list.append(parent.name.upper())
                        parent = parent.parent_state
                    goal_list.reverse()
                    self.solutions.append(goal_list)
            del queue[0]




    def find_solution_dfs(self, s, goal, stack):
        if len(s.path_left) == 0 :
            if goal:
                if goal.lower() == s.name:
                    stack.append(s.name.upper())
                    # print stack
                    self.solutions.append(list(stack))
                    stack.pop()
                    return True
                else:
                    return False
            else:
                stack.append(s.name.upper())
                self.solutions.append(list(stack))
                stack.pop()
                return True
        stack.append(s.name.upper())
        for i in s.sub_states:
            b = self.find_solution_dfs(i, goal, stack)
        stack.pop()


def print_report(idx, goal, start_node, solutions):
    print '\nFigure 1 from {} to {}:'.format(start_node.name.upper(), goal.upper() if goal else 'Anywhere')
    if len(solutions)<= 0:
        print 'No solutions\n'
        return
    print 'The first found solution: {}'.format(' '.join(solutions[0]))
    print 'Number of nodes expanded to find the first found solution: {}'.format(' '.join(solutions[0][1:-1]))
    print '\n{} solution'.format(len(solutions)) + ('' if len(solutions) <= 1 else 's')
    for item in solutions:
        print ' '.join(item)+' '
    print '\n'




# goal1 = None
# ai.find_solution_dfs(s, goal1,[])
# print_report(1,goal1,a,ai.solutions)
#
# ai.solutions = []
# ai.find_solution_bfs(s, goal1)
# print_report(1,goal1,a,ai.solutions)







# ai = AI_search_graph(g1,a)
# s = ai.generate_search_space(g1.paths(),a)
# d = ai.find_solution_dfs(s, goal1,[])
# print_report(1,goal1,a,ai.solutions)
# ai.solutions = []
# ai.find_solution_bfs(s, goal1)
# print_report(1,goal1,a,ai.solutions)

def solution(graph, start, strategy, goal):
    ai = AI_search_graph(graph,start)
    s = ai.generate_search_space(graph.paths(),start)
    if strategy == 'dfs':
        ai.find_solution_dfs(s, goal,[])
    elif strategy == 'bfs':
        ai.find_solution_bfs(s, goal)
    else:
        print 'invalide strategy input'
        sys.exit(1)
    print_report(1,goal,start,ai.solutions)

def main():
    args = sys.argv[1:]
    if len(args) <1 or len(args)>3:
        print 'usage: figure_index search_strategy(bfs|dfs) goal'
        print 'example: 1 dfs a'
        print 'example: 2 bfs'
        sys.exit(1)

    if args[0] != '1' and args[0] != '2':
        print 'invalid figure input'
        sys.exit(1)

    g1 = Graph()
    g2 = Graph()

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    g1.add_path(a,b)
    g1.add_path(a,d)
    g1.add_path(a,c)
    g1.add_path(b,d)
    g1.add_path(b,c)
    g1.add_path(e,d)
    g1.add_path(e,c)
    g1.add_path(d,c)



    if len(args) == 2:
        if args[0] == '2':
            g1.add_path(a,f)
            g1.add_path(b,f)
        solution(g1,a,args[1],None)
    else:
        if args[0] == '2':
            g1.add_path(a,f)
            g1.add_path(b,f)
        solution(g1,a,args[1],args[2])



if __name__ == '__main__':
  main()