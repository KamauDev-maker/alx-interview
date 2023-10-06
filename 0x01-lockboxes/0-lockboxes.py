#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.
    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

