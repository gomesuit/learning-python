import sqlparse
import pdb
import rlcompleter

pdb.Pdb.complete = rlcompleter.Completer(locals()).complete

query = '''

/* Username: Scheduled, Task ID: c0a5, Query ID: 618, Queue: scheduled_queries, Query Hash: 57d4f90c1d */ WITH TMP AS(
  SELECT
    year, month,
    sum(blendedcost) AS cost
  FROM
    "aaaaa"."bbbbbbbb"
  GROUP BY
    year, month
)

SELECT
  year,
  month,
  year || month as yearmonth,
  cost
FROM
  TMP
order by
  year desc, month desc
'''

# query = sqlparse.format(
#     query,
#     strip_comments=True,
#     reindent_aligned=True,
#     keyword_case='upper',
# )

print(query)

parsed_queries = sqlparse.parse(query)
tokens = list(parsed_queries[0].flatten())

for t in tokens:
    if t.ttype in sqlparse.tokens.Text.Whitespace:
        continue
    if t.ttype == sqlparse.tokens.Token.Punctuation:
        continue
    print("token_value: '{}', token_type: {}".format(t.value, t.ttype))

pdb.set_trace()
