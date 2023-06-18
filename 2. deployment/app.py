# AUTOGENERATED! DO NOT EDIT! File to edit: ../app.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'image', 'label', 'examples', 'intf', 'is_cat', 'classify_image']

# %% ../app.ipynb 2
from fastai.vision.all import *
import gradio as gr

def is_cat(x): return x[0].isupper()

# %% ../app.ipynb 3
learn = load_learner('./model.pkl')

# %% ../app.ipynb 5
learn.predict(im)

# %% ../app.ipynb 6
categories = ('Dog', 'Cat')

def classify_image(img):
    pred, idx, probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))

# %% ../app.ipynb 8
image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
examples = ['dog.jpg', 'cat.jpg', 'dunno.jpg']

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)
