
I wrote to this developer to buy a Discord joiner.

At first he seemed responsible and knowledgeable in his field. Later we agreed on the functionality.

Before paying, the seller specified that he would send the code the next day, and also that high-quality proxies were needed for it to work. I wrote the name of the proxy provider I work with (this is a really good provider, with whom I have been working for a long time and which passes cloudflare).

The author asked for proxies for testing, to make sure that they work. I sent them to him, he checked everything and said that everything was fine, I just would not be able to go to more than 100 servers. And immediately after that, he tried to sell me HIS proxies (at first I did not attach any importance to this).

Then he told me that he has his own solver, we talked a little and he went to write the code for me.

A little later he sends it, and I start testing. And it turns out that the code does not work, or rather, as he said, "does not work with my proxies" (although I gave him the same ones and he said that everything was fine). I asked him to suggest other services that were good in his opinion, and of course he does not know any services except his :)

Even then I began to feel deceived, because if after the test he said that it does not work with my proxies, I would have started to go through my proxies and check other providers, and simply would not have bought the code if it worked only through him (I do not have the opportunity to depend on the personal messages of another person, to buy traffic through correspondence, etc.).

Immediately after my complaint, he began to try to sell me his solver, first offering a version for 1200 euros, then he reduced the price by as much as 2 times. Then he began to offer to buy a version with a closed code, but for 200 euros. Later he said that I can pay him 100 euros now, and then another 100 euros tomorrow. And I realized that they are trying to cheat me out of money once again.
The only thing that confused me was that the person seemed adequate to me and had a history on GitHub. I tried to find a compromise, asked for free test traffic, or a test subscription to his captcha solver. I was refused all this, all the time blaming the proxies (although I again gave him theirs for the test) and refused to meet halfway. Then he said that my other providers were shit, and again began to offer to buy from him.

Obviously, he refused to return my money.

I do not recommend this developer for cooperation and buying his products. I DO NOT DENY that his solver works, and the proxies are better than mine. But the fact remains, he took my proxies, said that everything is fine, and after payment and a negative test, it turned out that my proxies are crap.

I understand that the author can start making excuses, cutting the correspondence and my words (or his) out of context, but believe me, the situation is exactly as I wrote. You can get the correspondence and any evidence from me, I saved everything. Be careful.
# Discord hCaptcha AI Solver

A powerful AI-based hCaptcha solver API designed specifically for Discord bot automation. This project provides a FastAPI web server running a fine-tuned Dutch language transformer model to automatically answer hCaptcha accessibility challenges in Dutch.

---
# 🔥 NEW: API-Based hCaptcha Solver!
Works like CapMonster & 2Captcha
€50/month | €200 lifetime | Source Code: €1200
Fast. Reliable. Easy.
https://t.me/dorukuz


https://github.com/user-attachments/assets/4eb3d40f-3228-4159-82c4-6fce5fbea371


## Features

- Uses a custom fine-tuned [RobBERT](https://huggingface.co/DTAI-KULeuven/robbert-2022-dutch-base) Dutch language model for high accuracy.
- Caches previous answers for ultra-fast response times.
- Simple REST API with a `/solve` endpoint accepting hCaptcha questions and returning AI-generated answers.
- Built with FastAPI for asynchronous and high-performance serving.
- Ideal for integrating into Discord bots that need to bypass hCaptcha accessibility challenges.

---

## How It Works

When the solver receives a question from the hCaptcha accessibility challenge (usually a simple Dutch "Ja" or "Nee" question), it:

1. Cleans and preprocesses the question text.
2. Checks if it already answered this question before — if yes, returns the cached answer.
3. Otherwise, it uses the transformer model pipeline to classify the answer as "Ja" (Yes) or "Nee" (No).
4. Logs the new question and answer for future caching.
5. Returns the answer in JSON format.

---

## API Usage

Send a POST request with JSON body:

```json
{
  "question": "Your hCaptcha question text here"
}
```

Response:

```json
{
  "question": "Your hCaptcha question text here",
  "answer": "Ja" // or "Nee"
}
```

---

## Integration Example in Discord Bots

In your Discord automation code, after detecting the accessibility challenge, you can send the question text to the local solver API, get the AI's answer, and fill it into the captcha input field automatically. This significantly speeds up and automates solving hCaptcha challenges during Discord account generation or bot registration.

Example workflow:

- Detect hCaptcha accessibility challenge frame.
- Extract the question text.
- POST to `http://localhost:8000/solve` with the question.
- Receive "Ja" or "Nee" answer.
- Fill the answer into the captcha input box.
- Submit and continue.

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Dorukuz/Discord-Captcha-Solver.git
cd discord-hcaptcha-ai-solver
```

2. Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
python app.py
```

The API server will start at `http://0.0.0.0:8000`.

---

## Why Choose This Solver?

- Trained specifically on Dutch accessibility questions used in hCaptcha.
- Designed to handle Discord's hCaptcha challenges efficiently.
- Lightweight and easy to deploy locally or on a server.
- Extensible for further fine-tuning or adding support for other languages.

---

## License

This repository and code are for demonstration and paid use only. Unauthorized commercial use is prohibited.

---
## Contact

For subscription plans, commercial use, or custom integration support, contact:  
[My own Telegram](https://t.me/dorukuz) 

[AXI DEV Telegram Group](https://t.me/axi1337) 

---

*This project is a cutting-edge AI assistant helping Discord automation workflows handle hCaptcha challenges with ease.*
