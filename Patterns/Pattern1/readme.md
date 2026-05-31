# Pattern 1: Square of Stars

This folder contains C and Python implementations that print an $N \times N$ square of `*` characters.

## Output Example (N = 5)

```
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
```

## Files

- `4x4.c`: C implementation
- `4x4.py`: Python implementation

## How It Works

Both programs use two nested loops:

- The outer loop controls rows.
- The inner loop prints `N` stars followed by a space in each row.

## Run the C Program

```
gcc 4x4.c -o pattern1
./pattern1
```

## Run the Python Program

```
python 4x4.py
```
