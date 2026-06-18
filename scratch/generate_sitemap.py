import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def generate_sitemap():
    base_url = "https://opticalillusionlab.pages.dev"
    pages_dir = "c:/Users/Amrutha/Documents/opticalillusionlab/src/pages"
    sitemap_path = "c:/Users/Amrutha/Documents/opticalillusionlab/public/sitemap.xml"
    
    urls = []
    
    # 1. Main pages
    main_pages = [
        "",
        "famous",
        "moving",
        "hidden",
        "for-kids",
        "color",
        "test",
        "what-do-you-see",
        "drawings",
        "generator",
        "how-they-work",
        "about",
        "contact",
        "privacy-policy",
        "terms"
    ]
    for p in main_pages:
        urls.append({
            "loc": f"{base_url}/{p}" if p else f"{base_url}/",
            "priority": "1.0" if not p else "0.8",
            "changefreq": "weekly" if p not in ["privacy-policy", "terms"] else "monthly"
        })
        
    # 2. Illusion Detail pages
    illusions_dir = os.path.join(pages_dir, "illusions")
    if os.path.exists(illusions_dir):
        files = os.listdir(illusions_dir)
        for f in sorted(files):
            if f.endswith(".astro"):
                slug = f[:-6]
                # Skip deleted/unwanted ones
                if slug in ["the-dress", "motion-binding", "three-dots-motion"]:
                    continue
                urls.append({
                    "loc": f"{base_url}/illusions/{slug}",
                    "priority": "0.6",
                    "changefreq": "monthly"
                })

    # Create XML
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for u in urls:
        url_el = ET.SubElement(urlset, "url")
        loc_el = ET.SubElement(url_el, "loc")
        loc_el.text = u["loc"]
        
        lastmod_el = ET.SubElement(url_el, "lastmod")
        lastmod_el.text = "2026-06-18"
        
        changefreq_el = ET.SubElement(url_el, "changefreq")
        changefreq_el.text = u["changefreq"]
        
        priority_el = ET.SubElement(url_el, "priority")
        priority_el.text = u["priority"]

    xml_str = ET.tostring(urlset, encoding="utf-8")
    parsed_xml = minidom.parseString(xml_str)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")
    
    # Remove extra empty lines from toprettyxml
    pretty_xml = "\n".join([line for line in pretty_xml.splitlines() if line.strip()])
    
    with open(sitemap_path, "w", encoding="utf-8") as sf:
        sf.write(pretty_xml)
        
    print(f"Generated sitemap with {len(urls)} URLs at {sitemap_path}")

if __name__ == "__main__":
    generate_sitemap()
