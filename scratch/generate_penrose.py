import math

# Isometric projection parameters
cos30 = math.cos(math.radians(30))
sin30 = math.sin(math.radians(30))

def project(x, y, z):
    # Standard isometric projection where:
    # X-axis projects to (-cos(30), sin(30))
    # Y-axis projects to (0, -1) (pointing up)
    # Z-axis projects to (cos(30), sin(30))
    u = -x * cos30 + z * cos30
    v = x * sin30 - y + z * sin30
    return u, v

def rotate_minus_30(u, v_coord):
    # Rotate by -30 degrees (clockwise):
    rad = math.radians(-30)
    ur = u * math.cos(rad) - v_coord * math.sin(rad)
    vr = u * math.sin(rad) + v_coord * math.cos(rad)
    return ur, vr

L = 150
T = 30

def get_box_faces(x_range, y_range, z_range):
    x0, x1 = x_range
    y0, y1 = y_range
    z0, z1 = z_range
    
    # Vertices
    v = {
        '000': (x0, y0, z0),
        '100': (x1, y0, z0),
        '010': (x0, y1, z0),
        '110': (x1, y1, z0),
        '001': (x0, y0, z1),
        '101': (x1, y0, z1),
        '011': (x0, y1, z1),
        '111': (x1, y1, z1),
    }
    
    # Faces defined by vertices
    faces = {
        'bottom': ('000', '100', '101', '001'),
        'top': ('010', '110', '111', '011'),
        'front_z': ('001', '101', '111', '011'),
        'back_z': ('000', '100', '110', '010'),
        'left_x': ('000', '010', '011', '001'),
        'right_x': ('100', '110', '111', '101'),
    }
    return v, faces

# Define the three beams.
# We want the loop to go:
# Z-beam (along Z): starts at (0, 0, 0) and ends at (0, 0, L)
# Y-beam (along Y): starts at (0, 0, L) and ends at (0, L, L)
# X-beam (along X): starts at (0, L, L) and ends at (L, L, L)
#
# Let's adjust thickness T.
bars = [
    # Z-beam (horizontal bottom bar on screen):
    # x: [0, T], y: [0, T], z: [0, L]
    get_box_faces((0, T), (0, T), (0, L)),
    
    # Y-beam (slanted up-right on screen):
    # x: [0, T], y: [0, L], z: [L-T, L]
    get_box_faces((0, T), (0, L), (L-T, L)),
    
    # X-beam (slanted up-left on screen):
    # x: [0, L], y: [L-T, L], z: [L-T, L]
    get_box_faces((0, L), (L-T, L), (L-T, L))
]

# Find bounds of all projected and rotated points
all_pts = []
for v, faces in bars:
    for pt in v.values():
        u, v_coord = project(*pt)
        ur, vr = rotate_minus_30(u, v_coord)
        all_pts.append((ur, vr))

min_u = min(p[0] for p in all_pts)
max_u = max(p[0] for p in all_pts)
min_v = min(p[1] for p in all_pts)
max_v = max(p[1] for p in all_pts)

width_2d = max_u - min_u
height_2d = max_v - min_v
center_u = (min_u + max_u) / 2
center_v = (min_v + max_v) / 2

scale = 220 / max(width_2d, height_2d)

def get_2d(x, y, z):
    u, v_coord = project(x, y, z)
    ur, vr = rotate_minus_30(u, v_coord)
    # Center in 300x300 canvas
    su = 150 + (ur - center_u) * scale
    sv = 150 + (vr - center_v) * scale
    return f"{su:.2f},{sv:.2f}"

def make_poly(v, faces_dict, face_name, fill):
    pts_3d = [v[key] for key in faces_dict[face_name]]
    points_str = " ".join(get_2d(*pt) for pt in pts_3d)
    return f'<polygon points="{points_str}" fill="{fill}" stroke="{fill}" stroke-width="0.5" />'

# Colors:
# - Top face: #FFFFFF
# - Left face: #8C8C8C
# - Right face: #2E2E2E
c_top = "#FFFFFF"
c_left = "#8C8C8C"
c_right = "#2E2E2E"

svg_elements = []

# Order of drawing to handle overlaps correctly:
# 1. Y-beam (along Y)
# 2. X-beam (along X)
# 3. Z-beam (along Z)

# --- Y-beam ---
v2, f2 = bars[1]
# Front-left face (z=L)
svg_elements.append(make_poly(v2, f2, 'front_z', c_left))
# Right face (x=T)
svg_elements.append(make_poly(v2, f2, 'right_x', c_right))

# --- X-beam ---
v3, f3 = bars[2]
# Top face (y=L)
svg_elements.append(make_poly(v3, f3, 'top', c_top))
# Front-left face (z=L)
svg_elements.append(make_poly(v3, f3, 'front_z', c_left))

# --- Z-beam ---
v1, f1 = bars[0]
# Top face (y=T)
svg_elements.append(make_poly(v1, f1, 'top', c_top))
# Right face (x=T)
svg_elements.append(make_poly(v1, f1, 'right_x', c_right))

svg_content = "\n  ".join(svg_elements)

html = f"""<!DOCTYPE html>
<html>
<body>
<svg width="400" height="400" viewBox="0 0 300 300" style="background:#f1f5f9;">
  {svg_content}
</svg>
</body>
</html>
"""

with open("scratch/preview.html", "w") as f:
    f.write(html)

print("Generated rotated -30 scratch/preview.html")
print(svg_content)
