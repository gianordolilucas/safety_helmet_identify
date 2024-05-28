import os
import xml.etree.ElementTree as ET
import zipfile
from tqdm import tqdm

def xml_to_yolo(xml_path, yolo_path):
  """
  Converte uma única anotação XML para label do YOLO.

  Args:
    xml_path: Caminho para o arquivo XML.
    yolo_path: Caminho para salvar o label do YOLO.
  """
  tree = ET.parse(xml_path)
  root = tree.getroot()

  # Obter informações da imagem
  image_name = root.find("filename").text
  image_width = int(root.find("width").text)
  image_height = int(root.find("height").text)

  # Criar lista de labels do YOLO
  yolo_labels = []
  for obj in root.findall("object"):
    class_name = obj.find("name").text
    bndbox = obj.find("bndbox")
    xmin = int(bndbox.find("xmin").text)
    ymin = int(bndbox.find("ymin").text)
    xmax = int(bndbox.find("xmax").text)
    ymax = int(bndbox.find("ymax").text)

    # Calcular coordenadas do centro e largura/altura normalizadas
    x_center = (xmin + xmax) / 2 / image_width
    y_center = (ymin + ymax) / 2 / image_height
    width = (xmax - xmin) / image_width
    height = (ymax - ymin) / image_height

    yolo_labels.append([class_name, x_center, y_center, width, height])

  # Salvar labels do YOLO
  with open(yolo_path, "w") as f:
    for label in yolo_labels:
      f.write(" ".join([str(item) for item in label]) + "\n")

def main():
  """
  Função principal para converter anotações XML em labels do YOLO para um conjunto de dados.

  Args:
    xml_dir: Diretório que contém os arquivos XML.
    yolo_dir: Diretório para salvar os labels do YOLO.
  """
  xml_dir = os.path.join(os.getcwd(), "/home/lucas-gianordoli/Downloads/archive.zip")
  yolo_dir = os.path.join(os.getcwd(), "/home/lucas-gianordoli/Documents/dataset")

  # Extrair arquivos XML do ZIP
  with zipfile.ZipFile(xml_dir, 'r') as zip_ref:
    zip_ref.extractall(yolo_dir)

  # Converter cada arquivo XML para label do YOLO
  print('Agora vou passar XML->YOLO.TXT')
  xml_files = [os.path.join(yolo_dir+'/annotations', f) for f in os.listdir(yolo_dir+'/annotations') if f.endswith(".xml")]
  for xml_path in tqdm(xml_files):
    yolo_path = xml_path.replace(".xml", ".txt")
    print(xml_path, '->', yolo_path)
    xml_to_yolo(xml_path, yolo_path)

  # Remover arquivos XML temporários
  for xml_path in xml_files:
    os.remove(xml_path)

if __name__ == "__main__":
  main()
