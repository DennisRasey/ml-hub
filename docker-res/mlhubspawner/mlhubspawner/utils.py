"""
Shared util functions
"""

import math
import time

LABEL_NVIDIA_VISIBLE_DEVICES = 'nvidia_visible_devices'
LABEL_EXPIRATION_TIMESTAMP = 'expiration_timestamp_seconds'

def get_container_metadata(spawner):
    meta_information = []
    container_labels = spawner.get_labels()
    lifetime_timestamp = spawner.get_lifetime_timestamp(container_labels)
    if lifetime_timestamp != 0:
        difference_in_days = math.ceil((lifetime_timestamp - time.time())/60/60/24)
        meta_information.append("Expires: {}d".format(difference_in_days))
    
    nvidia_visible_devices = container_labels.get(LABEL_NVIDIA_VISIBLE_DEVICES, "")
    if nvidia_visible_devices != "":
        meta_information.append("GPUs: {}".format(nvidia_visible_devices))
    
    if len(meta_information) == 0:
        return ""
    
    return "({})".format(", ".join(meta_information))