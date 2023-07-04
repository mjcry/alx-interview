#!/usr/bin/python3
"""Script will unlock list of lists"""

def canUnlockAll(boxes):
    keys = [0]
    visited = set(keys)  # Track visited boxes to avoid redundant iterations

    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in visited and boxKey < len(boxes):
                keys.append(boxKey)
                visited.add(boxKey)

    return len(keys) == len(boxes)
