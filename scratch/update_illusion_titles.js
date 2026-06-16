const fs = require('fs');
const path = require('path');

const dir = path.join(__dirname, '..', 'src', 'pages', 'illusions');
const files = fs.readdirSync(dir).filter(f => f.endsWith('.astro'));

files.forEach(file => {
  const filePath = path.join(dir, file);
  let content = fs.readFileSync(filePath, 'utf8');

  // Match: title="Something — Optical Illusion Lab" or title='Something — Optical Illusion Lab'
  // Support both en-dash (–), em-dash (—), and standard hyphen (-)
  const titleRegex = /title=["']([^"']+)["']/;
  const match = content.match(titleRegex);

  if (match) {
    const fullTitle = match[1];
    // Split by dash/hyphen
    const parts = fullTitle.split(/[-–—]/);
    if (parts.length > 1) {
      const name = parts[0].trim();
      const newTitle = `${name} — Interactive Optical Illusion | Optical Illusion Lab`;
      console.log(`File: ${file} | Old: "${fullTitle}" | New: "${newTitle}"`);
      
      // Replace title attribute
      const newContent = content.replace(
        /title=["']([^"']+)["']/,
        `title="${newTitle}"`
      );
      fs.writeFileSync(filePath, newContent, 'utf8');
    } else {
      console.log(`File: ${file} | Couldn't parse title: "${fullTitle}"`);
    }
  } else {
    console.log(`File: ${file} | No title match found`);
  }
});
console.log("Finished updating titles!");
