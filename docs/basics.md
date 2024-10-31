Building software is not too much different than constructing a chair or a table, renovating a room or building a
new house. You typically start with some kind of plan, which may be written down (or not), you'll use different
materials and ways of putting them together to create the thing you have designed.  

When building something physical, you'll use physial things obviously, nails, screws, wood, metal, bricks, stone, wires
and plastic. Each has a unique function and different properties that fit it for different contexts and exclude it in
others. You'd choose wood or iron rebar to provide a rigid frame and support weight instead of plastic, but if you want
something flexible plastic or thin metal would be a better choice. You are constantly making choices, based on
experience, on what materials and tools to use to achieve the results you want. This perfectly describes building
software, you make choices amongst many tools and materials to build the product you want to build.  It just so happens
that all of these materials have no physical existence, they are concepts, but put together with experience and wisdom,
they empower new tools, new interactions, and new worlds.

## Python

Python is a language used to build computer software. Using our building analogy, it is akin to an architectural school
of thought, similar to the functional or Bauhaus style, Wright's organic architecture or the art nouveau/Glasgow style.
Python provides several common features observable in other languages and some unique features that make it distinct.


## Types

Extending the building analogy lets start with the basics, similar to the nails, screws, nuts, bolts and other
fasteners, Python provides several different basic data types

- `int`: a positive or negative natural number, ... -2, -1, 0, 1, 2, ...
- `float`: a floating point number, 3.14159 or 2.718, calculations may be limited due to the core
- `str`: a string; an immutable sequence of character values
- `bool`: a boolean which can be `True` or `False`
- `None`: a representation of `null` - the absence of a value
- `complex`: a complex number with real and imaginary parts; 3+4j  - used for very specialized applications (IYKYK)

Python is a strongly typed dynamic language, which means that when you create a variable and give it a value like:

```python
  radius = 3
  pi = 3.1415926              # for starters
  greeting = "Hello World!" 
```
you don't need to explicitly specify the type as `int` or `float` or `str`, the variable is *dynamically* typed, the 
type of the value assigned to the variable is retained by Python as the type of that variable.   The type of a variable
determines what you can (and cannot) do with that variable.

```python
  area = pi * radius**2        # ** is the exponentiation operator 
  pi_greeting = pi*greeting    # ERROR!  NOT ALLOWED
```





- Basic syntax, operations and control flow looping
  - Operations:  `+`, `-`, `*`, `/`, `//`, `%`, `**`
  - remember precedence, use `()` to disambiguate
  - Variables: names/labels for values
  - a variable knows its type: **all variables are objects**
  - a variable can be dynamically changed to point to or label a new type
