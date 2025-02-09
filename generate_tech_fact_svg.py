import json
import random
import textwrap

# Load tech facts from JSON file
with open("tech-facts.json", "r", encoding="utf-8") as file:
    tech_facts = json.load(file)

# Pick a random fact
selected_fact = random.choice(tech_facts)["fact"]

# Define character width estimation
char_width = 9  # Adjusted for better accuracy
max_chars_per_line = 50  # Wrap lines after 50 characters

# Wrap text for width adjustment
wrapped_text = textwrap.fill(selected_fact, width=max_chars_per_line)
fact_lines = wrapped_text.split("\n")

# Find longest line to determine optimal width
longest_line = max(fact_lines, key=len)
text_width = len(longest_line) * char_width  # Estimate text width
box_width = text_width + 40  # Add just enough padding
svg_width = box_width + 20  # Add 20px extra for rounded corners

# Convert text into <tspan> for multiline support
svg_fact_text = ""
y_position = 60
for line in fact_lines:
    svg_fact_text += f'<text class="fact-text" x="30" y="{y_position}">{line}</text>\n'
    y_position += 24  # Line spacing

# Adjust height dynamically
box_height = y_position + 10
svg_height = box_height + 10

# Read the template SVG and replace placeholders
with open("tech-facts-template.svg", "r", encoding="utf-8") as file:
    svg_template = file.read()

updated_svg = (svg_template
    .replace("{fact_lines}", svg_fact_text)
    .replace("{box_width}", str(box_width))
    .replace("{box_height}", str(box_height))
    .replace("{svg_width}", str(svg_width))
    .replace("{svg_height}", str(svg_height))
)

# Write the updated SVG file
with open("tech-fact.svg", "w", encoding="utf-8") as file:
    file.write(updated_svg)

print("✅ tech-fact.svg updated successfully!")