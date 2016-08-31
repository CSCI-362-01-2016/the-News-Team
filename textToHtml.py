from string import Template
inf = open("textforhtml.txt","r")
outf = open("output.html","w")
template = Template("""<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Files In Directory</title>

</head>

<body>
    <h1>The Files In the Directory Are:</h1>
  <p>$output</p>
</body>
</html>""")
files = "";
for line in inf:
    files += line + "<br>"

outf.write(template.substitute(output=files))
inf.close()
outf.close()