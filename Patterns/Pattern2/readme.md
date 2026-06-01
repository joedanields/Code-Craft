# Pattern 2: Right Triangle of Stars

This folder contains C and Python implementations that print a right-angled triangle of `*` characters with $N$ rows.

## Output Example (N = 5)

```
* 
* * 
* * * 
* * * * 
* * * * * 
```

Note: The Python version prints an extra blank line after each row for spacing.

## Files

- `pattern2.c`: C implementation
- `pattern2.py`: Python implementation

## How It Works

Both programs use two nested loops:

- The outer loop controls rows.
- The inner loop prints `i + 1` stars followed by a space.

## Run the C Program

```
gcc pattern2.c -o pattern2
./pattern2
```

## Run the Python Program

```
python pattern2.py
```
