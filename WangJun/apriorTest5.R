library(Matrix)
library(arules)
library(arulesViz)
library(grid)
library(arulesViz)
require('RPostgreSQL')

pw <- {"Admin1234$"}
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "mht",host = "localhost", port = 5432,user = "etl", password = pw)
#rm(pw)

results <- dbGetQuery(con,"select cast(billid as text) billid,billproductname from billproduct")

transactions <- as(split(as.vector(results$billproductname),as.vector(results$billid)),"transactions")
#print(df_bill)
#itemFrequencyPlot(Groceries,topN=20,type="absolute")
#df_bill[] <- lapply(df_bill,factor)
rules <- apriori(transactions, parameter = list(supp = 0.001, conf = 0.8, maxlen = 2, minlen = 2))
options(digits=2)
inspect(rules[1:5])
rules<-sort(rules, by="confidence", decreasing=TRUE)
#library(arulesViz)
plot(rules,method="graph",interactive=TRUE,shading=NA)
