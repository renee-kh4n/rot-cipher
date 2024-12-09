# rot-cipher
A program that performs a simple letter substitution to decode or encode a text. 

## User Input
- `**Text**:string` - text to be deciphered or encoded
- `**Rot**:int` - number of rotations
- `**Direction**:string` - selection between 'forward or backward' rotation (may be internally represented as a bool)

## Output
- Text, transformed by the specified rotation

## Scope and Limitation
- Only characters belonging to the English Alphabet are rotated
- Numbers and other special symbols are retained after the rotation
