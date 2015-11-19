"""
Write a simple program to store some simple XML - basic tags and attributes. Dont worry about the encoding or XML features except for the tags and tag attributes. You cannot use any existing XML libraries or APIs. Your code should compile and run and demonstrate the abilities of the your XML classes.



Example code in C#


XMLobject x = new XMLObject();
XMLTag root = x.GetRoot();
root.SetName("People");
XMLTag person = root.NewTag("Person");
person.AddAttribute("id", "2323");
person.AddAttribute("DOB", "1/1/1901");
XMLTag fname = person.NewTag("FirstName", "John");
XMLTag lname = person.NewTag("LastName", "Smith");
XMLTag address = person.NewTag("address");
address.NewTag("street", "123 NW 45th street");
address.NewTag("city", "Gaithersburg");
address.NewTag("zip", "21234");
address.NewTag("state", "MD");
x.Print();
 
 Example output
 <people>
     <person id="2323" DOB="1/1/1901">
             <firstname>John</firstname>
                     <lastname>Smith</lastname>
                             <address>
                                         <street>123 NW 45th street</street>
                                                     <city>Gaithersuburg</city>
                                                                 <zip>21234</zip>
                                                                             <state>MD</state>
                                                                                     </address>
                                                                                         </person>
                                                                                         </people>
"""


"""
{
 "people": [{
  "person": {
   "attributes": {
    "id":232
    "dob":"01/16/1987
   }
   "tags": {
    "firstname":"john"
    "lastname":"smith"
    "address":{
     "tags": {
      "street":"someplace"
      "city":"somecity"
      "zip":2322
      "state":"tx"
     }
    }
   }
  }
 }]
}
"""

class Node(object):
    def __init__(self, *args, **kwargs):
        self.__name = ""
        self.__value = ""
        self.__node = None
        self.__attr = {}

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_parent(self, node):
        self.__parent_node = node

    def get_parent(self):
        return self.__parent_node

    def set_attribute(self, key, value):
        self.__attr[key] = value

    def get_attributes(self):
        return self.__attr

class XML(object):
    def __init__(self, *args, **kwargs):
        self.__nodes = []

    def create_node(self, name, parent=None):
        node = Node()
        node.set_name(name)
        node.set_parent(parent)
        self.__nodes.append(node)
        return node
    
    def print_xml(self):
        root = self.__nodes[0]
        self.__print_node(root)

    def __print_node(self, node, level=0):
        xml_str = ""
        node_str = node.get_name()
        node_attributes = node.get_attributes()
        if node_attributes:
            attr_str = ""
            for attr in node_attributes.keys():
                attr_str = attr_str + ' ' + attr + '="' + node_attributes[attr] + '"'

            node_str = node_str + " " + attr_str
            # person id=324 dob=1312
        
        tab_str = ""
        for i in range(level):
            tab_str = tab_str + "\t"

        children = self.get_child_nodes(node)
        xml_str = tab_str + "<" + node_str + ">"
        if not node.get_value():
            xml_str += "\n"
        else:
            xml_str += node.get_value()
            if len(children) > 0:
                xml_str += "\n"
            else:
                xml_str += "</" + node.get_name() + ">\n"

        for child in children:
            xml_str += self.__print_node(child, level=level+1)

        if not node.get_value() or (node.get_value() and len(children) > 0):
            xml_str += tab_str + "</" + node.get_name() + ">\n"

        if level == 0:
            print(xml_str)
            return None
        else:
            return xml_str



    def get_child_nodes(self, parent_node):
        child_nodes = []
        for node in self.__nodes:
            if node.get_parent() == parent_node:
                child_nodes.append(node)
        return child_nodes


if __name__ == "__main__":
    x = XML()
    r = x.create_node("people")
    p = x.create_node("person", r)
    p.set_attribute("id", "3232")
    p.set_attribute("dob", "1/1/1983")
    f = x.create_node("firstname", p)
    f.set_value("john")
    f.set_attribute("title","developer")
    l = x.create_node("lastname", p)
    l.set_value("smith")
    
    a = x.create_node("address", p)
    a.set_attribute("type","billing")
    s = x.create_node("street", a)
    s.set_value("123 nw 45th street")
    c = x.create_node("city", a)
    c.set_value("gaithersuburg")
    z = x.create_node("zip", a)
    z.set_value("32323")
    st = x.create_node("state", a)
    st.set_value("MD")

    a2 = x.create_node("address", p)
    a2.set_attribute("type","shipping")
    s2 = x.create_node("street", a2)
    ap = x.create_node("apartment", s2)
    ap.set_value("120A")
    s2.set_value("1220 n creek circle")
    c2 = x.create_node("city", a2)
    c2.set_value("waxahachie")
    z2 = x.create_node("zip", a2)
    z2.set_value("75165")
    st2 = x.create_node("state", a2)
    st2.set_value("tx")
    x.print_xml()

