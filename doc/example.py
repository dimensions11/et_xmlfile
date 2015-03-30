from io import BytesIO
from xml.etree.ElementTree import Element

from et_xmlfile import xmlfile

out = BytesIO()
with xmlfile(out) as xf:
    el = Element("root")
    xf.write(el) # write the XML straight to the file-like object

assert out.getvalue() == b"<root />"
