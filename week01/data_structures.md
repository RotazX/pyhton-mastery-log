
list vs tuple
A list can be changed after creation, but a tuple cannot.

A list has brackets but a tuple has parenthesis, and it also always needs a comma to be a tuple.

list - [1, 2, 3]  
tuple - (1, 2, 3)

A hash is an integer computed from a value.
Immutable things are hashable, mutable things aren't. Strings, numbers, tuples, None - all hashable. Lists, dicts, sets - not hashable.

Dict keys must be hashable.

A dict finds keys by hashing them, so a key's hash has to stay constant for its lifetime. Lists are mutable, so their contents - and any hash deried form them - can change after insertion, which would make the stored value permanently unreachable. Python blocks it rather than let you corrupt the dict. Use a tuple if you need a multi-part key.

Explain out loud: why did you choose a dict instead of a list of tuples for the contact book, and what would break if you had duplicate names?
Dict, because lookup, delete, and the duplicate check are all O(1) single expressions instead of scans, and because it serializes to JSON cleanly. The cost is that the dict enforces one number per name, so a duplicate silently overwrites the previous entry with no error. 
