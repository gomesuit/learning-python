import sqlparse
from sqlparse.sql import Where, Comparison, Parenthesis, Identifier


class RecursiveTokenParser(object):
    def __init__(self, query):
        self.query = query
        self.names = []

    def get_table_names(self):
        elements = sqlparse.parse(self.query)
        for token in elements[0].tokens:
            if isinstance(token, Identifier):
                self.identifier(token)
            elif isinstance(token, Parenthesis):
                self.parenthesis(token)
            elif isinstance(token, Where):
                self.where(token)
        return [str(name) for name in self.names]

    def where(self, token):
        for subtoken in token.tokens:
            if isinstance(subtoken, Comparison):
                self.comparison(subtoken)

    def comparison(self, token):
        for subtoken in token.tokens:
            if isinstance(subtoken, Parenthesis):
                self.parenthesis(subtoken)

    def parenthesis(self, token):
        for subtoken in token.tokens:
            if isinstance(subtoken, Identifier):
                self.identifier(subtoken)
            elif isinstance(subtoken, Parenthesis):
                self.parenthesis(subtoken)

    def identifier(self, token):
        self.names.append(token)

    def get_query(self):
        return self.query


sql2 = """
With 
a as
(
 select 
   x,y
from g
)

select
x, y,z
from b
left join a
on b.id = a.id

"""

t = RecursiveTokenParser(sql2)

print(t.get_query())
print(t.get_table_names())
