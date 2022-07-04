# FastAPI
FastAPI Tutorial python version `3.10.3`

## Set up and Run

### Run in local

Plain `main.py` in root directory:
```
python -m uvicorn main:app --reload 
```

If you put the code inside an `app` folder:

```
python -m uvicorn app.main:app --reload 
```

The changes automatically reload.

## Resources
* [This](https://www.youtube.com/watch?v=0sOvCWFmrtA) Is the main video tutorial
* [http methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
* [http status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
* [postman](https://www.postman.com/) Help us do http requests
* [pydantic](https://pydantic-docs.helpmanual.io/) Force data to have the schema we expect
