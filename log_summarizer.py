import os
import sys
from pathlib import Path

from openai import OpenAI


def summarize_log(log_file):
    log_path = Path(log_file)

    if not log_path.exists():
        print(f"Error: Log file '{log_file}' not found.")
        return

    log_text = log_path.read_text(
        encoding="utf-8",
        errors="replace"
    )

    if not log_text.strip():
        print("The log file is empty.")
        return

    # Keep the prompt within a reasonable size
    log_text = log_text[-12000:]

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.responses.create(
        model="gpt-6.2-astra",
        input=f"""
Summarize this build or test error log.

Include:
1. Error summary
2. Likely cause
3. Suggested solution

Do not invent information that is not present in the log.

ERROR LOG:
{log_text}
"""
    )

    print("\n===== BUILD ERROR SUMMARY =====\n")
    print(response.output_text)


if __name__ == "__main__":
    log_file = sys.argv[1] if len(sys.argv) > 1 else "build.log"
    summarize_log(log_file)