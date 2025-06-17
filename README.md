#📌 LinkedIn https://www.linkedin.com/in/bhavya-m-945767226/

# 🔠 Braille Auto-Correct and Suggestion System

## 📌 Overview

This project implements an intelligent Braille auto-correct and suggestion system for visually impaired users typing Braille using a standard QWERTY keyboard. It takes Braille character inputs (as QWERTY key combinations) and suggests the most likely intended word based on a predefined Braille dictionary.

---

## 🛠️ Features

- Accepts QWERTY-based Braille input (keys: D, W, Q, K, O, P).
- Suggests top 3 closest words using Levenshtein distance.
- Handles typos, missing or extra dots, and character-level errors.
- Real-time response with modular design for scaling.
- Easily extendable for learning, multi-language, and contractions.

---

## 🔤 QWERTY to Braille Mapping

| Key | Braille Dot |
|-----|--------------|
| D   | 1            |
| W   | 2            |
| Q   | 3            |
| K   | 4            |
| O   | 5            |
| P   | 6            |

A Braille character is formed by pressing one or more of the above keys simultaneously.

---

## 🚀 How It Works

1. User inputs a list of Braille characters as QWERTY key combinations.
2. The system converts these to Braille dot sets.
3. Each input word is compared to a Braille-encoded dictionary using Levenshtein distance.
4. Top 3 most similar words are returned as suggestions.

---

## 🧪 Sample Test Case

**Input**:  
```python
[['D', 'K'], ['D'], ['D', 'P']]
