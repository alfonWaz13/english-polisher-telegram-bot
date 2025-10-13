# English Polisher Telegram Bot

This is a personal software project developed as a learning exercise. It's a simple Telegram bot that uses a Generative AI model to help users improve their English. You can send it a sentence or phrase, and the bot will respond with a more natural, native-sounding alternative if needed.

---

## 🎯 Project Goals

This project was built with a clear set of learning objectives in mind:

* **Build a Telegram Bot:** The primary goal was to create my very first Telegram bot from scratch to understand the basics of the Telegram Bot API and handle user interactions.
* **Implement Webhooks:** A core objective was to move beyond traditional polling and learn how to implement an **event-driven architecture** using webhooks, which are essential for serverless applications.
* **Learn AWS Lambda:** The project was an opportunity to dive into **serverless architecture** and deploy a live application using AWS Lambda. This included learning about event-driven functions, managing environment variables, and the pay-per-use model.
* **Master GitHub Actions:** A key objective was to implement a fully automated **CI/CD pipeline**. The project's workflow uses GitHub Actions to automatically package the code and deploy it to AWS Lambda on every change to the `main` branch.

---

## 🛠️ Key Technologies

* **Python:** The core language for the bot's logic.
* **Google Gemini API:** The Generative AI model used to evaluate and correct English text.
* **AWS Lambda:** The serverless compute service that runs the bot's code.
* **GitHub Actions:** The CI/CD tool that automates the entire deployment process.

---

## 🚀 How It Works

The bot's architecture is event-driven and serverless:

1.  A user sends a message to the bot on Telegram.
2.  Telegram sends an **HTTP webhook request** to a specific URL provided in the configuration of the Lambda function.
3.  The API Gateway acts as a trigger, which invokes the **AWS Lambda function**.
4.  The Lambda function processes the incoming message, calls the Google Gemini API to polish the English text, and sends the polished response back to the user via the Telegram API.
5.  A **GitHub Actions workflow** automates this process, ensuring that any new code is automatically deployed and live within seconds.