def get_moon_phase(day, month):
    phases = [
        {"symbol": "🌑", "illumination": 0.0},
        {"symbol": "🌒", "illumination": 0.25},
        {"symbol": "🌓", "illumination": 0.5},
        {"symbol": "🌔", "illumination": 0.75},
        {"symbol": "🌕", "illumination": 1.0},
        {"symbol": "🌖", "illumination": 0.75},
        {"symbol": "🌗", "illumination": 0.5},
        {"symbol": "🌘", "illumination": 0.25},
    ]

    index = (day + month) % len(phases)
    return phases[index]





