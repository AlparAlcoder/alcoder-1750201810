# API Documentation

This API consists of two endpoints that allow you to create and retrieve items. Each item is a dictionary that contains a name, description, and price.

## Dependencies

This API requires the following Python packages:

- `fastapi`
- `pydantic`

Install them with `pip install fastapi pydantic uvicorn`.

## Models

### Item

```python
class Item(BaseModel):
    name: str
    description: str
    price: float
```

The `Item` model has the following attributes:

- `name`: A string that represents the name of the item.
- `description`: A string that provides a description of the item.
- `price`: A float that represents the price of the item.

## Endpoints

### POST /items/

This endpoint allows you to create a new item.

#### Parameters

- `item`: An instance of the `Item` model.

#### Return

Returns the created `Item` model.

#### Example

```bash
curl -X POST "http://localhost:8000/items/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"apple\",\"description\":\"A juicy red apple\",\"price\":0.5}"
```

### GET /items/{item_name}

This endpoint allows you to retrieve a specific item by its name.

#### Parameters

- `item_name`: A string that represents the name of the item.

#### Return

Returns the requested `Item` model.

#### Example

```bash
curl -X GET "http://localhost:8000/items/apple" -H  "accept: application/json"
```

## Important Notes

- If you try to create an item with a name that already exists, the API will return a 400 error with the detail "Item already exists".
- If you try to retrieve an item that does not exist, the API will return a 404 error with the detail "Item not found". 

To run the API, use the following command: `uvicorn main:app --reload`. Replace `main` with the name of your Python file. The `--reload` flag enables hot reloading, which means the server will update whenever you make changes to your code.