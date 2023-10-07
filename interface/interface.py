import gradio as gr
import os


def image_mod(image):
    return image.rotate(45)


demo = gr.Interface(
    image_mod,
    gr.Image(type="pil"),
    "image",
    flagging_options=["blurry", "incorrect", "other"],
    examples=[
    ],
)

if __name__ == "__main__":
    demo.launch()

