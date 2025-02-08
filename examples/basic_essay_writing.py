from essay_writer import EssayWriter


writer = EssayWriter(model="gpt-4o")

topic = "The impact of artificial intelligence on aged people."

essay = writer.write_essay(topic=topic, format="plain-text")

print("Generated essay on:", topic)
print(essay)
