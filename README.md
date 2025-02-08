# Essay Writer

A minimal Python-based essay writer package for students. Generate comprehensive essays for literally any topic with a simple command or Python script.

---

## Usage

```bash
pip install essay-writer
```

### CLI Usage

```bash
python -m essay_writer --topic "The Solar System"
```

On the first run, the CLI will prompt you to enter your `OPENAI_API_KEY` which will get stored for future use.

Alternatively, you can reset your API key using the following command.

```bash
python -m essay_writer --set-key "your-openai-api-key"
```

You could also request a re-prompt by using the `-r` flag.

```bash
python -m essay_writer -r --topic "The Solar System"
```

### Package Usage

First install the package.

```bash
pip install essay-writer
```

Then, simply import the package and call the `write_essay` method.

```python
from essay_writer import EssayWriter

## If you don't set the OPENAI_API_KEY, it will read the OPENAI_API_KEY variable from your .env file
writer = EssayWriter(keys={"OPENAI_API_KEY": "test-key" })

solar_system_essay = writer.write_essay(topic="The Solar System", format="markdown")

print(solar_system_essay)

```

---

## Motivation and Objectives

- Demonstrate essay writing capabilities using Generative AI and Python Programming.
- Help our students learn Python Programming, improve their understanding of Generative AI, and write better essays.
- Provide a simple, re-usable interface to integrate specialized essay writing capabilities into Generative AI applications.
- Serve as a research tool for researchers, and teachers to study essay generation, software design, and programming techniques to create sophisticated writing applications.

---

## Contributions

We welcome contributions from developers around the globe. The steps to contribute are simple:

- Fork the repository.
- Create a new branch with your changes.
- Submit a PR to this repository.
- Complete the PR review process with our team.

---

## License

Essay Writer is distributed under the MIT License. Refer to the [LICENSE](https://github.com/thehackersplaybook/essay-writer/blob/main/LICENSE) file for full details.
