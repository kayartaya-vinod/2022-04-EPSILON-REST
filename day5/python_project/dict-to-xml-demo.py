import dicttoxml2


p1 = dict(firstname='Vinod', lastname='Kumar', email='vinod@kwit.com', phone='9988776655')

xml = dicttoxml2.dicttoxml(p1, custom_root='contact', attr_type=False)
print(xml.decode('utf-8'))
