const fs = require('fs');
const path = require('path');

const dir = path.join(__dirname, '..', 'src', 'pages', 'illusions');
const files = fs.readdirSync(dir).filter(f => f.endsWith('.astro'));

files.forEach(file => {
  const filePath = path.join(dir, file);
  let content = fs.readFileSync(filePath, 'utf8');

  // Find the H1 header content
  const h1Regex = /<h1[^>]*>\s*([\s\S]*?)\s*<\/h1>/;
  const h1Match = content.match(h1Regex);

  if (h1Match) {
    let name = h1Match[1].trim();
    // Remove any HTML tags inside the H1 if they exist
    name = name.replace(/<[^>]*>/g, '').replace(/\s+/g, ' ');

    const newTitle = `${name} — Interactive Optical Illusion | Optical Illusion Lab`;
    console.log(`File: ${file} | Resolved Name: "${name}" | New Title: "${newTitle}"`);

    // Replace the title attribute
    // We match title="..." or title='...'
    const newContent = content.replace(
      /title="[^"]*"|title='[^']*'/,
      `title="${newTitle}"`
    );
    fs.writeFileSync(filePath, newContent, 'utf8');
  } else {
    console.log(`File: ${file} | No <h1> match found!`);
  }
});
console.log("Finished fixing titles!");
