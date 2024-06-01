# FreePBX (chan_sccp) Configuration

Configuring FreePBX with CISCAPPS is actually quite easy.

1) Login into your FreePBX admin panel.
2) Navigate to the **"Sccp Connectivity"** tab and select **"Server Config"**
   ![freePbx1.png](freePbx1.png)
3) Then click on the **"SCCP Device URL"** tab.
4) Edit the **"Phone Service URL"** and the **"Phone information URL"** to your 
   server's hostname, followed by `/homepage/` for the Service URL and `/info/`
   for the information URL. ![freePbx1.2.png](freePbx1.2.png)
5) Make sure to click Submit to save the changes.

The phones should automatically pull the new configuration, but if they don't,
then you need to restart the phones manually by pulling the ethernet cable out.

All phones should now be able to access CISCAPPS! You can try it out by pressing
the Services button on one of the phones. **_(Image below - Num.7)_**

![ciscoPhone.png](ciscoPhone.png)
(from cisco.com)