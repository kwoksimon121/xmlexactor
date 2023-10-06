import os
import sys
import lxml.etree as ET

# Output.txt creation
def txt_to_file(txt_file_path, text):
    with open(txt_file_path, 'w') as file:
        file.write(text)
    print("output file created!")

def main():
    # Path to the XML file
    xml_file_path = sys.argv[1]
    # User wanted tag
    wanted_tag = sys.argv[2]
    # Path to Output TXT file
    txt_file_path = sys.argv[3]

    try:
        # Parse the XML file
        tree = ET.parse(xml_file_path)
    except ET.ParseError as e:
        print("Error parsing XML file:", str(e))
        sys.exit()
    else:
        root = tree.getroot()
        temp = ""

        for element in root.iter(wanted_tag):
            #for element in element.iter():
                if element.text:
                    var = "%s - %s %s" % (element.tag, element.attrib, element.text)
                else:
                    var = "%s - %s" % (element.tag, element.attrib)
                temp = temp + var

        txt_to_file(txt_file_path, temp)

if __name__ == "__main__":
   main()