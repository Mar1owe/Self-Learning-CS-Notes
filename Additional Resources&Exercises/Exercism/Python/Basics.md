1. Python employs both [duck typing](https://en.wikipedia.org/wiki/Duck_typing) and [gradual typing](https://en.wikipedia.org/wiki/Gradual_typing), via [type hints](https://docs.python.org/3/library/typing.html)
2. Everything in python is an object
3. Python was created by Guido van Rossum and first released in 1991.
4. Name assignments
    ```Python
    <name> = <value>
    ```
5. Constants: Names meant to be assigned only once in a program. They should be defined at a module (file) level, and are typically visible to all functions and classes in the program. Using `SCREAMING_SNAKE_CASE` signals that the name should not be re-assigned, or its value mutated.
6. Functions explicitly return a value or object via the `return` keyword. Functions that do not have an explicit `return` expression will implicitly return `None`.
7. Docstrings  
    The first statement of a function body can optionally be a docstring, which concisely summarizes the function or object's purpose. Docstring conventions are laid out in [PEP257](https://peps.python.org/pep-0257/). Docstrings are declared using triple double quotes (""") indented at the same level as the code block.