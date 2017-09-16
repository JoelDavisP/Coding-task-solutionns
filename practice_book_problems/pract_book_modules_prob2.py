"""program to  count number of files for each extension in the given directory.  """

import os
path = input("Enter the path of the file to be searched, enclosed in double quotes.\n")

dirs = os.listdir(path)
ext = {}
py_count = 0
md_count = 0
txt_count = 0
png_count = 0
html_count = 0
other_count = 0
for i in dirs:
    extension = os.path.splitext(i)[1]
    if extension == ".py":
        py_count += 1
        ext['.py'] = py_count
    elif extension == '.md':
        md_count += 1
        ext['.md'] = md_count
    elif extension == '.txt':
        txt_count += 1
        ext['.txt'] = txt_count

    elif extension == '.png':
        png_count += 1
        ext['.png'] = png_count
    elif extension == '.html':
        html_count += 1
        ext['.html'] = html_count
    else:
        other_count += 1
        ext['other'] = other_count

print ext
