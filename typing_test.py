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


