## Changed made to commit 6e65:

['Key1', '\n Value1 ', 'Name', '\n                                FIRSTNAME MIDDLENAME LASTNAME                            ', '', 'Key2', '\n                                Value2                            ', '', 'Key3', '\n                                DD-MM-YYYY                            ', '', 'Key4', 'DD-MM-YYYY', '', 'Key5', '\n Value5 \n', 'Key6', 'Value6 Usually empty string', '', 'Key7', '\n                                Value7                            ', '']

Need a dict of key,value pairs like so:
```
{
    'Key1': 'Value1', 
    'Key2': 'Value2',
    'Key3': 'DD-MM-YYYY',
    'Key4': 'DD-MM-YYYY',
    'Key5': 'Value5',
    'Key6': 'Value6',
    'Key7': 'Value7'
    }
```

Initially the solution was pretty hacky. Very pretty hacky. 
Let's analyse the list first:
1. All the keys have no leading spaces or trailing spaces. they are exact.
2. All the values have some form of `\n` and leading and trailing space.
3. Further, each value has an empty string immediately after it. Edit: Wait. the first one doesn't have it.

Initial hacky Solution to convert it to a dict:
After I got this list, I would use a custom formatter() to do the following:
1. remove the first 6 empty strings. This inadverdently removed the value6 since it was usually an empty string. And since the next string was empty as well (all the time), I thought the key6 had a 0 value all the time.
2. remove the leading and trailing spaces using map() and str.strip
3. Then these lines here converted that list into a dict
```
for i in range(0, len(non_empty_data_list), 2):
        data_dict[non_empty_data_list[i]] = non_empty_data_list[i+1]
```

The list-to-dict command was written a bit wrong because of two things:
1. it spanned from 0 to len(non_empty_data_list). This was a bit wrong since it necessitated an extra 2 empty strings after Value7
2. Fortunately Value7 had one string empty string trailing it and I had to append one more before the list went to list-to-dict command

This could have been completely avoided by putting the range as `(0,len(non_empty_data_list)-2,2)`

This would have also solved the extra `:` I was getting at the end of the data_dict.



