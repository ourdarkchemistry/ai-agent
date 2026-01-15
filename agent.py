import json
from browser import Browser
from dom import extract_elements
from llm import decide
from memory import Memory
from tools import resolve_selector

def main():
    goal = input("Введите задачу: ")

    browser = Browser()
    memory = Memory()

    browser.goto("https://google.com")

    while True:
        elements = extract_elements(browser.page)
        decision_raw = decide(goal, elements, str(memory))

        print("LLM:", decision_raw)

        decision = json.loads(decision_raw)
        action = decision["action"]

        if action == "finish":
            print("ГОТОВО:", decision.get("result"))
            break

        if action == "goto":
            browser.goto(decision["url"])

        if action == "click":
            selector = resolve_selector(browser.page, decision["element_id"])
            browser.click(selector)

        if action == "type":
            selector = resolve_selector(browser.page, decision["element_id"])
            browser.type(selector, decision["text"])

        memory.add(decision_raw)

if __name__ == "__main__":
    main()
