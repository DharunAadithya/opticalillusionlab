import os

pages_dir = "c:/Users/Amrutha/Documents/opticalillusionlab/src/pages"
illusions_dir = os.path.join(pages_dir, "illusions")

# Pre-defined templates and information for all 22 detail pages
pages_data = [
    {
        "slug": "waterfall-effect",
        "title": "Waterfall Effect",
        "category": "Motion",
        "difficulty": "🟢 Easy",
        "discoverer": "Robert Addams (1834)",
        "svg": """<svg class="w-48 h-48 animate-[spin_10s_linear_infinite]" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" fill="none" stroke="#3b82f6" stroke-width="2" />
            <path d="M 50,50 L 50,5 A 45,45 0 0,1 81.8,18.2 Z" fill="#1e1b4b" opacity="0.3" />
            <path d="M 50,50 L 95,50 A 45,45 0 0,1 81.8,81.8 Z" fill="#1e1b4b" opacity="0.3" />
            <path d="M 50,50 L 50,95 A 45,45 0 0,1 18.2,81.8 Z" fill="#1e1b4b" opacity="0.3" />
            <path d="M 50,50 L 5,50 A 45,45 0 0,1 18.2,18.2 Z" fill="#1e1b4b" opacity="0.3" />
            <circle cx="50" cy="50" r="3" fill="#ef4444" />
          </svg>""",
        "explanation": "The Waterfall Effect is one of the classic motion aftereffects in visual psychology. When a person stares continuously at a downward moving stimulus, such as a cascading waterfall, the motion-sensitive neurons in the visual cortex (specifically area MT/V5) that detect downward movement become adapted and fatigued. When the observer then looks at a stationary object, the downward-detecting neurons fire at a rate below their normal baseline. Consequently, the upward-detecting neurons, which are fully rested, fire relatively faster in comparison. The brain interprets this imbalance as upward motion, causing the stationary scene to appear to drift upward. This demonstrates that human motion perception is coded via opponent-process channels that continuously calibrate our balance of sight.",
    },
    {
        "slug": "motion-aftereffect",
        "title": "Motion Aftereffect",
        "category": "Motion",
        "difficulty": "🟡 Medium",
        "discoverer": "Aristotle (350 BC)",
        "svg": """<svg class="w-48 h-48 animate-[spin_5s_linear_infinite]" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" fill="none" stroke="#ec4899" stroke-width="3" />
            <path d="M 50,50 C 30,30 20,50 50,5" fill="none" stroke="#ec4899" stroke-width="2" />
            <path d="M 50,50 C 70,30 80,50 95,50" fill="none" stroke="#ec4899" stroke-width="2" />
            <path d="M 50,50 C 70,70 80,50 50,95" fill="none" stroke="#ec4899" stroke-width="2" />
            <path d="M 50,50 C 30,70 20,50 5,50" fill="none" stroke="#ec4899" stroke-width="2" />
            <circle cx="50" cy="50" r="3.5" fill="#eab308" />
          </svg>""",
        "explanation": "The Motion Aftereffect (MAE) is a sensory illusion experienced after staring at a moving visual pattern for a brief period (usually 20 to 30 seconds) and then focusing on a stationary target. First documented by Aristotle in his treatise Parva Naturalia, the illusion causes the stationary target to appear to move in the opposite direction of the original motion. The neurological basis for the MAE lies in the adaptation of direction-selective neurons in the middle temporal visual area (MT/V5) of the brain. When these neurons become fatigued, their resting discharge rates drop. When you shift your gaze to a static image, the non-adapted neurons representing the opposite direction fire at their standard rate, generating a phantom movement signal. This serves as key evidence of the comparative computational models used by our brains to translate light into direction.",
    },
    {
        "slug": "ouchi-illusion",
        "title": "Ouchi Illusion",
        "category": "Motion",
        "difficulty": "🔴 Hard",
        "discoverer": "Hajime Ouchi (1977)",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-900 border border-slate-700" viewBox="0 0 100 100">
            <defs>
              <pattern id="ouchi-horiz" width="8" height="8" patternUnits="userSpaceOnUse">
                <rect width="4" height="8" fill="#ffffff" />
                <rect x="4" width="4" height="8" fill="#000000" />
              </pattern>
              <pattern id="ouchi-vert" width="8" height="8" patternUnits="userSpaceOnUse">
                <rect width="8" height="4" fill="#ffffff" />
                <rect y="4" width="8" height="4" fill="#000000" />
              </pattern>
            </defs>
            <rect width="100" height="100" fill="url(#ouchi-horiz)" />
            <circle cx="50" cy="50" r="25" fill="url(#ouchi-vert)" stroke="#ef4444" stroke-width="1.5" class="animate-bounce" />
          </svg>""",
        "explanation": "The Ouchi Illusion is a famous peripheral drift illusion named after Japanese artist Hajime Ouchi. It consists of a central circular disk of perpendicular stripes floating over a background grid. When you move your eyes or scroll the page, the central circle appears to shake, float, or slide independently of the background. This effect occurs because of how the brain processes horizontal and vertical edges. The primary visual cortex divides the image into two orthogonal motion channels. Because the eye's natural micro-movements (saccades) occur in all directions, they trigger contrasting motion signals along the horizontal and vertical boundaries. The brain fails to coordinate these perpendicular signals, leading it to segment the circle as a separate 3D layer that is sliding across the page.",
    },
    {
        "slug": "enigma-illusion",
        "title": "Enigma Illusion",
        "category": "Motion",
        "difficulty": "💀 Expert",
        "discoverer": "Isia Leviant (1981)",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-900" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" fill="none" stroke="#ffffff" stroke-dasharray="1,2" stroke-width="40" />
            <circle cx="50" cy="50" r="30" fill="none" stroke="#eab308" stroke-width="4" class="animate-pulse" />
            <circle cx="50" cy="50" r="20" fill="none" stroke="#3b82f6" stroke-width="3" />
            <circle cx="50" cy="50" r="4" fill="#ef4444" />
          </svg>""",
        "explanation": "The Enigma Illusion, designed by Isia Leviant in 1981, features radiating spokes overlaying concentric rings. When looking at the image, observers report a rapid, circular flow or shimmering movement along the rings, despite the visual being entirely static. For decades, visual scientists debated whether the effect originated in the retina or the brain. In 2008, neuroscientists discovered that the illusion is driven by tiny, involuntary eye movements called micro-saccades. These movements shift the radial lines across the retina, generating transient signals that the visual cortex (area MT) interprets as continuous motion along the circular rings. This demonstrates how motor activity and sensory processing are deeply integrated in visual comprehension.",
    },
    {
        "slug": "levitating-ball",
        "title": "Levitating Ball",
        "category": "Motion",
        "difficulty": "🔴 Hard",
        "discoverer": "Visual Science",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-950" viewBox="0 0 100 100">
            <!-- Background checkerboard lines -->
            <line x1="10" y1="90" x2="90" y2="90" stroke="#334155" stroke-width="3" />
            <!-- Shadow (moving left and right to simulate height) -->
            <ellipse cx="50" cy="88" rx="12" ry="4" fill="#000000" opacity="0.6" class="animate-[pulse_3s_ease-in-out_infinite]" />
            <!-- The ball -->
            <circle cx="50" cy="50" r="10" fill="url(#ball-grad)" />
            <defs>
              <radialGradient id="ball-grad" cx="40%" cy="40%" r="60%">
                <stop offset="0%" stop-color="#fb7185" />
                <stop offset="100%" stop-color="#be123c" />
              </radialGradient>
            </defs>
          </svg>""",
        "explanation": "The Levitating Ball is a classic demonstration of motion parallax and depth cues. A sphere is placed in a static position on the screen, while a dark shadow moves back and forth underneath it. Even though the ball does not move a single pixel, the brain perceives the ball as rising, falling, and levitating in 3D space. This illusion occurs because the brain relies on the relative position of shadows to compute depth and distance in a 3D environment. When the shadow moves further away from the ball, the brain applies the size-distance rule, concluding that the ball must be rising. When the shadow aligns directly underneath the ball, it appears to rest on the floor. This highlights that our perception of height and position is highly contextual.",
    },
    {
        "slug": "whites-illusion",
        "title": "White's Illusion",
        "category": "Color",
        "difficulty": "🟡 Medium",
        "discoverer": "Michael White (1979)",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-100" viewBox="0 0 100 100">
            <!-- Black and white stripes -->
            <rect x="0" y="0" width="100" height="15" fill="#000" />
            <rect x="0" y="30" width="100" height="15" fill="#000" />
            <rect x="0" y="60" width="100" height="15" fill="#000" />
            <rect x="0" y="90" width="100" height="10" fill="#000" />
            <!-- Gray test patches -->
            <rect x="25" y="10" width="12" height="25" fill="#7f7f7f" />
            <rect x="65" y="25" width="12" height="25" fill="#7f7f7f" />
          </svg>""",
        "explanation": "White's Illusion is a powerful brightness illusion described by Michael White in 1979. It consists of identical gray rectangles placed on a background of alternating black and white stripes. Some gray blocks sit on the black stripes, while others sit on the white stripes. Surprisingly, the gray blocks on the black stripes appear significantly darker than the gray blocks on the white stripes. This is counter-intuitive because standard lateral inhibition predicts that a dark background should make the gray block appear lighter. Instead, the brain groups the gray blocks with the stripes they interrupt, demonstrating that high-level grouping and Gestalt continuity override local retinal contrast calculations.",
    },
    {
        "slug": "simultaneous-contrast",
        "title": "Simultaneous Contrast",
        "category": "Color",
        "difficulty": "🟢 Easy",
        "discoverer": "Michel Eugène Chevreul (1839)",
        "svg": """<svg class="w-48 h-48 select-none" viewBox="0 0 120 100">
            <rect x="0" y="0" width="60" height="100" fill="#1e293b" />
            <rect x="60" y="0" width="60" height="100" fill="#cbd5e1" />
            <rect x="20" y="40" width="20" height="20" fill="#f97316" />
            <rect x="80" y="40" width="20" height="20" fill="#f97316" />
          </svg>""",
        "explanation": "Simultaneous Contrast was first documented in detail by French chemist Michel Eugène Chevreul in 1839. It occurs when two identical color patches are placed against different colored backgrounds. For example, two identical orange squares will look completely different if one is placed on a dark blue background and the other on a light gray background. The square on the dark background appears brighter and more saturated, while the square on the light background appears washed out and darker. This occurs because the visual system processes colors comparatively rather than absolutely, using lateral inhibition in the retina to enhance contrast and color boundaries.",
    },
    {
        "slug": "wife-mother-in-law",
        "title": "My Wife and My Mother-in-Law",
        "category": "Ambiguous",
        "difficulty": "🟡 Medium",
        "discoverer": "W. E. Hill (1915)",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-900 rounded-xl" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="40" fill="none" stroke="#e2e8f0" stroke-width="2" />
            <!-- Simplified representation of profile contour -->
            <path d="M 35,30 C 45,30 55,25 57,20 C 59,15 57,10 55,5" fill="none" stroke="#e2e8f0" stroke-width="2" />
            <circle cx="41" cy="18" r="2.5" fill="#f59e0b" />
          </svg>""",
        "explanation": "My Wife and My Mother-in-Law is one of the most famous bistable ambiguous figures. Popularized by cartoonist W. E. Hill in 1915, the drawing contains both a young woman facing away into the background and an old woman looking downward in profile. The visual cortex experiences a rivalry between the two interpretations because the same line segments represent different facial features in each version: the young woman's chin functions as the old woman's nose, the young woman's ear acts as the old woman's eye, and the young woman's necklace is perceived as the old woman's mouth. This demonstrates that object recognition is a top-down prediction process.",
    },
    {
        "slug": "all-is-vanity",
        "title": "All is Vanity",
        "category": "Ambiguous",
        "difficulty": "🔴 Hard",
        "discoverer": "Charles Allan Gilbert (1892)",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-950" viewBox="0 0 100 100">
            <ellipse cx="50" cy="45" rx="30" ry="32" fill="#ffffff" />
            <circle cx="38" cy="42" r="10" fill="#020617" />
            <circle cx="62" cy="42" r="10" fill="#020617" />
            <path d="M 40,70 L 60,70" stroke="#020617" stroke-width="3" stroke-dasharray="1,1" />
          </svg>""",
        "explanation": "All is Vanity is a classic ambiguous composite drawing created by American illustrator Charles Allan Gilbert in 1892. It depicts a young woman sitting at a vanity mirror, looking at her reflection. However, when viewed from a distance, the entire scene blends to form the shape of a human skull. The round vanity mirror forms the dome of the skull, the woman's head and its reflection form the dark eye sockets, and the perfume bottles and cosmetics on the table form the row of teeth along the jaw. This illusion demonstrates how the visual system groups high-frequency detail (the woman and cosmetics) and low-frequency structures (the skull) differently based on viewing distance and focus.",
    },
    {
        "slug": "duck-rabbit",
        "title": "Duck-Rabbit Illusion",
        "category": "Ambiguous",
        "difficulty": "🟢 Easy",
        "discoverer": "Joseph Jastrow (1899)",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-950 rounded-xl" viewBox="0 0 100 100">
            <ellipse cx="55" cy="55" rx="28" ry="20" fill="none" stroke="#fff" stroke-width="2" />
            <circle cx="33" cy="50" r="18" fill="none" stroke="#fff" stroke-width="2" />
            <path d="M 17,42 Q 0,38 -5,45 M 17,50 Q 0,52 -5,58" fill="none" stroke="#fff" stroke-width="2" />
            <circle cx="28" cy="45" r="2.5" fill="#fff" />
          </svg>""",
        "explanation": "The Duck-Rabbit Illusion is a classic ambiguous figure popularized by psychologist Joseph Jastrow in 1899. The silhouette is bistable: it can be seen as a duck facing to the left (where the protrusions are its bill) or a rabbit facing to the right (where the same protrusions are its ears). The visual system cannot hold both interpretations in conscious awareness simultaneously, forcing a perceptual toggle. Jastrow used the illusion to demonstrate that perception is not a passive recording of sensory data, but an active, cognitive interpretation that is heavily influenced by mental focus, context, and semantic priming.",
    },
    {
        "slug": "boring-figure",
        "title": "Boring Figure",
        "category": "Ambiguous",
        "difficulty": "🟡 Medium",
        "discoverer": "Edwin Boring (1930)",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-900" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="40" fill="none" stroke="#fff" stroke-width="2" />
            <path d="M 30,50 Q 50,20 70,50" fill="none" stroke="#fff" stroke-width="2" />
          </svg>""",
        "explanation": "The Boring Figure is another name for the classic Wife and Mother-in-Law illusion. It is named after American psychologist Edwin Boring, who published a detailed analysis of the drawing in 1930. Boring used the figure to map out the mathematical boundaries of visual bistability and investigate how the brain assigns outlines to different shapes. The illusion demonstrates how the visual cortex alternates between two completely separate semantic frameworks when interpreting identical visual contours.",
    },
    {
        "slug": "hidden-faces-trees",
        "title": "6 Hidden Faces in Trees",
        "category": "Ambiguous",
        "difficulty": "🔴 Hard",
        "discoverer": "Visual Folklore",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-950" viewBox="0 0 100 100">
            <path d="M 20,95 L 45,30 L 50,95 M 80,95 L 55,20 L 50,95" fill="none" stroke="#10b981" stroke-width="2.5" />
            <path d="M 45,55 C 48,50 52,48 50,42" fill="none" stroke="#ef4444" stroke-width="2" />
          </svg>""",
        "explanation": "The 6 Hidden Faces in Trees is a popular ambiguous puzzle that exploits the brain's tendency toward pareidolia—our natural urge to find human faces and familiar shapes in random patterns. The branches and trunks of the trees are drawn such that their negative spaces and bark contours trace the profiles of human faces. Because the brain's fusiform face area (FFA) is highly specialized to detect face configurations, it actively scans the forest outlines, assembling the profiles out of the raw branches. This shows how top-down face processing override works.",
    },
    {
        "slug": "skull-coffee",
        "title": "Coffee Skull Illusion",
        "category": "Ambiguous",
        "difficulty": "🔴 Hard",
        "discoverer": "Modern Visual Art",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-900" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="40" fill="#78350f" />
            <circle cx="50" cy="50" r="35" fill="#fef08a" opacity="0.35" />
            <circle cx="40" cy="45" r="8" fill="#78350f" />
            <circle cx="60" cy="45" r="8" fill="#78350f" />
          </svg>""",
        "explanation": "The Coffee Skull is a modern ambiguous figure where the foam patterns in a cup of coffee form a skull. The dark coffee liquid represents the empty eye sockets and nose cavity, while the surrounding light foam forms the bone structure and teeth. Like the Salvador Dalí and Charles Allan Gilbert skull illusions, this highlights how our visual system matches raw contrast boundaries to familiar cognitive templates. The brain toggles between seeing a cup of espresso and a human skull.",
    },
    {
        "slug": "hidden-tiger",
        "title": "Hidden Tiger Illusion",
        "category": "Ambiguous",
        "difficulty": "🟡 Medium",
        "discoverer": "Visual Puzzle",
        "svg": """<svg class="w-48 h-48 select-none bg-amber-500" viewBox="0 0 100 100">
            <rect width="100" height="100" fill="#f59e0b" />
            <path d="M 10,10 L 90,90 M 90,10 L 10,90" stroke="#000" stroke-width="4" stroke-dasharray="2,8" />
          </svg>""",
        "explanation": "The Hidden Tiger is a classic visual puzzle where a tiger is standing in a forest, but a second tiger is hidden in the stripes of the first tiger. Specifically, the words 'the hidden tiger' are spelled out along the tiger's side stripes. This illusion demonstrates how semantic text patterns can be hidden within natural biological patterns, requiring the visual cortex to switch from object/pattern recognition to text reading to solve the puzzle.",
    },
    {
        "slug": "impossible-elephant",
        "title": "Impossible Elephant",
        "category": "Impossible",
        "difficulty": "🔴 Hard",
        "discoverer": "Roger Shepard (1990)",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-950" viewBox="0 0 100 100">
            <rect x="20" y="30" width="60" height="40" fill="none" stroke="#fff" stroke-width="2" />
            <line x1="30" y1="70" x2="30" y2="90" stroke="#fff" stroke-width="2" />
            <line x1="45" y1="70" x2="45" y2="90" stroke="#fff" stroke-width="2" />
            <line x1="60" y1="70" x2="60" y2="90" stroke="#fff" stroke-width="2" />
            <line x1="75" y1="70" x2="75" y2="90" stroke="#fff" stroke-width="2" />
          </svg>""",
        "explanation": "The Impossible Elephant (also known as L'egs-istential Dread) is an impossible object created by cognitive scientist Roger Shepard. The drawing depicts an elephant with a normal body, but its legs and feet are drawn inconsistently. The blank space between its legs is drawn as feet, while the actual legs end in blank space. The brain tries to construct a 3D model of the elephant but experiences cognitive friction because the contour lines are shared between the positive shapes (legs) and negative spaces (gaps), leading to a paradox.",
    },
    {
        "slug": "old-woman-young-woman",
        "title": "Old Woman / Young Woman",
        "category": "Ambiguous",
        "difficulty": "🟡 Medium",
        "discoverer": "Visual Psychology",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-900" viewBox="0 0 100 100">
            <path d="M 35,30 C 45,30 55,25 57,20 C 59,15 57,10 55,5" fill="none" stroke="#fff" stroke-width="2" />
          </svg>""",
        "explanation": "This detail page features the classic Old Woman / Young Woman drawing. It demonstrates visual bistability, where a single drawing displays two different women depending on which contours are prioritized by the brain's early visual processing. The young woman's neckband represents the old woman's mouth, her chin acts as the old woman's nose, and her ear represents the old woman's eye. The visual system flips between these two interpretations dynamically.",
    },
    {
        "slug": "duck-squirrel",
        "title": "Duck or Squirrel",
        "category": "Ambiguous",
        "difficulty": "🔴 Hard",
        "discoverer": "Modern Bistable Art",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-900" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="30" fill="none" stroke="#fff" stroke-width="2" />
            <path d="M 20,40 Q 5,42 0,50 Q 5,58 20,60" fill="none" stroke="#fff" stroke-width="2" />
          </svg>""",
        "explanation": "The Duck or Squirrel is an ambiguous bistable drawing where the duck's beak forms the squirrel's tail when the focus is reversed. Because the shape of a duck's body and a squirrel's body share similar curves, the brain switches between both interpretations based on contextual clues. This demonstrates how semantic templates are stored and activated in the lateral temporal lobes.",
    },
    {
        "slug": "skull-women",
        "title": "Skull or Women at a Table",
        "category": "Ambiguous",
        "difficulty": "🔴 Hard",
        "discoverer": "Salvador Dalí Style",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-950" viewBox="0 0 100 100">
            <ellipse cx="50" cy="45" rx="30" ry="32" fill="#fff" />
            <circle cx="38" cy="42" r="10" fill="#000" />
            <circle cx="62" cy="42" r="10" fill="#000" />
          </svg>""",
        "explanation": "This page showcases the Salvador Dalí style 'Skull or Women at a Table' illusion. The shape of a human skull is formed by the layout of two women sitting next to each other at a circular table. The brain groups the women and the table as a single low-frequency shape (a skull) when viewed from a distance, but zooms into the individual high-frequency elements (the women) when examined closely.",
    },
    {
        "slug": "saxophonist-woman",
        "title": "Saxophonist or Woman's Face",
        "category": "Ambiguous",
        "difficulty": "🟡 Medium",
        "discoverer": "Figure-Ground Study",
        "svg": """<svg class="w-48 h-48 select-none bg-indigo-950" viewBox="0 0 100 100">
            <path fill="#fff" d="M 10,10 L 10,90 L 50,90 Q 40,70 30,50 Q 45,30 10,10 Z" />
            <path fill="#312e81" d="M 50,90 L 90,90 L 90,10 L 50,10 Q 55,30 65,50 Q 55,70 50,90 Z" />
          </svg>""",
        "explanation": "The Saxophonist or Woman's Face is a classic figure-ground bistable drawing. The left side of the drawing (white) depicts a jazz saxophonist in profile, while the right side (dark blue) outlines a woman's face looking to the left. The brain experiences rivalry because the central outline serves as the boundary for both shapes, but the brain can only assign the boundary to one figure at a time.",
    },
    {
        "slug": "penguin-cat",
        "title": "Penguin or Cat",
        "category": "Ambiguous",
        "difficulty": "🟢 Easy",
        "discoverer": "Graphic Design",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-950" viewBox="0 0 100 100">
            <ellipse cx="50" cy="60" rx="30" ry="35" fill="#1e293b" />
            <ellipse cx="50" cy="62" rx="20" ry="25" fill="#f1f5f9" />
            <ellipse cx="50" cy="20" rx="20" ry="18" fill="#1e293b" />
          </svg>""",
        "explanation": "The Penguin or Cat is a minimalist ambiguous graphic. A single dark silhouette is drawn with waddling flippers and waddling feet (forming a penguin) but also contains cat ears and whiskers (forming a cat). The visual system resolves the ambiguous features using semantic associations, highlighting that object perception is contextual and memory-based.",
    },
    {
        "slug": "three-dots-motion",
        "title": "Three Dots Motion Binding",
        "category": "Motion",
        "difficulty": "🔴 Hard",
        "discoverer": "Visual Neuroscience",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-950" viewBox="0 0 100 100">
            <circle cx="30" cy="70" r="5" fill="#eab308" class="animate-ping" />
            <circle cx="70" cy="70" r="5" fill="#eab308" class="animate-ping" />
            <circle cx="50" cy="35" r="5" fill="#eab308" class="animate-ping" />
          </svg>""",
        "explanation": "Three Dots Motion Binding is a visual illusion where dots moving in separate circular paths are perceived as moving together in a rigid, lateral, or rocking motion. This occurs because the visual cortex (specifically area MT/V5) tries to bind separate visual elements into a single coherent object. By tracking the dots collectively, the brain assumes a global translation instead of separate local rotations.",
    },
    {
        "slug": "seasonal-duck-rabbit",
        "title": "Seasonal Duck or Rabbit",
        "category": "Ambiguous",
        "difficulty": "🟡 Medium",
        "discoverer": "Seasonal Bias Study",
        "svg": """<svg class="w-48 h-48 select-none bg-slate-950" viewBox="0 0 100 100">
            <ellipse cx="55" cy="55" rx="28" ry="20" fill="none" stroke="#fff" stroke-width="2" />
            <circle cx="33" cy="50" r="18" fill="none" stroke="#fff" stroke-width="2" />
            <path d="M 17,42 Q 0,38 -5,45 M 17,50 Q 0,52 -5,58" fill="none" stroke="#fff" stroke-width="2" />
            <circle cx="28" cy="45" r="2.5" fill="#fff" />
            <path d="M 20,80 Q 50,85 80,80" fill="none" stroke="#3b82f6" stroke-width="1.5" />
          </svg>""",
        "explanation": "The Seasonal Duck or Rabbit is a psychological study of cognitive priming. Research shows that observers are more likely to see the rabbit first around Easter (spring) and the duck first in October (autumn). This demonstrates that our visual interpretations are not purely feedforward; they are constantly primed by semantic associations, current environmental events, and memory.",
    }
]

# Write all 22 pages
for data in pages_data:
    filename = f"{data['slug']}.astro"
    filepath = os.path.join(illusions_dir, filename)
    
    # Check if file exists, don't overwrite if it was already created or we just want to create new ones
    if os.path.exists(filepath):
        print(f"File already exists, skipping: {filename}")
        continue

    content = f"""---
// src/pages/illusions/{filename}
import Layout from '../../layouts/Layout.astro';
---

<Layout 
  title="{data['title']} — Optical Illusion Lab" 
  description="Explore the science, history, and visual parameters of the {data['title']} optical illusion."
>
  <div class="py-12 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto space-y-12">
    <!-- Breadcrumb back navigation -->
    <nav class="flex text-xs font-black uppercase tracking-wider text-slate-400 space-x-2 pb-2 border-b border-indigo-500/10">
      <a href="/" class="hover:text-white transition-colors">Home</a>
      <span>/</span>
      <span class="text-purple-400">{data['title']}</span>
    </nav>

    <!-- Hero Header -->
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 pb-6">
      <div class="space-y-3">
        <div class="flex items-center space-x-2">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 uppercase tracking-wider">{data['category']}</span>
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-purple-500/10 text-purple-400 border border-purple-500/20 uppercase tracking-wider">{data['difficulty']}</span>
        </div>
        <h1 class="font-display text-4xl sm:text-5xl font-black tracking-tight text-slate-900 dark:text-white">
          {data['title']}
        </h1>
        <p class="text-slate-600 dark:text-slate-350 text-base max-w-2xl font-medium">
          Discover how the brain interprets this fascinating {data['category'].lower()} visual puzzle.
        </p>
      </div>
    </div>

    <!-- LARGE INTERACTIVE DEMO -->
    <div class="flex flex-col items-center justify-center py-6 border-b border-indigo-500/10">
      <div class="w-full max-w-[600px] mx-auto space-y-4">
        <div class="relative flex flex-col items-center justify-center h-96 w-full bg-slate-100 dark:bg-slate-950/40 rounded-xl overflow-hidden border border-indigo-500/10 p-6">
          {data['svg']}
        </div>
      </div>
    </div>

    <!-- Content Split Layout -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-12 pt-4">
      <!-- Left 2-Columns -->
      <div class="lg:col-span-2 space-y-10">
        <section class="space-y-4">
          <h2 class="font-display text-2xl font-black text-slate-900 dark:text-white flex items-center space-x-2">
            <span class="text-purple-500">🧠</span>
            <span>THE SCIENCE</span>
          </h2>
          <div class="prose prose-indigo dark:prose-invert text-slate-700 dark:text-slate-300 leading-relaxed text-xs sm:text-sm font-semibold text-justify">
            <p>{data['explanation']}</p>
          </div>
        </section>
      </div>

      <!-- Right Column -->
      <div class="space-y-8">
        <section class="rounded-3xl border border-indigo-950/20 bg-slate-900/60 p-6 space-y-4 shadow-xl">
          <h3 class="font-display text-lg font-black text-slate-900 dark:text-white flex items-center space-x-2">
            <span class="text-purple-500">📜</span>
            <span>HISTORY</span>
          </h3>
          <p class="text-xs sm:text-sm text-slate-650 dark:text-slate-355 leading-relaxed font-semibold">
            First described by {data['discoverer']}. It remains a fundamental demonstration of perceptual processing and cognitive framing.
          </p>
        </section>
      </div>
    </div>
  </div>
</Layout>
"""
    with open(filepath, "w", encoding="utf-8") as f:
      f.write(content)
    print(f"Created page: {filename}")

print("All missing detail pages created successfully!")
