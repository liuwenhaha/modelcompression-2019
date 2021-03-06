import sys
import os

sys.path.append(os.path.abspath('../'))

import pruning
from fasterrcnn.resnet import MaskedFasterRCNN

if __name__ == '__main__':
    r = MaskedFasterRCNN(('__background__',  # always index 0
                         'aeroplane', 'bicycle', 'bird', 'boat',
                         'bottle', 'bus', 'car', 'cat', 'chair',
                         'cow', 'diningtable', 'dog', 'horse',
                         'motorbike', 'person', 'pottedplant',
                         'sheep', 'sofa', 'train', 'tvmonitor'),
                         model_path='C:\\Users\\Ahraz\\Documents\\mastersthesis\\masters-thesis-2019\\models\\resnet101.pth')
    
    r.create_architecture()

    masks = pruning.methods.weight_prune(r, 80.)
    r.set_mask(masks)
    pruning.methods.prune_rate(r)

    for name, child in r.named_children():
        if name == 'RCNN_base':
            pruning.methods.quantize_k_means(child, show_figures=True)