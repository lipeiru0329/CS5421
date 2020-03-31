<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:template match="/">
        <html>
            <body>
                 <h2>The total number is </h2>
                <p><xsl:value-of select="sum(warehouses/warehouse[address/country = 'Indonesia' and items/item/name = 'Sunscreen']/items/item/qty/text())"/></p>
            </body>
        </html>
    </xsl:template>
    
</xsl:stylesheet>