from script.html_builder import func1, markdown_analysis, markdown_builder

title = 'Test Title'
keywords = 'Test Keywords'
markdown_content = '''
# 111
---
## 222
test test test
'''
iframe_url = ''
html_name = 'test.html'

# func1(title, keywords, markdown_content, iframe_url, html_name)




md = '''{[{title::Test Title}]}
{[{keywords::Test Keywords}]}
{[{iframe_url::}]}
{[{html_name::test2.html}]}
# 111
---
## 222
test test test
'''

# print(markdown_analysis(md))
# r = markdown_analysis(md)
# func1(r['title'], r['keywords'], r['markdown_content'], r['iframe_url'], r['html_name'])

markdown_builder('./md/hello_word.md')
