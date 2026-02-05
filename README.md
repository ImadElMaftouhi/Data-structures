# Data Structures

Implementations of common data structures in multiple languages. Each language folder contains library-style code that can be used together.

## Languages & Contents

| Language   | Data structures |
|-----------|------------------|
| **C**     | Singly linked list (SLL), Doubly linked list (DLL) |
| **Python**| SLL, DLL, Circular linked list (CLL), Binary tree, Queue, Stack |
| **JavaScript** | Linked list, Double linked list, Queue, Stack |
| **C++**   | *(placeholder)* |

## Build & run

**C** (CMake):

```bash
cd C
mkdir build && cd build
cmake ..
make
./Data_structures
```

**Python**: Import modules from the `Python` folder (e.g. `import Sll`, `import Dll`, `import Queue`). Run `main.py` for examples.

**JavaScript**: Use the `.js` files as modules or run with Node (e.g. `node Stack.js` if runnable).

## Layout

- `C/` — `library.h`, `library.c`, `main.c`; build with CMake.
- `Python/` — `Sll.py`, `Dll.py`, `Cll.py`, `BinTree.py`, `Queue.py`, `Stack.py`, `main.py`.
- `JavaScript/` — `Linked-list.js`, `Double-linked-list.js`, `Queue.js`, `Stack.js`.
- `C++/` — Reserved for future C++ implementations.
