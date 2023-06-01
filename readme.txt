
Problem description:

Given a JSON file such as: 
    { "foo": ["bar", "baz"], "orange": ["banana", "mango"], "bar": ["qux", "quux"], "monkey": ["cow", "parrot"], "banana": ["mango", "monkey"], "baz": ["baz"], "quux": ["bar", "banana"], "cow": ["orange"], ... } 
Write a Python program using only the standard libraries that finds all the cycles in such a file: 
In the example above we can have the cycle: "bar" -> "quux" -> "bar"  
Make sure that:  
- Every cycle is represented only once, e.g. 
`"bar" -> "quux" -> "bar"` is the same cycle as `"quux" -> "bar" -> "quux"`. 
- Only minimal cycles should be shown, e.g. in `"foo" -> "bar" -> "quux" -> "bar"`,
the `"foo"​ ->` should not be part of the cycle.  

Use of packages from pypi for development time dependencies, e.g. auto-formatting,
testing, mocking etc, is allowed. 
