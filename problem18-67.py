import sys

class Node:
    def __init__(self,value):
        self.value=value
        self.max_int_value=None
        self.parents=[]
        self.children=[]
    def __repr__(self):
        if self.max_int_value is None: return "<%d (%d,%d)>" % (self.value,len(self.parents),len(self.children))
        else: return "<%d,%d (%d,%d)>" % (self.value,self.max_int_value,len(self.parents),len(self.children))
    def build(self):
        assert(self.max_int_value is None)
        self.max_int_value=self.value
        aa=[]
        for parent in self.parents:
            assert(parent.max_int_value is not Node)
            aa.append(parent.max_int_value)
        if aa: self.max_int_value+=max(aa)

def load_triangle(filename="inputs/triangle.txt"):
    file=open(filename)
    top=None
    precrow=[]
    total=[]
    for k,line in enumerate(file):
        row=[Node(int(value)) for value in line.split(' ')]
        assert(len(row)==k+1)
        for child,parent in zip(row,precrow):
            child.parents.append(parent)
            parent.children.append(child)
        for child,parent in zip(reversed(row),reversed(precrow)):
            child.parents.append(parent)
            parent.children.append(child)
        if top is None:
            top=row[0]
        precrow=row
        total.extend(precrow)
    print "loaded %d nodes" % len(total)
    return top,precrow,total

def print_triangle(top):
    precrow=[top]
    while precrow:
        print precrow
        row=[]
        for node in precrow:
            if node.children: row.append(node.children[0])
        if precrow[-1].children: row.append(precrow[-1].children[-1])
        precrow=row

if len(sys.argv)>2: top,bottom,ordered=load_triangle(sys.argv[1])
else: top,bottom,ordered=load_triangle()
for order in ordered: order.build()
print max(node.max_int_value for node in bottom)
