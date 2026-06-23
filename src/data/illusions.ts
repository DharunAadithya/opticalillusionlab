export type IllusionCategory =
  | 'geometric'
  | 'color'
  | 'ambiguous'
  | 'impossible'
  | 'motion'
  | 'neural'
  | 'cognitive';

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
  { slug: 'adelsons-checkerboard', title: "Adelson's Checkerboard", category: 'color', difficulty: 'medium', type: 1, section: '/color', description: 'Two tiles look different but share the exact same gray reflectance.' },
  { slug: 'whites-illusion', title: "White's Illusion", category: 'color', difficulty: 'medium', type: 1, section: '/color', description: 'Identical gray bars look different on black vs white stripe backgrounds.' },
  { slug: 'simultaneous-contrast', title: 'Simultaneous Contrast', category: 'color', difficulty: 'easy', type: 1, section: '/color', description: 'Identical color patches look different on contrasting backgrounds.' },
  { slug: 'color-spheres', title: 'Color Spheres', category: 'color', difficulty: 'hard', type: 1, section: '/color', description: 'Gray circles appear red, blue, and green due to chromatic assimilation.' },
  { slug: 'rubins-vase', title: "Rubin's Vase", category: 'ambiguous', difficulty: 'easy', type: 3, section: '/famous', description: 'See a vase or two faces in profile — one image, two readings.' },
  { slug: 'duck-rabbit', title: 'Duck-Rabbit', category: 'ambiguous', difficulty: 'easy', type: 3, section: '/hidden', description: 'One drawing reads as a duck or a rabbit depending on grouping.' },
  { slug: 'old-woman-young-woman', title: 'Old Woman / Young Woman', category: 'ambiguous', difficulty: 'medium', type: 3, section: '/what-do-you-see', description: 'W.E. Hill figure: young woman or old woman in profile.' },
  { slug: 'wife-mother-in-law', title: 'My Wife and My Mother-in-Law', category: 'ambiguous', difficulty: 'medium', type: 3, section: '/hidden', description: 'Classic bistable portrait with shared contour lines.' },
  { slug: 'spinning-dancer', title: 'Spinning Dancer', category: 'ambiguous', difficulty: 'medium', type: 3, section: '/famous', description: 'Silhouette appears to spin clockwise or counter-clockwise.' },
  { slug: 'penrose-triangle', title: 'Penrose Triangle', category: 'impossible', difficulty: 'hard', type: 1, section: '/famous', description: 'An impossible triangle that cannot exist in three dimensions.' },
  { slug: 'penrose-stairs', title: 'Penrose Stairs', category: 'impossible', difficulty: 'hard', type: 1, section: '/famous', description: 'A staircase that endlessly ascends yet returns to its start.' },
  { slug: 'impossible-trident', title: 'Impossible Trident', category: 'impossible', difficulty: 'hard', type: 1, section: '/famous', description: 'Three prongs become two cylinders — a figure-ground paradox.' },
  { slug: 'rotating-snakes', title: 'Rotating Snakes', category: 'motion', difficulty: 'medium', type: 4, section: '/moving', description: 'Static rings appear to spin — zero animation in the code.' },
  { slug: 'pinna-brelstaff', title: 'Pinna-Brelstaff', category: 'motion', difficulty: 'medium', type: 4, section: '/moving', description: 'Concentric rings appear to rotate when you move your head.' },
  { slug: 'afterimage-stare', title: 'Complementary Afterimage', category: 'neural', difficulty: 'hard', type: 2, section: '/color', description: 'Stare at a colored cross; afterimage appears in your eyes only.' },
  { slug: 'troxler-fading', title: 'Troxler Fading', category: 'neural', difficulty: 'medium', type: 2, section: '/', description: 'Peripheral dots fade during steady fixation — a neural adaptation effect.' },
  { slug: 'kanizsa-triangle', title: 'Kanizsa Triangle', category: 'cognitive', difficulty: 'easy', type: 1, section: '/famous', description: 'Pac-Man shapes suggest a white triangle that is not drawn.' },
  { slug: 'curvature-blindness', title: 'Curvature Blindness', category: 'cognitive', difficulty: 'medium', type: 1, section: '/', description: 'Angled line segments hide smooth curvature until revealed.' },
  { slug: 'reverse-spoke', title: 'Reverse Spoke', category: 'cognitive', difficulty: 'medium', type: 1, section: '/', description: 'Wheel spokes appear to rotate opposite to actual motion.' },
  { slug: 'wertheimer-koffka', title: 'Wertheimer-Koffka Ring', category: 'cognitive', difficulty: 'easy', type: 1, section: '/for-kids', description: 'Ring segments look different shades due to surrounding context.' },
  { slug: 'fraser-spiral', title: 'Fraser Spiral', category: 'cognitive', difficulty: 'medium', type: 1, section: '/famous', description: 'Concentric circles appear as a spiral due to tilted segments.' },
  { slug: 'coffer-illusion', title: 'Coffer Illusion', category: 'cognitive', difficulty: 'hard', type: 3, section: '/famous', description: 'Grid of circles hides a pattern of rectangular coffers.' },
  { slug: 'mcgurk-effect', title: 'McGurk Effect', category: 'cognitive', difficulty: 'medium', type: 1, section: '/famous', description: 'Vision changes what you hear — an audio-visual illusion.' },
];

export const CATEGORY_LABELS: Record<IllusionCategory, string> = {
  geometric: 'Geometric / Context',
  color: 'Color / Contrast',
  ambiguous: 'Ambiguous Figures',
  impossible: 'Impossible Objects',
  motion: 'Peripheral Motion',
  neural: 'Neural Adaptation',
  cognitive: 'Cognitive / Gestalt',
};

export const DIFFICULTY_COLORS: Record<IllusionDifficulty, string> = {
  easy: 'border-l-green-500',
  medium: 'border-l-yellow-500',
  hard: 'border-l-red-500',
};
