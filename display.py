#Name - Tun Myat
#ID - 51705354

import cgi

print("Content-type: text/html")    #HTML is following
print()
print("<TITLE>CGI script output</TITLE>")
print("<H1>Displaying the image</H1>")

FORM = cgi.FieldStorage()

print("<img id = 'imgid' src='{}'>".format(FORM.getvalue('imglink1')))
print("<br>")

print("<p id='imgtitleid'>Image title is: {}".format(FORM.getvalue("title1")))
print("</p>")

print("<p id='imgyearid'>Image year is: {}".format(FORM.getvalue("year1")))
print("</p>")

print("<p id='imgdesid'>Image description is: {}".format(FORM.getvalue("description1")))
print("</p>")


print("<script>")
print("function Changeimgto1()")
print("{")
print("document.getElementById('imgid').src = '{}';".format(FORM.getvalue("imglink1")))
print("document.getElementById('imgtitleid').innerHTML = 'Image title is: {}';".format(FORM.getvalue("title1")))
print("document.getElementById('imgyearid').innerHTML = 'Image year is: {}';".format(FORM.getvalue("year1")))
print("document.getElementById('imgdesid').innerHTML = 'Image description is: {}';".format(FORM.getvalue("description1")))
print("}")
print("</script>")


print("<script>")
print("function Changeimgto2()")
print("{")
print("document.getElementById('imgid').src = '{}';".format(FORM.getvalue("imglink2")))
print("document.getElementById('imgtitleid').innerHTML = 'Image title is: {}';".format(FORM.getvalue("title2")))
print("document.getElementById('imgyearid').innerHTML = 'Image year is: {}';".format(FORM.getvalue("year2")))
print("document.getElementById('imgdesid').innerHTML = 'Image description is: {}';".format(FORM.getvalue("description2")))
print("}")
print("</script>")


print("<button type='button' onclick='Changeimgto1()'>First image</button>")
print("<br><br>")
print("<button type='button' onclick='Changeimgto2()'>Second image</button>")

print("")
print("<br><br>")