from pathlib import Path

src = Path("C:\\Portfolio Site\\Index.html")
html = src.read_text(encoding="utf-8")

# 1. Make the skills layout three columns on desktop.
html = html.replace(
    ".skills-grid { display: grid; grid-template-columns: repeat(4, 1fr); border: 1px solid var(--line); background: var(--line); gap: 1px; }",
    ".skills-grid { display: grid; grid-template-columns: repeat(3, 1fr); border: 1px solid var(--line); background: var(--line); gap: 1px; }"
)

# 2. Remove the <br> that was becoming its own grid item.
html = html.replace("          <br>\n", "")

# 3. Keep the responsive behavior: 3 -> 2 -> 1 columns.
html = html.replace(
    "@media (max-width: 900px) {\n"
    "    .hero-grid, .about-grid, .split-grid { grid-template-columns: 1fr; }\n"
    "    .hero-aside { padding-top: 1rem; }\n"
    "    .skills-grid { grid-template-columns: 1fr 1fr; }",
    "@media (max-width: 900px) {\n"
    "    .hero-grid, .about-grid, .split-grid { grid-template-columns: 1fr; }\n"
    "    .hero-aside { padding-top: 1rem; }\n"
    "    .skills-grid { grid-template-columns: 1fr 1fr; }"
)

# 4. Fix the JavaScript error that was stopping the rest of the script from running.
html = html.replace(
    '  document.getElementById("availability").textContent = SITE.availability;\n',
    ''
)

# 5. Make the generated skills match the three languages shown in the page.
old_skills = '''  skills: [
    { name: "Languages", note: "Languages you use regularly.", items: ["C++", "Python"] },
    { name: "Web", note: "Frontend and web technologies.", items: ["HTML", "CSS", "JavaScript", "[Add more]"] },
    { name: "Tools", note: "Development tools and platforms.", items: ["Git", "GitHub", "[VS Code]", "[Add more]"] },
    { name: "Other", note: "Frameworks, APIs, systems, or concepts.", items: ["[Discord API]", "[Add more]", "[Add more]"] }
  ],'''

new_skills = '''  skills: [
    {
      name: "C++",
      note: "I have been working with C++ for about 2–3 years, and it is currently my favorite programming language.",
      items: []
    },
    {
      name: "Python",
      note: "I started learning Python early in my programming journey. While I don't use it as frequently anymore, I am comfortable with the language and familiar with its syntax and core concepts.",
      items: []
    },
    {
      name: "HTML & CSS",
      note: "I have experience with frontend development through my work with FaZe Media, college courses, and personal projects. I am comfortable building and styling interfaces, although frontend development is currently the area where I have the least experience.",
      items: []
    }
  ],'''

if old_skills in html:
    html = html.replace(old_skills, new_skills)

# 6. Hide the empty tag row so the three skill descriptions stay clean.
html = html.replace(
    '  .tags { display: flex; flex-wrap: wrap; gap: .45rem; }',
    '  .tags { display: flex; flex-wrap: wrap; gap: .45rem; }\n'
    '  .tags:empty { display: none; }'
)

out = Path("C:\Portfolio Site\Index-Final.html")
out.write_text(html, encoding="utf-8")

print(f"Fixed file created: {out}")
print("Changes: fixed the JavaScript error, made skills 3-column, removed the stray <br>, and updated the generated skills to C++, Python, and HTML & CSS.")
