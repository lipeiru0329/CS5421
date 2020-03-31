<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Warehouse</h2>
                <table style="width: 100%" border="1 solid black">
                <xsl:for-each select="/warehouses/warehouse[address/country = 'Singapore' or address/country = 'Malaysia']">
                    <xsl:for-each select="items/item">
                        <xsl:sort select="qty" data-type="text" order="descending" />
                        <xsl:if test="position()=1">
                            <tr>
                            <th>Country</th>
                            <th><xsl:value-of select="../../address/country"></xsl:value-of></th>
                            <th>Warehouse Name:</th>
                            <th><xsl:value-of select="../../name"/></th>
                            <th>item</th>
                            <th><xsl:value-of select="name"/></th>
                            </tr>
                        </xsl:if>
                    </xsl:for-each>
                </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>