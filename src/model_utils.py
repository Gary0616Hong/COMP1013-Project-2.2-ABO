import numpy as np

def weighted_probability_fusion(image_prob, text_prob, alpha):
    """alpha weights the image model; (1-alpha) weights the text model."""
    return alpha * image_prob + (1.0 - alpha) * text_prob
