import spaces  # ОБЯЗАТЕЛЬНО на самой первой строке!

import gradio as gr
import torch
from transformers import pipeline

# Загрузка пайплайна (используем обновленное имя задачи)
pipe = pipeline(
    "image-text-to-text",
    model="Salesforce/blip-image-captioning-base",  # или ваша модель
    device="cuda" if torch.cuda.is_available() else "cpu",
)


# Декоратор выделяет GPU на время работы функции
@spaces.GPU
def predict(image):
    if image is None:
        return "Пожалуйста, загрузите изображение."
    result = pipe(image)
    return result[0]["generated_text"]


# Интерфейс Gradio
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Описание"),
    title="Image Captioning Demo",
)

if name == "main":
    demo.launch()
