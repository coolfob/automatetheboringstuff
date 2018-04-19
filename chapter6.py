tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():

    colWidths = [0] * len(tableData)
    for i in range(len(max(tableData,key=len))):
        for k in range(len(tableData)):
            colWidths[k] = len(max(tableData[k], key=len))
            print(tableData[k][i].rjust(colWidths[k]),end=' ')
        print()

printTable()
