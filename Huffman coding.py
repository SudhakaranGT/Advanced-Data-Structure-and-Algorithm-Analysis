import heapq


class Symbol:
    def __init__(self,symbol,freq):
        self.symbol = symbol
        self.freq = freq
        self.code = " "
        self.left = None
        self.right = None

    def __lt__(self,nxt):
        return self.freq < nxt.freq

        

def printNodes(node, val=''):
    newVal = val + str(node.code)
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
        
def sorting(data):
    data = sorted(data,key=lambda symbol:symbol.freq)
    return data
data = []
sym = []
while True:
    for i in range(int(input("Enter the Total no.of symbols:"))):
        s = input("Enter the symbol:")
        f = eval(input("Enter the frequency:"))
        symbol = Symbol(s,f)
        data.append(symbol)
        sym.append(symbol)
    data = sorting(data)
    while len(data) > 1:
             first = data.pop(0)
             second = data.pop(0)
             first.code = '0'   
             second.code = '1'          
             newnode = Symbol(first.symbol+second.symbol,first.freq+second.freq)
             newnode.left = first
             newnode.right = second
             data.append(newnode)
    printNodes(data[0])