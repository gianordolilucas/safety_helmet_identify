from ultralytics import YOLO, settings


model = YOLO('yolov9c.yaml')
model = YOLO('yolov9c.pt')
model.info()
results = model.train(data='helmet_dataset.yaml', epochs=1, imgsz=640)
results = model('/home/lucas/tcc/dataset/image.jpg')


# # Exemplo de anotações verdadeiras (caixas delimitadoras e classes dos objetos)
# true_annotations = []

# # Exemplo de previsões do modelo YOLO (caixas delimitadoras previstas e confiança)
# yolo_predictions = []

# # Função para verificar se uma caixa delimitadora prevista se sobrepõe significativamente com uma caixa delimitadora verdadeira
# def box_iou(box1, box2):

#     """
#     Calcula a Interseção sobre União (IoU) entre duas caixas delimitadoras.

#     Argumentos:
#         box1 (list[float]): Coordenadas da caixa 1 no formato [x1, y1, x2, y2].
#         box2 (list[float]): Coordenadas da caixa 2 no formato [x1, y1, x2, y2].

#     Retorna:
#         float: Valor de IoU entre 0 e 1, representando a sobreposição entre as caixas.
#     """

#     # Verificação de formato
#     if len(box1) != 4 or len(box2) != 4:
#         raise ValueError("As caixas devem ter 4 coordenadas: [x1, y1, x2, y2]")

#     # Extrair coordenadas
#     x1_1, y1_1, x2_1, y2_1 = box1
#     x1_2, y1_2, x2_2, y2_2 = box2

#     # Calcular área de interseção
#     inter_area = _box_inter_area(box1, box2)

#     # Calcular área de cada caixa
#     area_1 = _box_area(box1)
#     area_2 = _box_area(box2)

#     # Evitar divisão por zero
#     if area_1 == 0 or area_2 == 0:
#         return 0.0

#     # Calcular IoU
#     iou = inter_area / (area_1 + area_2 - inter_area)

#     return iou


# def _box_inter_area(box1, box2):

#     """
#     Calcula a área de interseção entre duas caixas delimitadoras.

#     Argumentos:
#         box1 (list[float]): Coordenadas da caixa 1 no formato [x1, y1, x2, y2].
#         box2 (list[float]): Coordenadas da caixa 2 no formato [x1, y1, x2, y2].

#     Retorna:
#         float: Área de interseção entre as caixas.
#     """

#     x1_1, y1_1, x2_1, y2_1 = box1
#     x1_2, y1_2, x2_2, y2_2 = box2

#     # Calcular coordenadas de interseção
#     inter_x1 = max(x1_1, x1_2)
#     inter_y1 = max(y1_1, y1_2)
#     inter_x2 = min(x2_1, x2_2)
#     inter_y2 = min(y2_1, y2_2)

#     # Área de interseção (se positiva)
#     if inter_x2 >= inter_x1 and inter_y2 >= inter_y1:
#         return (inter_x2 - inter_x1) * (inter_y2 - inter_y1)
#     else:
#         return 0.0


# def _box_area(box):

#     """
#     Calcula a área de uma caixa delimitadora.

#     Argumentos:
#         box (list[float]): Coordenadas da caixa no formato [x1, y1, x2, y2].

#     Retorna:
#         float: Área da caixa.
#     """

#     x1, y1, x2, y2 = box
#     return (x2 - x1) * (y2 - y1)


# # Construir as listas de rótulos verdadeiros e previstos
# true_labels = []
# predicted_labels = []

# # Iterar sobre as anotações verdadeiras
# for true_annotation in true_annotations:
#     true_class = true_annotation["class"]
#     true_bbox = true_annotation["bbox"]
    
#     # Adicionar o rótulo verdadeiro à lista
#     'true_labels.append(true_class)
    
#     # Verificar se há sobreposição significativa com alguma das previsões do YOLO
#     best_iou = 0
#     best_predicted_class = None
    
#     for yolo_prediction in yolo_predictions:
#         predicted_class = yolo_prediction["class"]
#         predicted_bbox = yolo_prediction["bbox"]
#         iou = box_iou(true_bbox, predicted_bbox)
        
#         # Se a sobreposição for significativa e a classe for a mesma, consideramos uma previsão correta
#         if iou > best_iou and true_class == predicted_class:
#             best_iou = iou
#             best_predicted_class = predicted_class
            
#     # Se encontrarmos uma previsão válida, adicionamos à lista de previsões
#     if best_predicted_class:
#         predicted_labels.append(best_predicted_class)
#     else:
#         # Se não houver previsão válida, consideramos como uma previsão incorreta (falso negativo)
#         predicted_labels.append(None)  # ou qualquer valor que indique que não houve detecção
        
# # Agora você tem suas listas de rótulos verdadeiros e previstos
# print("Verdadeiros:", true_labels)
# print("Previstos pelo YOLO:", predicted_labels)
