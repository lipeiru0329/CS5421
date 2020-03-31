<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:template match="/">
        <html> 
            <body>
                <h2>Warehouse in Singapore</h2>
                <xsl:for-each select="/warehouses/warehouse[address/country = 'Singapore']">
                    <h3>Warehouse Name: <xsl:value-of select="name"></xsl:value-of></h3>   
                    <table border="1">
                    <xsl:for-each select="items/item[qty > 975]">
                        
                        <tr>
                            <td>Name</td>
                            <td>Price</td>
                            <td>Quantity</td>
                        </tr>
                        <tr>
                            <td><xsl:value-of select="name"/></td>
                            <td><xsl:value-of select="price"/></td>
                            <td><xsl:value-of select="qty"/></td>
                        </tr>
                        
                    </xsl:for-each>
                    </table>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>
    
</xsl:stylesheet>