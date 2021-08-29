import sqlparse
import pdb
import rlcompleter

pdb.Pdb.complete = rlcompleter.Completer(locals()).complete

raw = "/* Username: Scheduled, Task ID: c0a5, Query ID: 618, Queue: scheduled_queries, Query Hash: 57d4f90c1d */ WITH TMP AS(\n  SELECT\n    year, month,\n    sum(blendedcost) AS cost\n  FROM\n    \"aaaaa\".\"bbbbbb\"\n  GROUP BY\n    year, month\n)\n\nSELECT\n  year,\n  month,\n  year || month as yearmonth,\n  cost \nFROM\n  TMP\norder by\n  year desc, month desc"

print(sqlparse.format(raw, reindent=True, keyword_case='upper'))

statement = sqlparse.parse(raw)[0]
statement.tokens

pdb.set_trace()
