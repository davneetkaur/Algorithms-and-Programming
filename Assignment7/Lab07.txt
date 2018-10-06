# CS61002: Algorithms and Programming 1 
# Name: Davneet Kaur
# Date: May 04, 2017
# Lab#.py: Assignment# 7


print "********** Exercise 1**********"


#Program to draw Graph using Snap and Graphviz
#This program represents a graph of various roads/streets in KSU
#Nodes represent KSU roads/streets
#Edges represent connection between roads

import snap

G = snap.TUNGraph.New()
for i in range(1,34):
    G.AddNode(i)
G.AddEdge(1,2)
G.AddEdge(1,3)
G.AddEdge(1,4)
G.AddEdge(1,5)
G.AddEdge(1,6)
G.AddEdge(1,7)
G.AddEdge(1,8)
G.AddEdge(5,9)
G.AddEdge(6,31)
G.AddEdge(6,32)
G.AddEdge(6,33)
G.AddEdge(7,33)
G.AddEdge(8,10)
G.AddEdge(8,11)
G.AddEdge(8,12)
G.AddEdge(8,13)
G.AddEdge(8,15)
G.AddEdge(8,16)
G.AddEdge(8,17)
G.AddEdge(13,14)
G.AddEdge(16,17)
G.AddEdge(16,18)
G.AddEdge(16,19)
G.AddEdge(17,24)
G.AddEdge(17,29)
G.AddEdge(19,21)
G.AddEdge(19,20)
G.AddEdge(22,21)
G.AddEdge(22,23)
G.AddEdge(22,24)
G.AddEdge(22,25)
G.AddEdge(22,27)
G.AddEdge(22,30)
G.AddEdge(24,26)
G.AddEdge(24,28)

S = snap.TIntStrH()
S.AddDat(1,"E Summit Street")
S.AddDat(2,"Kent dr")
S.AddDat(3,"Stockdale dr")
S.AddDat(4,"Janik dr")
S.AddDat(5,"Rizman dr")
S.AddDat(6,"W Campus Center dr")
S.AddDat(7,"E Campus Center dr")
S.AddDat(8,"Loop Road")
S.AddDat(9,"Williams dr")
S.AddDat(10,"Johnston dr")
S.AddDat(11,"Rhodes Rd")
S.AddDat(12,"Seiberling dr")
S.AddDat(13,"Eastway dr")
S.AddDat(14,"Petrarca dr")
S.AddDat(15,"Leebrick dr")
S.AddDat(16,"Jackson dr")
S.AddDat(17,"Horning Road")
S.AddDat(18,"Cunningham dr")
S.AddDat(19,"Chiarucci dr")
S.AddDat(20,"Dunbar dr")
S.AddDat(21,"Theatre dr")
S.AddDat(22,"Midway dr")
S.AddDat(23,"Prentice dr")
S.AddDat(24,"East Main Street")
S.AddDat(25,"Baumgardner dr")
S.AddDat(26,"Terrace dr")
S.AddDat(27,"Annex dr")
S.AddDat(28,"Hilltop dr")
S.AddDat(29,"Music dr")
S.AddDat(30,"Alumni dr")
S.AddDat(31,"Ted Boyd dr")
S.AddDat(32,"Allerton Street")
S.AddDat(33,"Campus Center dr")

print "Number of nodes is %d" %G.GetNodes()
print "Number of edges is %d" %G.GetEdges()
print "Cluster Coefficient of Graph is %f" %snap.GetClustCf(G, -1)
print "Cluste Coefficient of each node is"
print "NodeId\tCluster Coefficient"
clustCoefNode = snap.TIntFltH()
snap.GetNodeClustCf(G, clustCoefNode)
for item in sorted(clustCoefNode):
    print item, "\t", clustCoefNode[item]
print "Diameter of graph is %f" %snap.GetBfsFullDiam(G, 33, False)
snap.DrawGViz(G, snap.gvlNeato, "Lab07.png", "KSU Roads", S)
