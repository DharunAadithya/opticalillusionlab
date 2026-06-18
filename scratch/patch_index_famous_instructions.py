import os
import re

def patch_index():
    filepath = "src/pages/index.astro"
    if not os.path.exists(filepath):
        print(f"{filepath} not found")
        return
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    index_data = {
        "Poggendorff Illusion": {
            "ins": "Align your eyes with the black diagonal line. Drag the overlap slider to see if the two segments align.",
            "exp": "The Poggendorff Illusion is a geometrical-optical distortion where a diagonal line segment is interrupted by a vertical block. The brain misjudges the angle of the segment, making the two halves appear misaligned. This occurs because the visual system processes obtuse angles as larger and acute angles as smaller than they physically are."
        },
        "Adelson Checkerboard": {
            "ins": "Look at tiles A and B. Click 'Verify' to remove the background and check if they have the same shade of gray.",
            "exp": "Adelson's Checkerboard shows that the brain does not measure raw surface luminance; it evaluates colors relative to lighting. Because Tile B is inside the shadow cast by the cylinder, the visual cortex automatically scales its perceived brightness up, making it look white compared to Tile A."
        },
        "Color Spheres Illusion": {
            "ins": "Observe the spheres. Click 'Remove Lines' to see that they are actually the exact same shade of gray.",
            "exp": "The Color Spheres (Munker-White) illusion is caused by chromatic assimilation. The color of the foreground stripes bleeds into our perception of the gray spheres behind them, tricking our visual cortex into resolving them as red, blue, or green."
        },
        "Curvature Blindness": {
            "ins": "Scan your eyes across the lines. Drag the overlap slider to see if the zig-zag curves are actually smooth wavy lines.",
            "exp": "Curvature Blindness occurs because our brain processes curves and corners differently. The visual system groups segments by vertex contrast: when the vertex highlights align with the curvature, it groups them as smooth waves; when they contrast, it groups them as sharp zig-zag corners."
        },
        "Kanizsa Triangle": {
            "ins": "Stare at the center. Do you see a bright white triangle floating on top of the pac-man shapes?",
            "exp": "The Kanizsa Triangle is a Gestalt illusion showing boundary completion. The visual cortex fills in non-existent contours between the pac-man mouths and circles because it prefers to construct a complete, overlapping white triangle in the foreground."
        },
        "Troxler Fading": {
            "ins": "Stare at the central cross for 20 seconds. The pink dots will fade away and be replaced by a green afterimage.",
            "exp": "Troxler Fading shows neural adaptation. Receptors in your peripheral vision adapt to static, unchanging stimuli and stop firing, making peripheral details dissolve into the background. It works best with blurry edges that do not stimulate eye micro-saccades."
        },
        "Expanding Hole": {
            "ins": "Stare at the black center core. The dark void will appear to expand outward, swallowing the screen.",
            "exp": "The Expanding Hole illusion triggers a physiological response. The dark radial gradient mimics entering a dark tunnel, causing your pupils to dilate. The visual cortex interprets this dilation as forward motion, making the black hole appear to expand."
        },
        "Breathing Square": {
            "ins": "Focus on the blue square. Click 'Toggle Rotating Grid' to see why your brain thinks it's pulsing.",
            "exp": "The Breathing Square shows how background frames distort motion perception. The rotating yellow grid skews your frame of reference; the brain struggles to integrate the corners of the blue square with the moving grid, interpreting the rotation as expansion and contraction."
        },
        "Reverse Spoke Illusion": {
            "ins": "Focus on the center. Stare as the background spins, and watch the spoke wheel rotate in reverse.",
            "exp": "The Reverse Spoke illusion is a motion adaptation effect. Continuous exposure to the spinning spiral fatigue direction-sensitive MT/V5 cells. When you look at the wheel, opposite motion vectors dominate, simulating reverse spoke rotation."
        },
        "Afterimage Light Bulb": {
            "ins": "Stare at the red dot in the light bulb for 30s. Then focus on the white screen to see the yellow afterimage.",
            "exp": "Staring at the black bulb exhausts rods and cones in your retina. Shifting gaze to white triggers the rested receptors (responsible for yellow) to fire faster in comparison, creating a complementary yellow afterimage."
        },
        "Ishihara Color Test": {
            "ins": "Look at the circles of dots. Identify the number hidden in the pattern, then click 'Reveal Answer'.",
            "exp": "The Ishihara test uses pseudoisochromatic plates to screen for red-green color blindness. It hides numbers within dots of varying sizes and chromatic values, which can only be segregated if the visual system contains functioning L and M cone photoreceptors."
        },
        "Pinna-Brelstaff Illusion": {
            "ins": "Focus on the center dot. Move your head closer to the screen and back. The concentric circles will appear to rotate.",
            "exp": "The Pinna-Brelstaff illusion is a peripheral drift effect. The tilted, high-contrast micro-tiles stimulate direction-selective visual pathways as you move your head closer or further, translating radial scaling into perceived rotation."
        }
    }

    for name, info in index_data.items():
        # Find card heading
        title_idx = content.find(name)
        if title_idx == -1:
            print(f"Index Card {name} not found")
            continue
        
        # We need to find the demo-area class relative to title_idx
        demo_idx = content.find('class="demo-area', title_idx)
        if demo_idx == -1:
            demo_idx = content.find('class="group-hover', title_idx) # fallback
            
        if demo_idx != -1:
            # We want to insert the Instruction Box above demo_idx
            # Let's find the start tag <div class="demo-area... or <div class="group-hover...
            start_tag_idx = content.rfind('<div', title_idx, demo_idx)
            if start_tag_idx != -1:
                ins_box = f"""
        <!-- Instruction Box -->
        <div class="my-3 flex items-start gap-2 rounded-xl border border-indigo-500/10 bg-indigo-500/5 p-3 text-xs text-slate-350 text-left">
          <span class="text-base leading-none">👁️</span>
          <div>
            <strong class="text-slate-200">Instructions:</strong> {info['ins']}
          </div>
        </div>
"""
                content = content[:start_tag_idx] + ins_box + content[start_tag_idx:]
                print(f"Patched index.astro card {name} with instructions")
                
                # Now we want to insert the collapsible explanation at the bottom of the card.
                # The card is an anchor <a> which ends with </a>.
                # Let's find the next </a> after start_tag_idx
                # We find it by searching from start_tag_idx + len(ins_box) + 300
                close_a_idx = content.find('</a>', start_tag_idx + len(ins_box) + 200)
                if close_a_idx != -1:
                    exp_box = f"""
        <!-- Collapsible Explanation -->
        <details class="w-full mt-4 border-t border-slate-800/40 pt-3 text-xs text-slate-400 select-none text-left">
          <summary class="font-bold cursor-pointer hover:text-purple-400">👁️ Reveal Answer & Science</summary>
          <p class="mt-2 font-normal leading-relaxed text-slate-400">
            {info['exp']}
          </p>
        </details>
"""
                    content = content[:close_a_idx] + exp_box + content[close_a_idx:]
                    print(f"Patched index.astro card {name} with explanation details")
                else:
                    print(f"Could not find closing <a> tag for index.astro card {name}")
            else:
                print(f"Could not find demo-area start tag for index.astro card {name}")
        else:
            print(f"Could not find demo-area for index.astro card {name}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("index.astro patched successfully!")

def patch_famous():
    filepath = "src/pages/famous.astro"
    if not os.path.exists(filepath):
        print(f"{filepath} not found")
        return
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    famous_instructions = {
        "Spinning Dancer": "Observe the dancer's silhouette. Is she spinning clockwise or counter-clockwise? Toggle the helper belt to help focus.",
        "Rubin's Vase": "Stare at the center. Do you see a classic vase, or two dark profiles facing each other?",
        "Penrose Triangle": "Scan the corners of the triangle. Can you trace the impossible connections that loop forever?",
        "The Dress": "Observe the dress. Do you see it as blue/black, or white/gold? Cast your vote below.",
        "Müller-Lyer": "Compare the horizontal line segments. Click 'Verify' to see if the arrowheads are tricking your brain.",
        "Café Wall": "Look at the grey lines between the black and white tiles. Click 'Verify' to see if they are actually parallel.",
        "Necker Cube": "Stare at the wireframe cube. Observe how its orientation flips back and forth in your mind.",
        "Kanizsa Triangle": "Stare at the center. Notice how your brain constructs a bright white triangle out of the three pac-man shapes.",
        "Ponzo Illusion": "Compare the yellow horizontal bars between the railroad tracks. Click 'Verify' to slide them next to each other.",
        "Zöllner Illusion": "Observe the main diagonal lines. Click 'Verify' to see if the short crossing hashes are tricking you.",
        "Ames Room": "Observe the two figures standing in the corners. Watch how they swap sizes as they walk across the room.",
        "Hollow Face": "Move your cursor left and right. The hollow mask will appear to rotate and follow you.",
        "Rotating Snakes": "Stare at the center of one circle. The surrounding circles will appear to spin in your peripheral vision.",
        "Fraser Spiral": "Follow the spiral lines with your cursor. Click 'Verify' to see if they are concentric circles.",
        "Hermann Grid": "Look around the grid. Ghostly dark dots will flicker at the white path intersections in your periphery.",
        "Penrose Stairs": "Observe the dot walking the stairs. Trace the loop to see why it can climb forever without getting higher.",
        "Shepard Tables": "Compare the two tables. Click 'Verify (Overlay Tables)' to see if they are identical parallelograms.",
        "Coffer Illusion": "Find the 16 circles hidden in the grid of rectangular frames. Enter your guess to reveal them.",
        "Vertical-Horizontal": "Compare the vertical red line and horizontal blue line. Click 'Rotate' to check if they are identical in length.",
        "McGurk Effect": "Play the audio. Observe the mouth shape: does the visual coordinate make you hear DA instead of BA?"
    }

    for name, ins in famous_instructions.items():
        title_idx = content.find(f"<span>{name}</span>")
        if title_idx == -1:
            title_idx = content.find(name)
            
        if title_idx == -1:
            print(f"Famous Card {name} not found")
            continue
            
        demo_idx = content.find('class="demo-area', title_idx)
        if demo_idx != -1:
            # We want to find the tag <div class="demo-area...
            start_tag_idx = content.rfind('<div', title_idx, demo_idx)
            if start_tag_idx != -1:
                ins_box = f"""
        <!-- Instruction Box -->
        <div class="my-3 flex items-start gap-2 rounded-xl border border-indigo-500/10 bg-indigo-500/5 p-3 text-xs text-slate-350 text-left">
          <span class="text-base leading-none">👁️</span>
          <div>
            <strong class="text-slate-200">Instructions:</strong> {ins}
          </div>
        </div>
"""
                content = content[:start_tag_idx] + ins_box + content[start_tag_idx:]
                print(f"Patched famous.astro card {name} with instructions")
            else:
                print(f"Could not find demo-area start tag for famous.astro card {name}")
        else:
            print(f"Could not find demo-area for famous.astro card {name}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("famous.astro patched successfully!")

patch_index()
patch_famous()
