# PROJECT 7 – TEXT COMPRESSION USING CHARACTER RUNS

## About the Project
The Text Compression Using Character Runs project is designed to reduce the length of a text by identifying consecutive repeated characters. It uses Run-Length Encoding (RLE) to replace repeated characters with the character followed by its count. This helps reduce text size when the input contains repeated characters.

## Technologies Used
- **Python** – Used to develop the text compression program.
- **Strings** – Used to accept and process text.
- **Loops** – Used to identify consecutive repeated characters.
- **Conditional Statements** – Used to compare adjacent characters.
- **String Concatenation** – Used to create the compressed text.

## Main Features
- Accepts text from the user.
- Identifies consecutive repeated characters.
- Counts the number of repeated characters.
- Compresses text using Run-Length Encoding.
- Displays the original text.
- Displays the compressed text.
- Shows the original and compressed text lengths.

## Algorithm
1. Start the program.
2. Accept a string from the user.
3. Initialize an empty string for compressed text.
4. Set a counter to count repeated characters.
5. Traverse the input string character by character.
6. Compare the current character with the next character.
7. If both characters are the same, increase the counter.
8. Otherwise, add the character and its count to the compressed string.
9. Reset the counter and continue.
10. Display the original and compressed text.
11. Stop the program.

## Sample Output
```text
Enter a string: aaabbbccdddd

----- TEXT COMPRESSION REPORT -----

Original Text: aaabbbccdddd
Compressed Text: a3b3c2d4

Original Length: 12
Compressed Length: 8

Text Compression Successful!
```

## Conclusion
This project helps reduce text length by identifying and encoding consecutive repeated characters using Run-Length Encoding (RLE). It demonstrates Python concepts such as strings, loops, conditional statements, counters, and string concatenation.
