# Pattern 3: Right Triangle of Numbers

This folder contains C and Python implementations that print a right-angled triangle of numbers from 1 to the row index, with $N$ rows.

## Output Example (N = 5)

```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
```

## Files

- `pattern3.c`: C implementation
- `pattern3.py`: Python implementation

## How It Works

Both programs use two nested loops:

- The outer loop controls rows.
- The inner loop prints numbers from 1 to `i + 1` on each row.

## Run the C Program

```
gcc pattern3.c -o pattern3
./pattern3
```

## Run the Python Program

```
python pattern3.py
```
