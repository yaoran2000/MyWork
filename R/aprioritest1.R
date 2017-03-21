library(Matrix)
library(arules)
library(grid)
library(arulesViz)
library(datasets)
#Load the data set
data(Groceries)
#itemFrequencyPlot(Groceries,topN=20,type="absolute")
rules <- apriori(Groceries, parameter = list(supp = 0.001, conf=0.8))
plot(rules,method="graph",interactive=TRUE,shading=NA)

