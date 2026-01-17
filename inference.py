import torch, torch.nn as nn
import json, os

class MLP(nn.Module):
    def __init__(self, d_in=20, d_hidden=64, d_out=2):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(d_in,d_hidden), nn.ReLU(), nn.Linear(d_hidden,d_out))
    def forward(self, x): return self.net(x)

def model_fn(model_dir):
    model = MLP()
    state = torch.load(os.path.join(model_dir, "model.pt"), map_location="cpu")
    model.load_state_dict(state)
    model.eval()
    return model

def input_fn(request_body, content_type="application/json"):
    data = json.loads(request_body)
    return torch.tensor(data["inputs"]).float()

def predict_fn(input_data, model):
    with torch.no_grad():
        logits = model(input_data)
        probs = torch.softmax(logits, dim=-1)
        return probs.numpy().tolist()

def output_fn(prediction, accept="application/json"):
    return json.dumps({"probs": prediction}), accept
