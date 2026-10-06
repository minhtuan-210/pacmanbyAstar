class Node:
    def __init__(self, position, parent=Node, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    # Định nghĩa cho phép so sánh để dùng trong hàng đợi ưu tiên 
    def __lt__(self, other):
        return self.f < other.f

def load_map_from_string(map_str):
    grid = []
    start_pos = None
    end_pos = None 

    lines = map_str.split().split('\n')

    for x, line in enumerate(lines):
        row = []
        for y, char in enumerate(line): 
            if char == '%':
                row.append(1) 
                # 1 là tường 
            else:
                row.append(0)
                # 0 là đường đi 

                if char == 'p':
                    start_pos = (x,y)
                elif char == "F":
                    end_pos = (x,y)

#DO: thiết kế bản đồ mẫu