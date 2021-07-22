import argparse
import string

command_chars = '''"';<>+*-/^&|:=?'''
command_chars = list(map(ord, command_chars))

tree_chars = command_chars

class Tree:
        def __init__(self, root, left = None, right = None):
                self.root = root
                self.left = left
                self.right = right

        def __repr__(self):
                return '({}, {}, {})'.format(self.root, self.left, self.right)

class Leaf(Tree):
        def __init__(self, leaf):
                self.leaf = self.left = self.right = self.root = leaf

        def __repr__(self):
                return 'Leaf({})'.format(self.leaf)

def form_tree(array, tree = None):
        if tree is None:
                tree = Tree(array.pop(0))
        
        if isinstance(tree, Leaf):
                return tree

        if not array:
                return tree

        if tree.left is None and array:
                node = array.pop(0)
                if node in tree_chars: node = Tree(node)
                else: node = Leaf(node)
                        
                tree.left = form_tree(array, node)
                        
        if tree.right is None and array:
                node = array.pop(0)
                if node in tree_chars: node = Tree(node)
                else: node = Leaf(node)
                        
                tree.right = form_tree(array, node)

        return tree

def set_nodes(tree, vals):
        if isinstance(tree, Leaf):
                if tree.leaf is None:
                        try: return Leaf(vals.pop(0))
                        except: return Leaf(0)
                return tree
                
        if tree.left is None:
                try: tree.left = Leaf(vals.pop(0))
                except: tree.left = Leaf(0)
        else: tree.left = set_nodes(tree.left, vals)
                
        if tree.right is None:
                try: tree.right = Leaf(vals.pop(0))
                except: tree.right = Leaf(0)
        else: tree.right = set_nodes(tree.right, vals)

        return tree

def traverse(cmds, tree):
        if isinstance(tree, Leaf):
                return

        run_cmds(cmds, tree, tree, [])

        traverse(cmds, tree.left)
        traverse(cmds, tree.right)

def get_full_branch(tree):
        if isinstance(tree, Leaf):
                return chr(tree.leaf)
        return chr(tree.root) + get_full_branch(tree.left) + get_full_branch(tree.right)

def run_cmds(code, memory, current_node, parents, index = 0):
        char = code[index]
        
        if char == '.':
                print(end = chr(current_node.root))
        if char == '"':
                print(end = chr(current_node.left.root))
        if char == "'":
                print(end = chr(current_node.right.root))
        if char == ':':
                print(end = chr(current_node.left.root))
                print(end = chr(current_node.right.root))
        if char == '$':
                print(current_node.root)
        
        if char == '<':
                parents.append(current_node)
                current_node = current_node.left
        if char == '>':
                parents.append(current_node)
                current_node = current_node.right
        if char == '`':
                current_node = parents.pop()

        if char == '~': current_node.root = ~current_node.root
        if char == '@': current_node.root = 0

        if char == '+': current_node.root = current_node.left.root + current_node.right.root
        if char == '-': current_node.root = current_node.left.root - current_node.right.root
        if char == '*': current_node.root = current_node.left.root * current_node.right.root
        if char == '/': current_node.root = current_node.left.root // current_node.right.root
        if char == '^': current_node.root = current_node.left.root ^ current_node.right.root
        if char == '&': current_node.root = current_node.left.root & current_node.right.root
        if char == '|': current_node.root = current_node.left.root | current_node.right.root

        if char == '=':
                cmds = get_full_branch(current_node.left) + get_full_branch(current_node.right)
                run_cmds(cmds, memory, current_node, [])

        if char == '?':
                if current_node.root:
                        current_node = current_node.left
                else:
                        current_node = current_node.right

        if char == '#':
                if current_node.root:
                        current_node = memory
                        parents = []
        
        if char == '(':
                scan = ''
                depth = 1
                index += 1
                while True:
                        if code[index] == '(': depth += 1
                        if code[index] == ')': depth -= 1
                        if depth == 0: break
                        scan += code[index]
                        index += 1
                if scan:
                        traverse(scan, memory)

        return index

def main(code, argv, mem_flag, debug_flag):
	if not code: return
        chars = list(map(lambda c: None if c == '_' else ord(c) * (c != '%'), code))
        memory = set_nodes(form_tree(chars), argv)
        current_node = memory
        parents = []
        index = 0

        if mem_flag:
                print(memory)

        while index < len(code):
                index = run_cmds(code, memory, current_node, parents, index) + 1
                if debug_flag:
                        print(memory)

if __name__ == '__main__':
        parser = argparse.ArgumentParser(prog = './yggdrasil')

        getcode = parser.add_mutually_exclusive_group()
        getcode.add_argument('-f', '--file', help = 'Specifies that code be read from a file', action = 'store_true')
        getcode.add_argument('-c', '--cmd', '--cmdline', help = 'Specifies that code be read from the command line', action = 'store_true')

        parser.add_argument('-m', '--memory', help = 'Dump the binary memory tree before execution', action = 'store_true')
        parser.add_argument('-d', '--debug', help = 'Dump debug info', action = 'store_true')
        
        parser.add_argument('program')
        parser.add_argument('argv', nargs = '*', type = int)
        
        settings = parser.parse_args()

        if settings.file:
                with open(settings.program, encoding = 'utf-8') as file:
                        code = file.read()
        else:
                code = settings.program
        
        main(code, settings.argv, settings.memory, settings.debug)
