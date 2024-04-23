import os
import random
import shutil

def select_random_images(input_dir, output_dir, labels_output_dir, max_index, num_images):   
    image_files = os.listdir(input_dir)

    print("Número de imagens disponíveis:", len(image_files))

    # Número de imagens disponíveis para seleção
    num_available_images = min(max_index, len(image_files))

    print("Número de imagens disponíveis para seleção:", num_available_images)

    # Verificar se o número de imagens disponíveis é suficiente
    if num_available_images < num_images:
        raise ValueError("O número de imagens disponíveis é menor do que o número de imagens desejadas.")

    # Selecionar aleatoriamente 'num_images' índices exclusivos dentro do intervalo disponível
    try:
        selected_indices = random.sample(range(num_available_images), num_images)
        print('Selected_indices:',selected_indices, len(selected_indices))
    except ValueError as e:
        print("Erro ao selecionar índices aleatórios:", e)
        print("num_available_images:", num_available_images)
        print("num_images:", num_images)
        return

    # Copiar as imagens selecionadas para o diretório de saída
    for index in selected_indices:
        try:
            image = image_files[index]
            shutil.copy(os.path.join(input_dir, image), output_dir)
            # Obter o nome do arquivo XML correspondente
            xml_file = image.replace('.png', '.txt')
            # Copiar o arquivo XML correspondente para o diretório de saída dos labels
            shutil.copy(os.path.join(labels_root, xml_file), labels_output_dir)
        except ValueError as e:
            print("ERROR:", e)

# Diretório raiz dos arquivos XML
labels_root = '/home/lucas/tcc/dataset/train/labels'


    

# Diretório de entrada para as imagens de validação
valid_input_dir = '/home/lucas/tcc/dataset/valid/images'
train_input_dir = '/home/lucas/tcc/dataset/train/images'
test_input_dir = '/home/lucas/tcc/dataset/train/images'

# Diretório de saída para as imagens de validação selecionadas
valid_output_dir = '/home/lucas/tcc/dataset/randomic_dataset/valid/images'
train_output_dir = '/home/lucas/tcc/dataset/randomic_dataset/train/images'
test_output_dir = '/home/lucas/tcc/dataset/randomic_dataset/test/images'


valid_output_dir_label = '/home/lucas/tcc/dataset/randomic_dataset/valid/labels'
train_output_dir_label = '/home/lucas/tcc/dataset/randomic_dataset/train/labels'
test_output_dir_label = '/home/lucas/tcc/dataset/randomic_dataset/test/labels'

# Número máximo de índices para cada conjunto
max_index = 5000

# Número de imagens que você deseja selecionar para cada conjunto
num_images = 10

# Selecionar imagens aleatórias para o conjunto de validação
select_random_images(valid_input_dir, valid_output_dir,valid_output_dir_label,  max_index, num_images)

# Selecionar imagens aleatórias para o conjunto de teste
select_random_images(test_input_dir, test_output_dir, test_output_dir_label, max_index, num_images)

# Selecionar imagens aleatórias para o conjunto de teste
select_random_images(train_input_dir, train_output_dir,train_output_dir_label,  max_index, num_images)
