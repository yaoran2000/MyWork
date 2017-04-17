require('RPostgreSQL')
pw <- {"Admin1234$"}
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "mht",host = "localhost", port = 5432,user = "etl", password = pw)
rm(pw)
print(dbExistsTable(con, "billproduct"))

