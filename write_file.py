def td(x):
    return '<td>{}</td>'.format(x)

def tr(l):
    html = "<tr>"
    for x in l:
        html += td(x)
    html += "</tr>"
    return html

def row_values(n):
    l = []
    for i in range(1,11):
        l.append(n*i)
    return l

f = open('test.html', 'w')
f.write("Hello world!")