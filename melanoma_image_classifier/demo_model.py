import cv2
import numpy as np
import torch
from net_class import Net
import warnings
warnings.filterwarnings("ignore")

def apply_model(path):

    print("WARNING! DISCLAIMER! DON'T USE THIS FOR REAL MEDICAL ADVICE!!!!")
    print("THIS IS JUST A PROGRAMMING TUTORIAL. GO TO A REAL DOCTOR IF YOU THINK YOU MIGHT HAVE MELANOMA!")
    print()

    # 50x50 pixels
    img_size = 50

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, (img_size,img_size))

    img_array = np.array(img)

    img_array = img_array / 255

    img_array = torch.Tensor(img_array)

    net = Net()
    net.load_state_dict(torch.load("saved_model.pth"))
    net.eval()


    net_out = net(img_array.view(-1, 1, img_size,img_size))[0]



    if net_out[0] >= net_out[1]:
        print()
        print()
        print("Prediction: BENIGN")
        print(f"Confidence: {round(float(net_out[0]),3)}")
        print()
        print()
    else:
        print()
        print()
        print("Prediction: MELANOMA")
        print(f"Confidence: {round(float(net_out[1]),3)}")
        print()
        print()


