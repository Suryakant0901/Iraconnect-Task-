s = input("Enter a string: ")

text = ""

for ch in s:
    if ch.isalnum():
        text += ch.lower()

left = 0
right = len(text) - 1

while left < right:
    if text[left] != text[right]:
        print(False)
        break

    left += 1
    right -= 1
else:
    print(True)