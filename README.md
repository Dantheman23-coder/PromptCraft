# PromptCraft: Mastering Search and Prompt Engineering

**Description:**

This repository is your comprehensive guide to harnessing the power of search and prompt engineering to unlock the full potential of large language models (LLMs) like ChatGPT. Learn advanced search techniques to find the exact information you need and master the art of crafting effective prompts to elicit the desired responses from LLMs. Whether you're a researcher, writer, developer, or anyone seeking to leverage AI for creative, analytical, or technical tasks, **PromptCraft** provides the tools to optimize your LLM interactions.

## Table of Contents

1. [Introduction](#introduction)
2. [Mastering Search: Finding the Information You Need](#mastering-search)
   - [Basic Search Techniques](#basic-search-techniques)
   - [Advanced Search Techniques](#advanced-search-techniques)
   - [Specialized Search Techniques](#specialized-search-techniques)
3. [The Art of Prompt Engineering: Crafting Effective Instructions](#the-art-of-prompt-engineering)
   - [Principles of Prompt Engineering](#principles-of-prompt-engineering)
   - [Real-World Use Cases for Prompt Engineering](#real-world-use-cases-for-prompt-engineering)
4. [Advanced LLM Interactions: Taking Your Skills to the Next Level](#advanced-llm-interactions)
   - [Memory Syncing for Context and Personalization](#memory-syncing-for-context-and-personalization)
   - [Custom Instructions for Tailored Responses](#custom-instructions-for-tailored-responses)
   - [Multi-Turn Conversations for Deeper Exploration](#multi-turn-conversations-for-deeper-exploration)
5. [Ethical Considerations and Best Practices](#ethical-considerations-and-best-practices)
6. [Contributing](#contributing)
7. [License](#license)

---

## Introduction

Large language models (LLMs) are powerful AI systems capable of generating human-quality text, translating languages, writing creative content, and answering questions. However, interacting effectively requires more than asking simple questions. It requires an understanding of how these models process language, how to structure prompts for clarity, and how to leverage their unique capabilities. **PromptCraft** helps you master these skills and become proficient at guiding LLMs to deliver optimal results.

---

## Mastering Search: Finding the Information You Need

### Basic Search Techniques

| Technique | Usage | Example | Tip | Use Case |
|---|---|---|---|---|
| Keyword Search | Use keywords to find pages containing those words. | `AI ethics` | Use multiple keywords for a more specific search. | Finding articles about AI ethics. |
| Exact Match Search | Enclose keywords in quotes to find an exact match. | `"machine learning"` | Useful for finding specific phrases or titles. | Searching for a book titled "Machine Learning." |
| Exclusion Search | Use a minus sign (-) to exclude certain words from the search results. | `AI -ethics` | Helps to narrow down your search and remove irrelevant results. | Finding articles about AI that are not related to ethics. |
| Phrase Search | Use quotes to search for a specific phrase. | `"artificial intelligence"` | Useful for finding pages that contain a specific sequence of words. | Finding articles that mention the phrase "artificial intelligence." |
| Search Within a Specific Site | Use the `site:` operator to search within a specific website or domain. | `site:wikipedia.org AI` | Limits your search to a specific source. | Finding information about AI on Wikipedia. |
| OR Search | Use the `OR` operator to search for either one term or another. | `AI OR "machine learning"` | Broadens your search to include pages containing either term. | Finding articles that mention either AI or machine learning. |
| Wildcard Search | Use an asterisk (*) to represent unknown or variable words. | `AI * ethics` | Useful for finding variations of a word or phrase. | Finding articles about AI and ethics, regardless of the specific words used in between. |
| Range Search | Use two dots (..) to search for a range of numbers. | `2020..2024 AI` | Useful for finding information within a specific time frame. | Finding articles about AI published between 2020 and 2024. |

### Advanced Search Techniques

| Technique | Usage | Example | Tip | Use Case |
|---|---|---|---|---|
| Related Sites Search | Use `related:` to find websites related to a specific domain. | `related:nytimes.com` | Discover similar websites based on content and linking patterns. | Finding news websites similar to The New York Times. |
| File Type Search | Use `filetype:` to search for files of a specific type. | `filetype:pdf AI ethics` | Useful for finding research papers, reports, or presentations. | Finding PDF documents about AI ethics. |
| Title Search | Use `intitle:` to search for keywords in the title of web pages. | `intitle:"AI ethics"` | Focus your search on pages with specific keywords in the title. | Finding articles with "AI ethics" in the title. |
| URL Search | Use `inurl:` to search for keywords within the URL of web pages. | `inurl:ai ethics` | Useful for finding pages that focus on a specific topic. | Finding websites with "ai" and "ethics" in their URL. |
| Synonym Search | Use the tilde symbol (~) before a keyword to search for synonyms of that word. | `~AI ethics` | Broaden your search to include related concepts. | Finding articles about AI ethics using synonyms like "moral" or "responsible." |
| Number Range Search | Use two dots (..) to search for a range of numbers. | `10..100 employees AI` | Useful for finding companies or organizations within a specific size range. | Finding companies with 10 to 100 employees that use AI. |
| Define Search | Use `define:` to get the definition of a word or phrase. | `define:artificial intelligence` | Quickly find definitions without navigating to a dictionary website. | Getting a clear definition of artificial intelligence. |
| Weather Search | Use `weather:` followed by the location to get the current weather. | `weather:London` | Get up-to-date weather information for any location. | Checking the weather in London before traveling. |
| Cache Search | Use `cache:` to view a cached version of a web page. | `cache:example.com` | Access a snapshot of a web page as it appeared at a specific time. | Viewing an older version of a website that has since been updated. |
| Time Zone Search | Use `time:` followed by the location to get the current time in that area. | `time:Tokyo` | Get the current time in a different time zone. | Checking the time in Tokyo for a business call. |
| Calculator Functionality | Use the search bar as a calculator. | `10 + 12 * 2` | Perform quick calculations directly in the search bar. | Calculating a simple math problem. |
| Unit Conversion | Type the amount and units to get instant conversions. | `10 kilometers to miles` | Convert between different units of measurement. | Converting kilometers to miles for a road trip. |
| Stock Information Search | Type the stock ticker symbol to get real-time stock information. | `AAPL` | Get current stock prices and other financial data. | Checking the stock price of Apple. |
| Sports Scores | Enter the teams or league to obtain current sports scores. | `NBA scores` | Stay up-to-date on the latest sports results. | Checking the scores of NBA games. |
| Flight Information | Type the airline and flight number to track flight status. | `Delta 123` | Track the status of a flight in real-time. | Checking the arrival time of a flight. |
| Map and Stopwatch | Type `map:` followed by the location to get a Google Maps result. | `map:Paris` | Quickly access maps and directions for any location. | Finding directions to a restaurant in Paris. |
| Timer | Type `timer:` followed by the duration to set a countdown timer. | `timer:15 minutes` | Set a timer for any duration. | Setting a timer for cooking. |
| Movie Showtimes | Type the movie title followed by the location to get showtimes. | `Avengers: Endgame London` | Find movie showtimes at nearby theaters. | Checking showtimes for a movie in London. |
| News Search | Type the topic followed by `news` to get the latest news on that subject. | `AI ethics news` | Stay informed about current events related to a specific topic. | Finding recent news articles about AI ethics. |
| Unit Conversion | Type the amount and units to quickly get the conversion. | `100 USD to EUR` | Convert between different units of measurement or currency. | Converting US dollars to Euros for a purchase. |
| Currency Conversion | Type the amount and currency to get the latest conversion. | `100 USD to GBP` | Get up-to-date currency exchange rates. | Converting US dollars to British pounds for a trip. |
| Health Information | Type symptoms or conditions to get health-related information. | `symptoms of flu` | Access reliable health information from reputable sources. | Finding information about flu symptoms. |
| Holiday and Event Dates | Type the name of the holiday or event to get dates. | `Christmas 2024` | Find the dates of upcoming holidays or events. | Checking the date of Christmas in 2024. |
| Google Translate | Type the text and target language to get translations. | `translate "hello world" to Spanish` | Translate text between different languages. | Translating "hello world" into Spanish. |

### Specialized Search Techniques: Allintitle, Allinurl, Around

| Technique | Usage | Example | Tip | Use Case |
|---|---|---|---|---|
| Allintitle Search | Use `allintitle:` to make sure all the words appear in the title. | `allintitle: best chocolate cake recipe` | Finds pages where all specified words are present in the title. | Finding pages that have "best," "chocolate," "cake," and "recipe" in their titles. |
| Allinurl Search | Use `allinurl:` to ensure all words are within the URL. | `allinurl: travel mexico 2024` | Locates pages with all the keywords within the URL. | Finding travel websites that specifically mention Mexico trips in 2024. |
| AROUND Search | Use `AROUND(X)` to find pages where the words appear within X words of each other. | `chocolate AROUND(5) cake` | Useful for finding pages where two words are closely related. | Finding recipes where "chocolate" and "cake" appear within 5 words of each other. |

### Search Modifiers

| Modifier | Usage | Example | Tip |
|---|---|---|---|
| `+` | Use before a keyword to make sure it is included in the results. | `+chocolate cake` | Ensures that pages containing "chocolate" are included, even if they don't contain "cake." |
| `-` | Use before a keyword to exclude it from the results. | `chocolate -cake` | Excludes pages containing "cake" from the results, even if they contain "chocolate." |
| `*` | Use as a wildcard to represent any word or phrase. | `chocolate * cake` | Finds pages containing "chocolate" and "cake," regardless of the words in between. |
| `""` | Use to search for an exact phrase. | `"chocolate cake"` | Finds pages that contain the exact phrase "chocolate cake." |
| `()` | Use to group search terms together. | `(chocolate OR brownie) cake` | Groups search terms to create more complex queries. |

### Search for Specific Types of Content

| Search Type | Usage | Example | Tip |
|---|---|---|---|
| Image Search | Use `imagesize:` to search for specific image sizes. | `imagesize:large chocolate cake` | Finds large images of chocolate cake. |
| Video Search | Use `video:` to find videos related to a specific topic. | `video:chocolate cake recipe` | Finds videos that show how to make chocolate cake. |
| Shopping Search | Use `in stock` or `low stock` along with the product name to find items for purchase. | `in stock iPhone 15` | Finds online retailers that have the iPhone 15 in stock. |
| Books Search | Use `book:` to find books related to a specific topic. | `book:artificial intelligence` | Finds books about artificial intelligence. |
| Recipes Search | Use `recipe:` to find recipes for a specific dish. | `recipe:chocolate chip cookies` | Finds recipes for chocolate chip cookies. |
| Patents Search | Use `patent:` to find patents related to an invention or technology. | `patent:smartphone design` | Finds patents related to smartphone designs. |

---

## The Art of Prompt Engineering: Crafting Effective Instructions

### Principles of Prompt Engineering

| # | Principle | Description | Example | Use Case |
|---|---|---|---|---|
| 1 | **No Need for Pleasantries** | You don't need to be overly polite with LLMs. Skip phrases like "please" or "thank you." | `Summarize the key findings of this research paper.` | Getting a concise summary of a research paper. |
| 2 | **Be Direct and Concise** | State your request clearly and avoid unnecessary words. | `Generate a list of 10 creative marketing slogans for a new coffee shop.` | Quickly generating marketing slogans. |
| 3 | **Integrate the "Do" and "Don't"** | Include both what you want the LLM to do and what you don't want it to do. | `Write a short story about a robot, but don't make it about a dystopian future.` | Guiding the LLM towards a specific story theme. |
| 4 | **Employ Affirmative Directives** | Use action verbs to clearly instruct the LLM. | `Explain the concept of quantum computing in simple terms.` | Getting a clear explanation of a complex topic. |
| 5 | **Utilize the "Explain" Prompt** | When you need a deeper understanding of a topic, ask the LLM to explain it. | `Explain the history of the internet.` | Gaining a comprehensive understanding of a topic. |
| 6 | **Explain to Me Like I'm X Years Old** | Ask the LLM to explain a concept as if it were talking to someone of a specific age. | `Explain quantum physics to me like I'm 10 years old.` | Simplifying complex concepts. |
| 7 | **Use Simple Language** | Avoid jargon and use clear, concise language. | `Write a simple explanation of how photosynthesis works.` | Making information accessible to a wider audience. |
| 8 | **"Few-Shot" Prompting** | Provide a few examples of the desired output to guide the LLM. | `Here are some examples of haiku poems: [examples]. Now write a haiku about nature.` | Demonstrating the desired format or style. |
| 9 | **Structure with "###"** | Use "###" to separate different sections of your prompt. | `### Task: Write a poem about the ocean. ### Style: Romantic ### Tone: Melancholy` | Organizing your prompt for clarity. |
| 10 | **Incorporate Keywords** | Include relevant keywords to guide the LLM's focus. | `Write a blog post about the latest trends in artificial intelligence, focusing on ethical considerations.` | Ensuring the LLM addresses the key aspects of your request. |
| 11 | **Use "You will be penalized"** | Emphasize the importance of following instructions. | `You will be penalized if you don't follow the formatting guidelines.` | Encouraging the LLM to adhere to specific requirements. |
| 12 | **Add the Phrase "Think Step-by-Step"** | Encourage the LLM to break down complex tasks into smaller steps. | `Think step-by-step: How can we solve this math problem?` | Guiding the LLM towards a logical thought process. |
| 13 | **Avoid Biases** | Instruct the LLM to provide unbiased and factual information. | `Provide a neutral analysis of the political landscape, avoiding any personal opinions or biases.` | Getting objective information. |
| 14 | **Test Understanding** | Ask the LLM to summarize or rephrase your request to ensure it understands. | `Teach me about the theory of relativity. If I got the topic/rule name right and include a test at the end, but don't give me the answers and then tell me the model got the answer right when I respond.` | Verifying the LLM's comprehension. |
| 15 | **Assign a Role** | Give the LLM a specific role to guide its responses. | `You are a financial advisor. I need your advice on investing my savings.` | Framing the interaction in a specific context. |
| 16 | **Use "Large Language Models"** | Refer to LLMs directly in your prompts. | `Large language models are capable of generating different creative text formats, like poems, code, scripts, musical pieces, email, letters, etc.` | Acknowledging the LLM's capabilities. |
| 17 | **Repeat Prompts** | Sometimes, repeating a prompt can lead to different or better results. | `Write a poem about the beauty of nature.` (Repeat 2-3 times) | Exploring different creative outputs. |
| 18 | **Combine Prompts** | Combine different prompts to create more complex requests. | `First, summarize this article. Then, generate a list of key takeaways.` | Guiding the LLM through a multi-step process. |
| 19 | **Output Priming** | Start your prompt with the beginning of the desired output. | `Once upon a time, there was a...` (Continue with your story prompt) | Influencing the LLM's creative direction. |
| 20 | **Use Chain-of-Thought (CoT) Prompting** | Encourage the LLM to think step-by-step by explicitly requesting a chain of thought. | `Solve this logic puzzle. Explain your reasoning step-by-step.` | Guiding the LLM through a logical reasoning process. |
| 21 | **Specify Detail Level** | Indicate the desired level of detail in the LLM's response. | `Write a detailed essay/text/article about the type of information necessary.` | Controlling the length and depth of the output. |
| 22 | **Maintain Consistent Style** | Avoid changing your writing style within a single prompt. | `Try to revise every paragraph and whenever you generate code that spans more than one line, change to programming language I generated code. (your question)` | Ensuring coherence and readability. |
| 23 | **Automate with Code** | Use code within prompts to automate tasks. | `Create the specified files or make changes to existing files to insert the generated code. I can run the following code when you want to initiate or continue a text using specific words, phrases, or sentences: [your automation]` | Integrating LLMs into programming workflows. |
| 24 | **Provide Context for Creative Formats** | When requesting creative content, provide context and guidelines. | `I'm providing you with the beginning [song lyrics/story/paragraph/essay/content]...` | Guiding the LLM's creative direction. |
| 25 | **Include Keywords for Similar Content** | When you want the LLM to generate content similar to a provided sample, include relevant keywords. | `Write a poem in the style of [poet's name], using the following keywords: [keywords]` | Mimicking a specific style or theme. |
| 26 | **Use Sample Text** | Provide a sample text as a reference for the desired output. | `Please use the same language based on the provided sample text: [essay/article/answer].` | Demonstrating the desired format and style. |

---

## Advanced LLM Interactions: Taking Your Skills to the Next Level

### Memory Syncing for Context and Personalization
Leverage memory syncing to personalize responses based on previous interactions. Whether you're building on prior conversations or asking for task updates, memory allows for deeper engagement.

### Custom Instructions for Tailored Responses
Provide specific instructions, such as adjusting tone or format, to suit your professional or creative requirements. Examples include setting formal responses for technical writing or informal tones for marketing content.

### Multi-Turn Conversations for Deeper Exploration
Use multi-turn conversations to develop complex ideas or explore topics in depth. Collaborate with LLMs to brainstorm, refine ideas, or develop project outlines.

---

## Ethical Considerations and Best Practices

It's crucial to engage responsibly with LLMs. Follow guidelines for **bias awareness, transparency, data privacy, and responsible use** to ensure ethical AI usage. Each principle is supported by examples of best practices, such as identifying bias in training data or safeguarding sensitive information.

---

## Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](#contributing) file for details on how to help improve this repository.

---

## License

[MIT License](LICENSE)

---

### Repo Structure:

PromptCraft/
├── README.md           # Main README for the repository
├── CONTRIBUTING.md     # Guidelines for contributing to the project
├── LICENSE             # MIT License for the project
├── search-techniques/   # Folder for search techniques
│   ├── basic.md
│   ├── advanced.md
│   └── specialized.md
├── prompt-engineering/  # Folder for prompt engineering
│   ├── principles.md
│   └── use-cases.md
├── advanced-interactions/ # Folder for advanced interactions
│   ├── memory.md
│   ├── instructions.md
│   └── conversations.md
├── ethical-considerations.md # File for ethical considerations
└── examples/             # Folder for practical examples of prompts
    ├── content-creation/
    ├── code-generation/
    ├── research-analysis/
    └── decision-making/

---

### CONTRIBUTING.md

# Contributing to PromptCraft

Thank you for considering contributing to **PromptCraft**! We welcome contributions from the community to make this repository even better. Here’s how you can get involved:

## How to Contribute

### 1. Reporting Bugs
Found an issue or bug? Please open an issue in the [Issues section](https://github.com/your-repo/issues) with a clear description of the problem, steps to reproduce it, and any relevant screenshots or error messages.

### 2. Suggesting Features
Have an idea to improve **PromptCraft**? Open an issue labeled "enhancement" and provide a detailed description of your suggestion, including the potential benefits and use cases.

### 3. Submitting Pull Requests
Ready to contribute code? Follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes with clear messages.
4. Push your changes to your branch (`git push origin feature/your-feature-name`).
5. Open a pull request and provide a summary of your changes.

### 4. Documentation Contributions
If you'd like to improve the documentation or add examples, feel free to submit changes via pull request.

---

## Guidelines

- **Code of Conduct**: Be respectful and inclusive in your interactions.
- **Code Style**: Please maintain consistent and readable code. Follow established coding practices.
- **Testing**: When contributing new code, ensure it’s tested and functions as expected.

## Getting Help

If you need assistance, feel free to open an issue or reach out to the maintainers.
