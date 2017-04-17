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

df_bill <- dbGetQuery(con,"select cast(t1.billid as text) billid,string_agg(t1.billproductname,',') from billproduct t1 group by t1.billid")

#print(df_bill)
#itemFrequencyPlot(Groceries,topN=20,type="absolute")
df_bill[] <- lapply(df_bill,factor)
rules <- apriori(df_bill, parameter = list(supp = 0.001, conf = 0.8))
options(digits=2)
inspect(rules[1:5])
rules<-sort(rules, by="confidence", decreasing=TRUE)
#library(arulesViz)
plot(rules,method="graph",interactive=TRUE,shading=NA)
