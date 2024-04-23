def precision(true_labels, predicted_labels):
    """

    Args:
        true_labels (list): Lista de rótulos verdadeiros.
        predicted_labels (list): Lista de rótulos previstos pelo modelo.

    Returns:
        float: Valor da precisão.
    """
    # Calcula o número de verdadeiros positivos e falsos positivos
    true_positives = sum((p_label == 1 and t_label == 1) for p_label, t_label in zip(predicted_labels, true_labels))
    false_positives = sum((p_label == 1 and t_label == 0) for p_label, t_label in zip(predicted_labels, true_labels))
    
    # Evita divisão por zero
    if true_positives + false_positives == 0:
        return 0
    
    # Calcula e retorna a precisão
    return true_positives / (true_positives + false_positives)

def recall(true_labels, predicted_labels):
    """
    Args:
        true_labels (list): Lista de rótulos verdadeiros.
        predicted_labels (list): Lista de rótulos previstos pelo modelo.

    Returns:
        float: Valor da recall.
    """
    # Calcula o número de verdadeiros positivos e falsos negativos
    true_positives = sum((p_label == 1 and t_label == 1) for p_label, t_label in zip(predicted_labels, true_labels))
    false_negatives = sum((p_label == 0 and t_label == 1) for p_label, t_label in zip(predicted_labels, true_labels))
    
    # Evita divisão por zero
    if true_positives + false_negatives == 0:
        return 0
    
    # Calcula e retorna a racall
    return true_positives / (true_positives + false_negatives)


def f1_score(true_labels, predicted_labels):
    """
    Calcula o F1-Score do modelo.

    Args:
        true_labels (list): Lista de rótulos verdadeiros.
        predicted_labels (list): Lista de rótulos previstos pelo modelo.

    Returns:
        float: Valor do F1-Score.
    """
    # Calcula precisão e revocação
    prec = precision(true_labels, predicted_labels)
    rec = recall(true_labels, predicted_labels)
    
    # Evita divisão por zero
    if prec + rec == 0:
        return 0
    
    # Calcula e retorna o F1-Score
    return 2 * (prec * rec) / (prec + rec)


def false_positive_rate(true_labels, predicted_labels):
    """
    Calcula a taxa de falsos positivos do modelo.

    Args:
        true_labels (list): Lista de rótulos verdadeiros.
        predicted_labels (list): Lista de rótulos previstos pelo modelo.

    Returns:
        float: Valor da taxa de falsos positivos.
    """
    # Calcula o número de falsos positivos e verdadeiros negativos
    false_positives = sum((p_label == 1 and t_label == 0) for p_label, t_label in zip(predicted_labels, true_labels))
    true_negatives = sum((p_label == 0 and t_label == 0) for p_label, t_label in zip(predicted_labels, true_labels))
    
    # Evita divisão por zero
    if false_positives + true_negatives == 0:
        return 0
    
    # Calcula e retorna a taxa de falsos positivos
    return false_positives / (false_positives + true_negatives)
