import sqlparse

# Split a string containing two SQL statements:
raw = 'select * from foo; select * from bar;'
statements = sqlparse.split(raw)
statements

first = statements[0]
print(sqlparse.format(first, reindent=True, keyword_case='upper'))

parsed = sqlparse.parse('select * from foo')[0]
parsed.tokens
