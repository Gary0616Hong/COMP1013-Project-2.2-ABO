import io, requests
from PIL import Image

def download_image(url, timeout=15):
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        return Image.open(io.BytesIO(r.content)).convert("RGB")
    except Exception:
        return None
