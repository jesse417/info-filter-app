def filter_text(text: str, keywords: list) -> str:
    keywords_lower = [k.lower() for k in keywords]
    lines = text.split(". ")
    filtered = [
        line for line in lines
        if any(keyword in line.lower() for keyword in keywords_lower)
    ]
    return ". ".join(filtered)

if __name__ == "__main__":
    test_text = "Python is great for automation. AI can summarize large texts. Cybersecurity is important in 2025."
    keywords = ["AI", "2025"]
    result = filter_text(test_text, keywords)
    print(result)
