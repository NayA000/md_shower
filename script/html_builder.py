


def func1(title, keywords, markdown_content, iframe_url, html_name = 'test.html'):
    with open('static\\template.html', 'r', encoding='utf8') as file:
        html_text = file.read()
    
    title_placeholder = '''{[{title}]}'''
    keywords_placeholder = '''{[{keyowrds}]}'''
    markdown_content_placeholder = '''{[{markdown_content}]}'''
    iframe_url_placeholder = '''{[{iframe_url}]}'''

    html_text = html_text.replace(title_placeholder, title)
    html_text = html_text.replace(keywords_placeholder, keywords)
    html_text = html_text.replace(markdown_content_placeholder, markdown_content)
    html_text = html_text.replace(iframe_url_placeholder, iframe_url)

    with open(f'static/{html_name}', 'w') as file:
        file.write(html_text)

def markdown_analysis(markdown_text):
    '''
    解析格式为
    从markdown文件头中解析出格式为'{[{key::value}]}'的内容
    并构造成字典返回
    '''
    import re
    lines = markdown_text.split('\n')
    result = {}

    re_pattern = re.compile(r'\{\[\{(.*)(::)(.*)\}\]\}')

    while True:
        matchs = re_pattern.search(lines[0])
        if matchs:
            result[matchs.group(1)] = matchs.group(3)
            lines.pop(0)
        else:
            break
    
    result['markdown_content'] = '\n'.join(lines)
    return result

def markdown_builder(md_file_path):
    with open(md_file_path, 'r', encoding='utf8') as file:
        md = file.read()
    
    r = markdown_analysis(md)
    func1(r['title'], r['keywords'], r['markdown_content'], r['iframe_url'], r['html_name'])