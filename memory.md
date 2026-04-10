# Memory

## Modulo, Cycling, and Ranges

### 1. The Mental Model: Modulo is a Clock
Stop thinking about modulo (`%`) as just "division remainders." Think of it as a **circle or a clock**. It forces any number to stay within the boundaries of a specific range (like an array's length).

Example for an array of length 3 `[A, B, C]`:
* `0 % 3 = 0` (Stays at A)
* `1 % 3 = 1` (Stays at B)
* `2 % 3 = 2` (Stays at C)
* `3 % 3 = 0` (Wraps back to A)

### 2. The Negative Modulo Trap
Confusion happens when you try to move backward (e.g., `-1 % 3`). 
* **Python:** Returns `2` (It is mathematically pure and knows you want to wrap around).
* **Java, C++, C#, JS:** Returns `-1` (They calculate the *remainder*. Using `-1` as an array index will crash your program).

### 3. The "Bulletproof" Cycling Formula
To ensure your logic works in *every* language and never throws an "Index Out of Bounds" error when moving backward, use this exact formula:

`safe_index = (((current_index + steps) % length) + length) % length`

**Why it works for extreme negatives (e.g., starting at 0, taking -389 steps, length 3):**
1. `-389 % 3` yields `-2` (in Java/JS).
2. `-2 + 3` (add the length) yields `1`. This rescues the number from negative territory.
3. `1 % 3` yields `1`. You safely land on index 1.

---

### 4. Ranges & The Fencepost Error (Off-By-One)
When working with dates or number ranges, bugs happen because developers confuse **inclusive** (counting items) with **exclusive** (counting distance).

**The Fencepost Rule:**
* **Counting Gaps (Distance):** `End - Start`. 
  * *Use case:* How much time has passed. (e.g., Rotating shifts, measuring age).
* **Counting Posts (Inclusive):** `(End - Start) + 1`. 
  * *Use case:* Total number of objects or days. (e.g., "How many days was I physically in the office from the 1st to the 5th? Answer: 5 days").

### 5. Real-World Scenario: Rotating Shifts
* **Array of Shifts:** `["A", "B", "C"]` (Length = 3)
* **Reference Date:** `2026-01-01` is at Index `0` (Shift A).

**Goal: Find the shift for any date in the future or past.**
1. Find the **gaps** (days passed) between the Target Date and Reference Date. 
   * *Future Example (Jan 5th):* `5 - 1 = 4` days passed.
   * *Past Example (Dec 30th):* `-2` days passed.
2. Plug that distance into the Bulletproof Formula:
   * **Going Forward (4 days):** `((0 + 4) % 3 + 3) % 3 = 1` (Shift B)
   * **Going Backward (-2 days):** `((0 + -2) % 3 + 3) % 3 = 1` (Shift B)


```py
from datetime import datetime

def get_shift(
    target_datetime: datetime, 
    shift_length_hours: int, 
    current_index: int = 0, 
    reference_datetime: datetime = datetime(2026, 1, 1, 8, 0), 
    shifts: tuple = ("A", "B", "C")
    ) -> str:

    # 1. Find exact time difference
    time_diff = target_datetime - reference_datetime
    
    # 2. Convert to total exact hours
    hours_passed = time_diff.total_seconds() / 3600

    # 3. Calculate full shifts passed
    shifts_passed = int(hours_passed // shift_length_hours)

    # 4. Modulo to cycle the array safely
    safe_index = (current_index + shifts_passed) % len(shifts)
    
    return shifts[safe_index]
```