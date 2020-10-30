#Name - Tun Myat
#ID - 51705354

import cgi

print("Content-type: text/html")    #HTML is following
print()


print("<H1>Requesting image</H1>")

print("<b>First image<br></b>")
print("<form action='/test/cgi-bin/display.py' method = 'post'>Image link: <input type='text' name='imglink1'><br>")
print("Title: <input type='text' name='title1'><br>")
print("Year: <input type='text' name='year1'><br>")
print("Description: <input type='text' name='description1'><br><br><br>")


print("<b>Second image<br></b>")
print("Image link: <input type='text' name='imglink2'><br>")
print("Title: <input type='text' name='title2'><br>")
print("Year: <input type='text' name='year2'><br>")
print("Description: <input type='text' name='description2'><br><br><br>")

	
print("<input type='submit' value='Submit'></form>")

