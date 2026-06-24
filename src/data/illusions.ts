export type IllusionCategory =
  | 'geometric'
  | 'color'
  | 'ambiguous'
  | 'impossible'
  | 'motion'
  | 'neural'
  | 'cognitive'
  | 'hidden';

export type IllusionDifficulty = 'easy' | 'medium' | 'hard';

export interface IllusionEntry {
  slug: string;
  title: string;
  category: IllusionCategory;
  difficulty: IllusionDifficulty;
  type: 1 | 2 | 3 | 4;
  section: string;
  description: string;
}

export const ILLUSIONS: IllusionEntry[] = [
  { slug: 'muller-lyer', title: 'Müller-Lyer', category: 'geometric', difficulty: 'medium', type: 1, section: '/famous', description: 'Identical line segments appear different lengths due to arrowhead context.' },
  { slug: 'ebbinghaus', title: 'Ebbinghaus Circles', category: 'geometric', difficulty: 'easy', type: 1, section: '/famous', description: 'A central circle looks larger or smaller depending on surrounding circles.' },
  { slug: 'cafe-wall', title: 'Café Wall', category: 'geometric', difficulty: 'medium', type: 1, section: '/famous', description: 'Parallel horizontal lines appear tilted due to offset mortar joints.' },
  { slug: 'hermann-grid', title: 'Hermann Grid', category: 'geometric', difficulty: 'easy', type: 1, section: '/famous', description: 'Ghost dots appear at grid intersections in peripheral vision.' },
  { slug: 'zoellner-illusion', title: 'Zöllner Illusion', category: 'geometric', difficulty: 'medium', type: 1, section: '/famous', description: 'Parallel lines look slanted when crossed by short diagonal hatch marks.' },
  { slug: 'ponzo-illusion', title: 'Ponzo Illusion', category: 'geometric', difficulty: 'easy', type: 1, section: '/famous', description: 'Identical bars look different sizes inside converging railroad tracks.' },
  { slug: 'delboeuf', title: 'Delboeuf Illusion', category: 'geometric', difficulty: 'easy', type: 1, section: '/famous', description: 'Identical inner circles appear different sizes inside different outer rings.' },
  { slug: 'poggendorff', title: 'Poggendorff Illusion', category: 'geometric', difficulty: 'medium', type: 1, section: '/', description: 'A diagonal line appears misaligned when interrupted by a vertical bar.' },
  { slug: 'vertical-horizontal', title: 'Vertical-Horizontal', category: 'geometric', difficulty: 'easy', type: 1, section: '/famous', description: 'A vertical line looks longer than an equal horizontal line.' },
  { slug: 'whites-illusion', title: "White's Illusion", category: 'color', difficulty: 'medium', type: 1, section: '/color', description: 'Identical gray bars look different on black vs white stripe backgrounds.' },
  { slug: 'simultaneous-contrast', title: 'Simultaneous Contrast', category: 'color', difficulty: 'easy', type: 1, section: '/color', description: 'Identical color patches look different on contrasting backgrounds.' },
  { slug: 'color-spheres', title: 'Color Spheres', category: 'color', difficulty: 'hard', type: 1, section: '/color', description: 'Gray circles appear red, blue, and green due to chromatic assimilation.' },
  { slug: 'rubin-vase', title: "Rubin's Vase", category: 'hidden', difficulty: 'easy', type: 3, section: '/hidden', description: 'See a vase or two faces in profile — one image, two readings.' },
  { slug: 'duck-rabbit', title: 'Duck-Rabbit', category: 'hidden', difficulty: 'easy', type: 3, section: '/hidden', description: 'One drawing reads as a duck or a rabbit depending on grouping.' },
  { slug: 'my-wife-and-my-mother', title: 'My Wife and My Mother-in-Law', category: 'hidden', difficulty: 'medium', type: 3, section: '/hidden', description: 'Classic bistable portrait with shared contour lines.' },
  { slug: 'hidden-tiger', title: 'Tiger in the Bamboo', category: 'hidden', difficulty: 'hard', type: 3, section: '/hidden', description: 'A camouflaged forest scene hiding a complete tiger in its vertical lines.' },
  { slug: 'faces-in-tree', title: 'Faces in the Tree', category: 'hidden', difficulty: 'hard', type: 3, section: '/hidden', description: 'Look at branches and roots to find five hidden human profiles.' },
  { slug: 'dalmatian-dog', title: 'Camouflaged Dalmatian', category: 'hidden', difficulty: 'hard', type: 3, section: '/hidden', description: 'A sniffing Dalmatian dog emerges from a field of high-contrast black spots.' },
  { slug: 'hidden-arrow', title: 'Hidden Arrow', category: 'hidden', difficulty: 'medium', type: 3, section: '/hidden', description: 'Spot the arrow shape hidden in the negative space of a geometric pattern.' },
  { slug: 'hidden-face-pattern', title: 'Hidden Face in Pattern', category: 'hidden', difficulty: 'hard', type: 3, section: '/hidden', description: 'A human face is hidden in the lines and textures of a natural pattern.' },
  { slug: 'spinning-dancer', title: 'Spinning Dancer', category: 'ambiguous', difficulty: 'medium', type: 3, section: '/famous', description: 'Silhouette appears to spin clockwise or counter-clockwise.' },
  { slug: 'penrose-triangle', title: 'Penrose Triangle', category: 'impossible', difficulty: 'hard', type: 1, section: '/famous', description: 'An impossible triangle that cannot exist in three dimensions.' },
  { slug: 'penrose-stairs', title: 'Penrose Stairs', category: 'impossible', difficulty: 'hard', type: 1, section: '/famous', description: 'A staircase that endlessly ascends yet returns to its start.' },
  { slug: 'impossible-trident', title: 'Impossible Trident', category: 'impossible', difficulty: 'hard', type: 1, section: '/famous', description: 'Three prongs become two cylinders — a figure-ground paradox.' },
  { slug: 'rotating-snakes', title: 'Rotating Snakes', category: 'motion', difficulty: 'medium', type: 4, section: '/moving', description: 'Static rings appear to spin — zero animation in the code.' },
  { slug: 'breathing-square', title: 'Breathing Square', category: 'motion', difficulty: 'medium', type: 4, section: '/moving', description: 'A rotating square behind occluders appears to expand and contract.' },
  { slug: 'pinna-brelstaff', title: 'Pinna-Brelstaff', category: 'motion', difficulty: 'medium', type: 4, section: '/moving', description: 'Concentric rings appear to rotate when you move your head.' },
  { slug: 'pulsing-grid', title: 'Pulsing Grid', category: 'motion', difficulty: 'medium', type: 4, section: '/moving', description: 'A high-contrast grid where intersections appear to breathe and pulse continuously.' },
  { slug: 'moving-circles', title: 'Moving Circles', category: 'motion', difficulty: 'medium', type: 4, section: '/moving', description: 'Concentric gears that seem to rotate slowly in your peripheral vision as you look around.' },
  { slug: 'afterimage-stare', title: 'Complementary Afterimage', category: 'neural', difficulty: 'hard', type: 2, section: '/color', description: 'Stare at a colored cross; afterimage appears in your eyes only.' },
  { slug: 'troxler-fading', title: 'Troxler Fading', category: 'neural', difficulty: 'medium', type: 2, section: '/', description: 'Peripheral dots fade during steady fixation — a neural adaptation effect.' },
  { slug: 'kanizsa-triangle', title: 'Kanizsa Triangle', category: 'cognitive', difficulty: 'easy', type: 1, section: '/famous', description: 'Pac-Man shapes suggest a white triangle that is not drawn.' },
  { slug: 'curvature-blindness', title: 'Curvature Blindness', category: 'cognitive', difficulty: 'medium', type: 1, section: '/', description: 'Angled line segments hide smooth curvature until revealed.' },
  { slug: 'reverse-spoke', title: 'Reverse Spoke', category: 'cognitive', difficulty: 'medium', type: 1, section: '/', description: 'Wheel spokes appear to rotate opposite to actual motion.' },
  { slug: 'wertheimer-koffka', title: 'Wertheimer-Koffka Ring', category: 'cognitive', difficulty: 'easy', type: 1, section: '/for-kids', description: 'Ring segments look different shades due to surrounding context.' },
  { slug: 'fraser-spiral', title: 'Fraser Spiral', category: 'cognitive', difficulty: 'medium', type: 1, section: '/famous', description: 'Concentric circles appear as a spiral due to tilted segments.' },
  { slug: 'coffer-illusion', title: 'Coffer Illusion', category: 'cognitive', difficulty: 'hard', type: 3, section: '/famous', description: 'Grid of circles hides a pattern of rectangular coffers.' },
];

export const CATEGORY_LABELS: Record<IllusionCategory, string> = {
  geometric: 'Geometric / Context',
  color: 'Color / Contrast',
  ambiguous: 'Ambiguous Figures',
  impossible: 'Impossible Objects',
  motion: 'Peripheral Motion',
  neural: 'Neural Adaptation',
  cognitive: 'Cognitive / Gestalt',
  hidden: 'Hidden Figures',
};

export const DIFFICULTY_COLORS: Record<IllusionDifficulty, string> = {
  easy: 'border-l-green-500',
  medium: 'border-l-yellow-500',
  hard: 'border-l-red-500',
};
