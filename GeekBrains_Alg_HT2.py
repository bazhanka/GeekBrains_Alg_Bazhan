str = 'pop it now'
d = {}
for el in str:
    d[el]=str.count(el)
sorted_d = sorted(d.items(), key=lambda x: x[1])

class Node:
    def __init__(self, value, left_ch=None, right_ch=None):
       self.value = value
       self.left_ch = left_ch
       self.right_ch = right_ch


class Tree:
    def __init__(self, root):
        self.root = root

def height(node):
    if not node:
        return 0
    else:
        left_height = height(node.left_ch)
        right_height = height(node.right_ch)
        return max(left_height,right_height) + 1

def print_node(node,level):
    if not node:
        return 0
    if level == 1:
        print(node.value,end='-')
    elif level > 1:
        print_node(node.left_ch, level-1)
        print_node(node.right_ch, level-1)

def print_tree(node):
    i = 1
    ht = height(node)
    while i <= ht:
        print_node(node, i)
        print()
        i+=1


print(sorted_d)
def hoffman_tree(kwargs):
    d = kwargs
    while len(d) >= 1:
        my_node1 = Node(d[0][0])
        my_node2 = Node(d[1][0])
        my_node_init = Node('empty',my_node1, my_node2)
        d.append(('empty',int(d[0][1])+int(d[1][1])))
        d.remove(d[0])
        d.remove(d[0])
        d = sorted(d, key=lambda tup: tup[1])
        print(my_node_init.value, my_node2.value, my_node1.value)
        if len(d) == 1:
            my_root = Tree(my_node_init)
            return print_tree(my_root.root)
            break
#судя по всему, он в списке перезаписывает значения узлов, хотя отрабатывает верно. не понимаю, как их хранить

print(hoffman_tree(sorted_d))