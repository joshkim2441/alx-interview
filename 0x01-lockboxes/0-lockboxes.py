#!/bin/usr/python3

def canUnlockAll(boxes):
    opened_boxes = set([0])
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]

        for key in keys:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                queue.append(key)

    return len(opened_boxes) == len(boxes)
