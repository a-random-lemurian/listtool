# listtool

This is a customizable name generator that accepts JSON input.

## Example

```json
{ "word": [
        [
            "I use",
            "Just gotta tell people I use"
        ],
        [
            "Arch btw"
        ]
    ]
}
```

Feeding this input to the program with the `-p` flag will print:
```
I use Arch btw
Just gotta tell people I use Arch btw
```

## What's `--endless-sky-phrase`?

It's a program command-line option that will output plugin code for a game
known as [Endless Sky](https://github.com/endless-sky/endless-sky).
