et_xmlfile documentation
------------------------

et_xmlfile is a low memory streaming XML generator developed for compatibility with lxml.etree.xmlfile where this is not available.
It is pure Python and about twice as slow than lxml or other solutions.


Note on performance
-------------------

There is one area where an optimisation for lxml will negatively affect the performance of et_xmfile: when using the `.element()` method on an xmlfile context manager. It is recommended not to use this, though the method is provided for code compatibility.


Sample code:
++++++++++++

.. literalinclude:: example.py


API Documentation
-----------------

.. toctree::
    :maxdepth: 1

    api/et_xmlfile
