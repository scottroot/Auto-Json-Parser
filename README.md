# Auto JSON Parser

This is just a single Python script that allows you to convert text strings of malformed JSON into working JSON objects or formatted and cleaned JSON strings.

## What it does

The script relies on the presence of a comma between each entry, and at this time does not acknowledge nested dicts, but may add that in later if my current use case requires it.  The script splits the string by commas, uses ast.literal_eval to interpret the snippet as a dict and then cleans both sides.

## Usage
```python
> bad_json = """{'content':"\"Tweet: #\", 'description': "Article from poster "@user" on Twitter"}
> cleaned_json = auto_json_parser(bad_json, output="json")
> print(cleaned_json)
# {"content": "Tweet: #", "description": "Article from pposter @user on Twitter"}
```
