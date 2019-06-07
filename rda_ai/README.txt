Get an API key from here: https://api.data.gov/signup/

And invoke the program like so,

```
$ USDA_CLIENT_API_TOKEN='YOUR_API_KEY' python3 nutrition_info_usda.py
```

Or, add the token to a `secrets.env` file, like so

```
# secrets.env
export USDA_CLIENT_API_TOKEN='YOUR_API_KEY'
```

Read the variable into your environment,

```
$ source secrets.env
```

and invoke the program thusly,

```
$ python3 nutrition_info_usda.py
```


