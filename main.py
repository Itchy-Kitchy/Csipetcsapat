import xml.etree.ElementTree as ET

# ------------------------------------------
# Ez a rész az XML modul rész.
# Kérlek mindegyikötök importálja a modulját
# amit választott és kommentekkel ellátva
# mutassa be a modul pár alapvető
# funkcióit. Lehetőleg ne sokat.
# Az én modulomét vehetitek alapul.
# ------------------------------------------

# Egy adott sample.xml 
# fájl beolvasása a parse funkcióval,
# majd a getroot-al az első
# elemének kiolvasása.

mytree = ET.parse("sample.xml")
myroot = mytree.getroot()
print(myroot)

# Ugyan ez a funkció egy string
# tömbbön használva.

data = "<?xml version="1.0" encoding="UTF-8"?>
<metadata>
<food>
  <item name="reggeli">szendvics</item>
  <price>800 Forint</price>
  <calories>553 kalória</calories>
</food>
</metadata>"

myroot = ET.fromstring(data) # a root elem a data string-ből
print(myroot.tag) # metadata
print(myroot[0].tag) # food - a metadata első örökölt tag-ja

for i in myroot[0]:
  print(i.tag, i.attrib)

# item  {'name':'reggeli'}
# price {}
# description {}
# calories {}

for i in myroot[0]:
  print(i.text)
  
# reggeli
# 800 Forint
# 553 kalória

# Egy kitejedtebb xml dokumentumban
# az egyes adattípusok lekérdezésére példa:

for i in myroot.finall("food"):
  item = x.find("item").text
  price = x.find("price").text
  print(item, price)
  
