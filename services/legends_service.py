# services/legends_service.py
from .api_legends import get_legends_from_api
from .curated_legends import get_curated_legends

def get_best_legends(day, month):
    try:
        # Try the Wikipedia API first
        legends = get_legends_from_api(day, month)
        if legends and len(legends) > 0:
            return legends
    except Exception as e:
        print(f"API failed: {e}")
    
    # If API fails or is empty, use your curated list
    return get_curated_legends(day, month)