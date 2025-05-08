from transformers import pipeline

# Load the summarization pipeline (this may download the model the first time)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text: str) -> str:
    """
    Summarizes input text using a transformer model.

    Args:
        text (str): The raw or filtered input text.

    Returns:
        str: A summarized version of the input.
    """
    if not text.strip():
        return "No content to summarize."

    # Hugging Face models work best with texts <1024 tokens (~500-700 words)
    result = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return result[0]['summary_text']


# Test blockm
if __name__ == "__main__":
    input_text = "AI can summarize large texts. Cybersecurity is important in 2025. Python is used in automation and data science. Machine learning is a core field in AI. Ethical hacking is vital for modern infrastructure."
    summary = summarize_text(input_text)
    print("Summary:\n", summary)
