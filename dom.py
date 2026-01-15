from typing import List, Dict

JS_SCRIPT = """
() => {
  const elements = [];
  let id = 0;

  function isVisible(el) {
    const rect = el.getBoundingClientRect();
    return rect.width > 0 && rect.height > 0;
  }

  const candidates = document.querySelectorAll(
    'a, button, input, textarea, select'
  );

  for (const el of candidates) {
    if (!isVisible(el)) continue;

    elements.push({
      id: "el_" + id++,
      tag: el.tagName.toLowerCase(),
      text: el.innerText || "",
      placeholder: el.placeholder || "",
      type: el.type || "",
    });

    el.setAttribute("data-agent-id", elements[elements.length - 1].id);
  }

  return elements;
}
"""

def extract_elements(page) -> List[Dict]:
    return page.evaluate(JS_SCRIPT)
