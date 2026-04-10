### Initial Query
explain different machine learning model performance metrics with real world examples and how to remember them accurately; recall, precision, accuracy, etc.

### ML Performance Metrics Cheatsheet

#### The Foundation: Confusion Matrix
* **TP (True Positive):** Predicted Yes, Actual Yes.
* **TN (True Negative):** Predicted No, Actual No.
* **FP (False Positive):** Predicted Yes, Actual No. *(Type I Error - False Alarm)*
* **FN (False Negative):** Predicted No, Actual Yes. *(Type II Error - Miss)*

#### Core Metrics & Mnemonic Devices
* **Accuracy:** Overall correctness. `(TP + TN) / Total`
    * *Caveat:* Useless for highly imbalanced datasets.
* **Precision:** Focuses on the quality of positive predictions. `TP / (TP + FP)`
    * *Mnemonic:* **P**recision = **P**redictions. (How many *predicted* positives were right?)
    * *Goal:* Minimize False Positives (Don't waste resources).
* **Recall (Sensitivity):** Focuses on catching all actual positives. `TP / (TP + FN)`
    * *Mnemonic:* **R**ecall = **R**eality. (How many *actual reality* positives did we catch?)
    * *Goal:* Minimize False Negatives (Don't miss the critical events).
* **F1-Score:** Harmonic mean. `2 * (Precision * Recall) / (Precision + Recall)`
    * *Use Case:* When you need a balanced metric and uneven class distribution exists.

#### ⚠️ Gotchas to Remember
> "High accuracy is a lie if the dataset is heavily skewed."
1.  **Accuracy Paradox:** A 99% accurate model might just be predicting the majority class 100% of the time. 
2.  **The Trade-off:** Increasing Precision usually decreases Recall, and vice versa. You must choose based on the *business cost* of False Positives vs. False Negatives.


<br/><br/>


### Initial Query
how is precision different from recall; explain; and provide notes

### ML Metrics Cheatsheet: Precision vs. Recall

#### Core Definitions
* **<mark style="background-color: #e6f7ff; padding: 2px;">Precision</mark>**
    * *Concept:* The **quality** of your positive predictions. Out of everything flagged as positive, how many were actually true?
    * *Formula:* `TP / (TP + FP)`
    * *Goal:* Minimize <span style="color: #d9534f;">**False Positives**</span> (False Alarms).
* **<mark style="background-color: #fff0f6; padding: 2px;">Recall</mark>**
    * *Concept:* The **quantity** of actual positives found. Out of all real positive events, how many did you catch?
    * *Formula:* `TP / (TP + FN)`
    * *Goal:* Minimize <span style="color: #d9534f;">**False Negatives**</span> (Missed Detections).

#### The Trade-Off & Caveats
> *You rarely maximize both. They exist on a seesaw controlled by the model's prediction threshold.*
* **High Precision / Low Recall:** Strict model. <span style="color: #5cb85c;">Trust the alarms</span>, but <span style="color: #d9534f;">expect to miss events</span>.
* **High Recall / Low Precision:** Loose model. <span style="color: #5cb85c;">Catches everything</span>, but <span style="color: #d9534f;">generates massive noise</span>.
* **Accuracy Paradox:** Never rely on simple Accuracy for heavily imbalanced datasets (e.g., fraud, rare diseases).

#### Heuristics: When to use which?
1.  **Optimize Precision when:** The cost of a False Positive is high. *(Example: Spam filters. Missing an important email is worse than letting one spam message through).*
2.  **Optimize Recall when:** The cost of a False Negative is high. *(Example: Cancer screening. Missing a tumor is catastrophic; false alarms are an acceptable cost).*
3.  **Balance Both:** Use the **F1-Score** `2 * (Precision * Recall) / (Precision + Recall)` when you need a balanced metric for uneven class distribution.


<br/><br/>

