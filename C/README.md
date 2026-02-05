
## How the `C/` Folder is Organized

The `C` folder follows standard C project practices for modularity and portability. Here’s a guide to the main components:

### File Types

- **`.h` files (headers)**:  
  - Declare public structs, types, and function prototypes (function signatures, without bodies).
  - Example: `library.h` declares functions you can call from other files.

- **`.c` files (sources/implementation)**:  
  - Contain the actual code for the functions declared in headers (function definitions).
  - Example: `library.c` implements the functions declared in `library.h`.
  - Multiple `.c` files can exist; each can include any needed headers.

- **`main.c`**:  
  - The entry point of the program, typically containing the `main()` function.
  - Includes headers (such as `library.h`) to use functions defined elsewhere.

- **`CMakeLists.txt`**:  
  - Build script for CMake that configures project compilation (specifies sources, headers, executables, and build options).

### Using the Library

- To use the linked list (or any library code), a `.c` file just needs:  
  `#include "library.h"`  
  The compiler uses the prototypes in the header to type-check.  
  The actual function definitions are linked in from `library.c` during build/linking.

- **Typical workflow:**  
  1. Declare APIs/types in `.h`  
  2. Implement in `.c`  
  3. `#include` the `.h` in any `.c` file needing the APIs/types

- It is conventional—but not strictly required—that implementation and header share a base name (e.g. `library.h` / `library.c`).

### Additional File Types (may or may not be present)

- `*.a` : Static library (archive) file
- `*.so` : Shared library (Linux, UNIX)
- `*.dylib` : Shared library (macOS)
- `*.dll` : Dynamic link library (Windows)
- `*.lib` : Static library (Windows)
- `*.obj` : Compiled object file

This layout helps separate API from implementation, supports code reuse, and makes builds portable.


