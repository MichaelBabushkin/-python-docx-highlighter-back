import re

s = '1. Foobar { abc } ( Explanation - Foo { cde } - Count - 5301435 ) 2. Foobaz { memo } ( Explanation - baz {bleh } - Count - 13946664 )'

# s_without_parens = re.sub('\(.+?\)','',s)

text_in_brackets = re.findall('{(.+?)}',s)
print(text_in_brackets)

# text_in_brackets