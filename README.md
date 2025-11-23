


## 🚀 Typing Speed Test

A simple command-line Python application to measure a user's typing speed in **Words Per Minute (WPM)** and the time taken.

### 📋 Prerequisites

To run this script, you only need to have **Python 3** installed on your system.

### 📝 How to Run

1.  **Save the code:** Save the provided Python code into a file named **`typing_test.py`**.

2.  **Open your terminal/command prompt.**

3.  **Run the script** using the Python interpreter:

    ```bash
    python typing_test.py
    ```

### 💡 How It Works

1.  **Setup:** The script first imports the built-in **`time`** module for accurate timing.
2.  **Display:** It displays the target sentence to the user.
3.  **Start Timing:** When the user presses `ENTER` to begin typing, the **`time.time()`** function records the **`start`** timestamp.
4.  **User Input:** The program waits for the user to type and press `ENTER` again.
5.  **Stop Timing:** The **`end`** timestamp is recorded immediately upon receiving the input.
6.  **Calculation:**
      * **Time Taken:** Calculated as `end - start`.
      * **Words Typed:** Calculated by splitting the user's typed string and counting the elements (`len(typed.split())`).
      * **WPM (Words Per Minute):** Calculated using the formula:
        $$WPM = \frac{\text{Words Typed}}{\text{Time Taken in Seconds} / 60}$$
7.  **Results:** The final time, word count, and WPM are printed, rounded to two decimal places.

### 📦 Code Snippet

```python
import time

print("Typing Speed Test\n")

sentence = "the quick brown fox jumps over the lazy dog ."
print("Type this sentence:\n")
print(sentence)

input("\nPress ENTER when you are ready...\n")

start = time.time()
typed = input("Start typing:\n")
end = time.time()

time_taken = end - start

# Count words
typed_words = len(typed.split())
wpm = typed_words / (time_taken / 60)

print("\nResults:")
print("Time taken:", round(time_taken, 2), "seconds")
print("Words typed:", typed_words)
print("WPM:", round(wpm, 2))
```

-----
