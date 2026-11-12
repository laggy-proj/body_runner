#!/usr/bin/env python3
"""Одноразово завантажує MediaPipe локально, щоб гра працювала повністю офлайн.
Запуск:  python3 download_mediapipe.py   (поруч із body-runner-3d.html)
Потім:   python3 -m http.server 8000     і відкрийте http://localhost:8000/body-runner-3d.html
"""
import os, urllib.request
V = "0.10.14"
CDN = f"https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@{V}"
FILES = {
    "vision_bundle.mjs": f"{CDN}/vision_bundle.mjs",
    "wasm/vision_wasm_internal.js": f"{CDN}/wasm/vision_wasm_internal.js",
    "wasm/vision_wasm_internal.wasm": f"{CDN}/wasm/vision_wasm_internal.wasm",
    "wasm/vision_wasm_nosimd_internal.js": f"{CDN}/wasm/vision_wasm_nosimd_internal.js",
    "wasm/vision_wasm_nosimd_internal.wasm": f"{CDN}/wasm/vision_wasm_nosimd_internal.wasm",
    "pose_landmarker_lite.task": "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task",
}
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mediapipe")
for rel, url in FILES.items():
    dst = os.path.join(root, rel); os.makedirs(os.path.dirname(dst), exist_ok=True)
    print("↓", rel); urllib.request.urlretrieve(url, dst)
print("Готово. Тепер гра не потребує інтернету.")
