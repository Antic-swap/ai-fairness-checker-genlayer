# AI Fairness Checker (GenLayer)

## Overview

AI Fairness Checker is an intelligent smart contract built on GenLayer that evaluates the fairness of user-submitted content using AI.

It demonstrates how LLMs and blockchain can enable subjective decision-making directly on-chain.

---

## Problem

Traditional smart contracts are:

* Deterministic
* Unable to handle subjective logic
* Dependent on external human judgment

---

## Solution

This project introduces:

* AI-powered fairness evaluation
* Natural language input processing
* On-chain storage of AI decisions

---

## How It Works

1. User submits content (text)
2. Contract sends it to AI (LLM)
3. AI analyzes fairness
4. Returns:

   * Verdict (text)
   * Fair/Unfair (boolean)
5. Result stored on-chain

---

## AI Integration

* Uses `nondet.exec_prompt()` for LLM execution
* Uses `eq_principle` for validator agreement
* Enables subjective consensus

---

## Contract Functions

### check_fairness(content)

Submit text for evaluation

### get_result()

Returns formatted verdict

### get_full_status()

Returns full contract state

---

## Tech Stack

* GenLayer Python SDK
* LLM via nondeterministic execution
* Smart contract logic

---

## Key Features

* AI-based decision making
* On-chain fairness validation
* Simple and extensible design
* Demonstrates subjective consensus

---

## Limitations

* Basic response parsing
* Single input at a time
* No advanced moderation categories

---

## Future Improvements

* Multi-category moderation (spam, fraud, abuse)
* Better JSON parsing
* Batch processing
* Integration with dApps

---

## Use Cases

* Content moderation
* Spam detection
* DAO governance filtering
* Dispute pre-check systems

---

## Demo Flow

1. Deploy contract
2. Call check_fairness()
3. View result using get_result()

---

## Conclusion

This project shows how AI and blockchain can enable intelligent contracts capable of handling real-world subjective decisions without centralized control.
