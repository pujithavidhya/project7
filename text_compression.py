
# Text Compression Using Character Runs

text = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(text)):

    if i < len(text) - 1 and text[i] == text[i + 1]:
        count += 1

    else:
        if count > 1:
            compressed += text[i] + str(count)
        else:
            compressed += text[i]

        count = 1

print("\nOriginal String:", text)
print("Compressed String:", compressed)

if len(compressed) < len(text):
    print("Compression is beneficial.")
else:
    print("Compression is not beneficial.")
