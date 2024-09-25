# Morse
## Morse Code Converter

## This script converts the input in the string (encode_morse) at line 66 into Morse code and outputs it with a delay to simulate the real transmission of messages in Morse code.
Each letter of the alphabet and digits are represented by a combination of dots (`·`) and dashes (`−`).

## Features
I took the Morse alphabet with the respective designations and translated everything into Morse symbols from lines 16 to 51. If you find any discrepancies, please let me know! :)

## Morse Code Mapping
- **Dots (`·`)**: Short signal.
- **Dashes (`−`)**: Long signal.
- **Symbol space**: A short pause between elements of a character.
- **Letter space**: A longer pause between letters.
- **Word space**: A long pause to separate words.

## Example Usage

On line 66, input your message in quotes and run the code, and you will see the code update each time you give it a new task to translate:
`encode_morse("Right Here")`