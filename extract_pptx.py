import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_text_from_pptx(pptx_path):
    text = ""
    try:
        with zipfile.ZipFile(pptx_path, 'r') as z:
            for filename in z.namelist():
                if filename.startswith('ppt/slides/slide') and filename.endswith('.xml'):
                    xml_content = z.read(filename)
                    root = ET.fromstring(xml_content)
                    slide_text = []
                    for elem in root.iter():
                        if elem.tag.endswith('}t') and elem.text:
                            slide_text.append(elem.text)
                    if slide_text:
                        text += " ".join(slide_text) + "\n\n"
        return text
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    pptx_path = sys.argv[1]
    extracted = extract_text_from_pptx(pptx_path)
    with open('pptx_text.txt', 'w', encoding='utf-8') as f:
        f.write(extracted)
