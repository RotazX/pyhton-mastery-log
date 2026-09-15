
Not very confident in:
    early returns and goard clauses
    args and kwargs
    dicts, tuples, and sets

Situation. I was working through a self-directed Python curriculum and needed a project that went beyond single-file exercises — something that read external data, processed it, and produced a report.

Task. Build a leaderboard: take a plain-text file of player names and scores, and output a ranked summary. The real requirement was that it survive messy input, because a file written by hand always has blank lines and typos in it.

Action. I split it into three layers. One function's only job is reading the file and returning raw lines. A second parses those lines into name-score pairs — that's where the validation lives: it checks each row has the expected number of fields and that the score actually converts to an integer, and skips rows that don't instead of crashing. A third takes the parsed data and returns it sorted by score, using sorted with a key function rather than sorting in place, so the caller's data isn't mutated behind its back. Printing happens in the main block, not inside any of those. The reason for that split is testability: only the file-reading function touches the disk, so the parsing and ranking logic can be tested by passing in a list of strings — no temporary files, no cleanup. It also means swapping the input from a text file to a CSV or a database later only changes the one function that reads.

Result. It takes a scores file and prints a ranked leaderboard with positions, handles malformed rows without dying, and the logic is covered by tests that run in milliseconds. It's the first thing I wrote where the structure was a deliberate decision rather than whatever order I happened to write the code in.