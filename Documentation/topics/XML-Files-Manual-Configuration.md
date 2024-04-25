# XML Files (Manual) Configuration

To configure the deskphones to access CISCAPPS, you can also edit the XML
configuration files.

This guide assumes you know how to find the XML file(s).

1) Locate the lines `<informationURL>` and `<servicesURL>`
2) Edit the `informationURL` to your server's hostname followed by `/info/`
3) Edit the `servicesURL` to your server's hostname followed by `/homepage/`
   ![editingXMLfile.png](editingXMLfile.png)
4) Save the file.
5) Manually restart the phone by unplugging the ethernet cable.

The phone(s) should now be able to access CISCAPPS! You can try it out by pressing
the Services button on one of the phones. **_(Image below - Num.7)_**

![ciscoPhone.png](ciscoPhone.png)
(from cisco.com)