
import os
#Replace your PAT
os.environ['CLARIFAI_PAT'] = "fca99ae707424f389ec932c209c3254d"
from clarifai.client.user import User
from clarifai.client.workflow import Workflow
from clarifai.client.model import Model
#replace your "user_id"
user_id="khwab001"
model_id = 'llama2-7b-chat'
model_version_id = 'e52af5d6bc22445aa7a6761f327f7129'
app_id = "inter-llama"

def get_res(input):
    #input
    # Model Predict
    res = bytes(input, 'utf-8')
    model_prediction = Model("https://clarifai.com/meta/Llama-2/models/llama2-7b-chat").predict_by_bytes(res, "text")
    result = model_prediction.outputs[-1].data.text.raw
    return result