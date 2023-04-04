import xml.etree.ElementTree as ET
import random

xml_template = '''
<Employees>
    <CountryCode>PT</CountryCode>
    <Employee>
        <EmployeeID>501</EmployeeID>
        <FirstName>Johny</FirstName>
        <LastName>Silverhand</LastName>
        <LanguageCode>de-DE</LanguageCode>
        <Operator>
            <SignOnName>jsilver</SignOnName>
            <CleartextPassword>920290</CleartextPassword>
            <PasswordEffectiveDate>20210929</PasswordEffectiveDate>
            <PasswordExpirationDate>29990101</PasswordExpirationDate>
            <PasswordEntryErrorCount>5</PasswordEntryErrorCount>
            <PrintCode>JS</PrintCode>
            <ProfileAffiliation>
                <ProfileID>4</ProfileID>
                <RetailStoreID>1234</RetailStoreID>
                <EffectiveDate>20210929</EffectiveDate>
                <ExpirationDate>20211231</ExpirationDate>
            </ProfileAffiliation>
            <ProfileAffiliation>
                <ProfileID>2</ProfileID>
                <RetailStoreID>1234</RetailStoreID>
                <EffectiveDate>20210929</EffectiveDate>
                <ExpirationDate>20220630</ExpirationDate>
            </ProfileAffiliation>
        </Operator>
    </Employee>
</Employees>
'''

for i in range(1, 4):

    imiona = ['Staszek', 'Jurek', 'Artur', 'Gerwazy', 'Jerzy', 'Antoni', 'Jaroslaw', 'Jeremy', 'Cezary']
    nazwiska = ['Kot', 'Kiler', 'Ryba', 'Waski', 'Siarzewski', 'Szanski', 'Dyzma', 'Rywin', 'Kiepski', 'Pazura']

    xml_data = xml_template.format()

    root = ET.fromstring(xml_data)
    tree = ET.ElementTree(root)

    numer_id = root.find(".//EmployeeID")
    numer_id.text = '500'
    numer_id.text = str(int(numer_id.text) + i)
    print(numer_id.text)

    imie_element = root.find(".//FirstName")
    imie_element.text = random.choice(imiona)
    nazwisko_element = root.find(".//LastName")
    nazwisko_element.text = random.choice(nazwiska)

    filename = f"file_{i}.xml"
    tree.write(filename, encoding="utf-8", xml_declaration=True)
