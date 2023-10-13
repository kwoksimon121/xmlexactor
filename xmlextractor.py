#v1.1
import os
import sys
import lxml.etree as ET
import csv
import pandas as pd

def txt_ntag(tags, root, txt_file_path):
    print("hello")
    out_str = ""
    for tag in tags:
        for element in root.iter(tag):   
            if element.tag == tag:
                out_str = out_str + "TAG: %s " % (element.tag)
                if element.attrib:
                    out_str = out_str + "ATTRIB: %s " % (element.attrib)
                if element.text:
                    out_str = out_str + "TEXT: %s" % (element.text)
                if not out_str.endswith("\t"):
                    out_str = out_str + "\n"
    print(out_str)
    file = open(txt_file_path, 'w')
    file.write(out_str)
    print("txt created!")

#def single tag
def txt_to_file(txt_file_path, wanted_tag, root):
    #print("\ninside function\n")
    out_str = ""
    wtcount = 0    #wanted_tag_count
    ntcount = 0    #nest_tag_count
    for element in root.iter(wanted_tag):   #check wanted tag
            wtcount += 1
            for element in element.iter():      #check nested tag
                out_str = out_str + "TAG: %s " % (element.tag)
                if element.tag != wanted_tag:
                    ntcount += 1
                if element.attrib:
                    out_str = out_str + "ATTRIB: %s " % (element.attrib)
                if element.text:
                    out_str = out_str + "TEXT: %s" % (element.text)
                if not out_str.endswith("\t"):
                    out_str = out_str + "\n"
            out_str = out_str + "\n================================\n"
    out_str = out_str + "\nEND of TAG: %s " % (wanted_tag)

    print("%d \"%s\" element found" % (wtcount, wanted_tag))  
    print("%d nested element found" % (ntcount))  
    file = open(txt_file_path, 'w')
    file.write(out_str)
    print("txt created!")

#def xlsx_to_file(xlsx_file_path, root, wanted_tag):
def xlsx_to_file(csv_file_path):
    new_dataFrame = pd.read_csv(csv_file_path)
    xlsx_file_path = csv_file_path.replace(".csv", ".xlsx")
    new_excel = pd.ExcelWriter(xlsx_file_path)
    new_dataFrame.to_excel(new_excel, index=False, sheet_name='Sheet1')
    new_excel.close()
    print("xlsx created")

def csv_to_file(csv_file_path, root, wanted_tag):
    csvfile = open(csv_file_path, 'w', encoding='utf-8')
    csvfile_writer = csv.writer(csvfile)
    
    csvfile_writer.writerow(["tag","attrib","text"])
       
    wtcount = 0
    ntcount = 0
    tag = ""
    attrib = ""
    text = ""
    for element in root.iter(wanted_tag):   #check wanted tag
            wtcount += 1
            #ntcount = 0
            for element in element.iter():      #check nested tag
                tag = element.tag
                if element.tag != wanted_tag:
                    ntcount += 1
                if element.attrib:
                    attrib = element.attrib
                else:
                    attrib = ""
                if element.text:
                    text = element.text
                else:
                    text = ""            
                csv_line = [tag, attrib, text]
                csvfile_writer.writerow(csv_line)
    csvfile.close()
    print("%d \"%s\" element found" % (wtcount, wanted_tag))  
    print("%d nested element found" % (ntcount))  
    print("csv created")
    
def main():
    
    xml_file_path = sys.argv[1] # Path to the XML file
    wanted_tag = sys.argv[2]    # User wanted tag
    out_file_path = sys.argv[3] # Path to Output TXT file

    try:
        # Parse the XML file
        tree = ET.parse(xml_file_path)
    except ET.ParseError as e:
        print("Error parsing XML file:", str(e))
        sys.exit()
    else:
        #split wanted_tag string into n by comma
        splited_tag = wanted_tag.split(',')
    
        root = tree.getroot()
        if splited_tag == 1:
            if out_file_path.endswith('.txt'):
            #txt
                txt_to_file(out_file_path, wanted_tag, root)
            elif out_file_path.endswith('.csv') or out_file_path.endswith('.xlsx'):
            #csv
                csv_to_file(out_file_path, root, wanted_tag)
            #xlsx
                xlsx_to_file(out_file_path)
        else:
            x=5    
            print(splited_tag)
            txt_ntag(splited_tag, root, out_file_path)
            #n tags
        
if __name__ == "__main__":
   main()