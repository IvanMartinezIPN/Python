import xml.etree.ElementTree as ET
#funciones para elemntree en jerarquia
miarbol = ET.parse('archivo1.xml')

root = miarbol.getroot()
print(root)