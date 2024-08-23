import sys

H = 3
N = 10000

# Границы кластеров
CLUSTER_1_X_MIN = 0
CLUSTER_1_Y_MIN = 0
CLUSTER_2_X_MIN = 5
CLUSTER_2_Y_MIN = 4
CLUSTER_3_X_MIN = 2
CLUSTER_3_Y_MIN = 7.5

def get_abs(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def is_in_cluster(x_min, y_min, x, y):
    return x_min <= x <= x_min + H and y_min <= y <= y_min + H

def get_centroid(points):
    min_sum = sys.maxsize
    centroid = (0, 0)
    for i in range(len(points)):
        total_distance = 0
        for j in range(len(points)):
            total_distance += get_abs(points[i][0], points[i][1], points[j][0], points[j][1])
        if total_distance < min_sum:
            min_sum = total_distance
            centroid = points[i]
    return centroid

def solve():
    cluster_1_points = []
    cluster_2_points = []
    cluster_3_points = []

    for _ in range(N):
        x, y = map(float, input().split())
        if is_in_cluster(CLUSTER_1_X_MIN, CLUSTER_1_Y_MIN, x, y):
            cluster_1_points.append((x, y))
        elif is_in_cluster(CLUSTER_2_X_MIN, CLUSTER_2_Y_MIN, x, y):
            cluster_2_points.append((x, y))
        else:
            cluster_3_points.append((x, y))

    c_1 = get_centroid(cluster_1_points)
    c_2 = get_centroid(cluster_2_points)
    c_3 = get_centroid(cluster_3_points)

    avg_x = (c_1[0] + c_2[0] + c_3[0]) / 3
    avg_y = (c_1[1] + c_2[1] + c_3[1]) / 3

    print(avg_x * 10000)
    print(avg_y * 10000)

if __name__ == "__main__":
    solve()
