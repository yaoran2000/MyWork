library(Matrix)
library(arules)
library(arulesViz)
library(grid)
library(arulesViz)
require('RPostgreSQL')

pw <- {"Admin1234$"}
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "mht",host = "localhost", port = 5432,user = "etl", password = pw)
rm(pw)

df_bill <- dbGetQuery(con,"select cast(t1.billid as text) billid,string_agg(t1.billproductname,',') from billproduct t1 group by t1.billid")

#print(df_bill)
#itemFrequencyPlot(Groceries,topN=20,type="absolute")
#df_bill[] <- lapply(df_bill,factor)
for (column in names(df_bill)){
  df_bill[column] <- as.factor(df_bill[[column]])
}
lapply(df_bill,class)
df_bill_matrix <- as(df_bill, "transactions")
#print(results_matrix)
rules <- apriori(df_bill_matrix, parameter = list(supp = 0.001, conf = 0.9))
options(digits=2)
inspect(rules[1:5])
rules<-sort(rules, by="confidence", decreasing=TRUE)
plot(rules,method="graph",interactive=TRUE,shading=NA)
