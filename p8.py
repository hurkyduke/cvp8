import cv2
import numpy as np

# Create a black image
image_size = 900
image = np.ones((image_size, image_size, 3), dtype=np.uint8)

# Define cube vertices
cube_vertices = np.array([[100, 100, 100], [400, 100, 100], [400, 400, 100],
                          [100, 400, 100], [100, 100, 400], [400, 100, 400],
                          [400, 400, 400], [100, 400, 400]], dtype=np.float32)

# Define cube edges
cube_edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
              (0, 4), (1, 5), (2, 6), (3, 7)]

# Colors for each face of the cube
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Rotation angles
angle_x = 0
angle_y = 0
angle_z = 0

# Rotation matrix function
def get_rotation_matrix(angle_x, angle_y, angle_z):
    rotation_x = np.array([[1, 0, 0],
                           [0, np.cos(angle_x), -np.sin(angle_x)],
                           [0, np.sin(angle_x), np.cos(angle_x)]])

    rotation_y = np.array([[np.cos(angle_y), 0, np.sin(angle_y)],
                           [0, 1, 0],
                           [-np.sin(angle_y), 0, np.cos(angle_y)]])

    rotation_z = np.array([[np.cos(angle_z), -np.sin(angle_z), 0],
                           [np.sin(angle_z), np.cos(angle_z), 0],
                           [0, 0, 1]])

    rotation_matrix = rotation_x.dot(rotation_y).dot(rotation_z)
    return rotation_matrix

# Create a window
cv2.namedWindow('3D Rotating Cube')

while True:
    # Clear the image
    image.fill(0)

    # Rotate cube vertices
    rotation_matrix = get_rotation_matrix(angle_x, angle_y, angle_z)
    rotated_vertices = cube_vertices.dot(rotation_matrix.T)

    # Draw cube edges
    for edge in cube_edges:
        start_point = tuple(rotated_vertices[edge[0], :2].astype(int))
        end_point = tuple(rotated_vertices[edge[1], :2].astype(int))
        color = colors[cube_edges.index(edge) % len(colors)]
        cv2.line(image, start_point, end_point, color, 2)

    # Display the image
    cv2.imshow('3D Rotating Cube', image)

    # Check for keyboard events
    key = cv2.waitKey(30) & 0xFF

    # Exit when 'ESC' is pressed
    if key == 27:
        break

    # Update rotation angles based on keyboard input
    if key == ord('w'):
        angle_x += 0.1
    elif key == ord('s'):
        angle_x -= 0.1
    elif key == ord('a'):
        angle_y += 0.1
    elif key == ord('d'):
        angle_y -= 0.1
    elif key == ord('q'):
        angle_z += 0.1
    elif key == ord('e'):
        angle_z -= 0.1

cv2.destroyAllWindows()
