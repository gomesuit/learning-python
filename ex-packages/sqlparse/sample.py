import sqlparse
import pprint
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

token_uniq = set()
for t in tokens:
    token_uniq.add(t.ttype)
pprint.pprint(token_uniq)


def print_tokens(tokens):
    for t in tokens:
        print(f"token_type: {t.ttype}, token_value: '{t.value}'")


comments = [t for t in tokens if t.ttype in sqlparse.tokens.Comment]
print_tokens(comments)

names = [t for t in tokens if t.ttype in sqlparse.tokens.Name]
print_tokens(names)

keywords = [t for t in tokens if t.ttype in sqlparse.tokens.Keyword]
print_tokens(keywords)

iterals = [t for t in tokens if t.ttype in sqlparse.tokens.Literal]
print_tokens(iterals)

operators = [t for t in tokens if t.ttype in sqlparse.tokens.Operator]
print_tokens(operators)

pdb.set_trace()
