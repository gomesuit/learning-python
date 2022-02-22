import deepl
import os

translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))

result = translator.translate_text(
    "How are you?",
    target_lang="JA",
)
print(result.text)
print(result.detected_source_lang)

result = translator.translate_text(
    "お元気ですか？",
    target_lang="EN-US",
)

print(result.text)
print(result.detected_source_lang)

# Check account usage
usage = translator.get_usage()
if usage.character.limit_exceeded:
    print("Character limit exceeded.")
else:
    print(f"Character usage: {usage.character.count} of {usage.character.limit}")
