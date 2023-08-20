# store-app
Backend structure developed using Django REST Framework for an e-commerce application.

# store-app API Documentation

This documentation outlines the usage and endpoints of the E-Commerce API. The API supports basic e-commerce functionalities such as product management, cart operations, and order processing.

## Authorization

### Login

This endpoint generates a token that allows users to authenticate into the system.

**Request:**

### POST /login/
Content-Type: application/json

    {
        "username" : <your_username>,
        "password" : <your_password>
    }

**Response Example:**

    {
        "token": <Token>,
        "user_id": <user_id>
    }

### Logout

This endpoint deletes the token generated for the user.

### POST /logout/
Authorization: Token <your_token>

**Response Example:**

Status Code: 204 No Content

## Products

### List Products

This endpoint retrieves a list of available products.

**Request:**

### GET /products/


**Response Example:**

    {
        "id": 10,
        "name": "siirt pistachio",
        "description": "An endemic nut grown in Siirt, Turkey.",
        "price": "499.99",
        "stock": 7500,
        "image": "http://127.0.0.1:8000/media/products/2023/08/18/test.jpeg",
        "category": 4
    },
    {
        "id": 11,
        "name": "çorum chickpeas(leblebi)",
        "description": "Çorum's famous roasted chickpea is made from black peas.",
        "price": "44.99",
        "stock": 9200,
        "image": "http://127.0.0.1:8000/media/products/2023/08/18/test_como3qo.jpeg",
        "category": 4
    },
    // Other products

### Add Product

This endpoint allows you to add a new product.

**Request:**

### POST /products/
Content-Type: application/json

    {
        "name": "laptop",
        "description": "A high-performance laptop.",
        "price": "1299.99",
        "stock": 20,
        "category": <category_id>
    }

 **Response Example:**

    {
        "id": 41,
        "name": "laptop",
        "description": "A high-performance laptop.",
        "price": "1299.99",
        "stock": 20,
        "image": null,
        "category": 5
    }

## Detail Product

This endpoint retrieves the information of a single product.

**Request:**

### GET /products/{product_id}


**Response Example:**

    {
        "id": 41,
        "name": "laptop",
        "description": "A high-performance laptop.",
        "price": "1299.99",
        "stock": 20,
        "image": null,
        "category": 5
    }

### Update Product

This endpoint is used to update product information.

**Request:**

### PATCH /products/{product_id}/
Content-Type: application/json

    {
        "price": "1599.99"
    }

 **Response Example:**

    {
        "id": 41,
        "name": "laptop",
        "description": "A high-performance laptop.",
        "price": "1599.99",
        "stock": 20,
        "image": null,
        "category": 5
    }

### Delete Product

This endpoint is used to delete a product.

**Request:**

### DELETE /products/{products_id}

 **Response Example:**

Status Code: 204 No Content

## Carts
### List Cart

This endpoint retrieves the user's cart.

**Request:**

### GET /carts/
Authorization: Token <your_token>

 **Response Example:**

    [
        {
            "id": 10,
            "cart_items": [
                {
                    "id": 3,
                    "quantity": 5,
                    "cart": 10,
                    "product": 41
                },
                {
                    "id": 4,
                    "quantity": 8,
                    "cart": 10,
                    "product": 10
                },
                {
                    "id": 10,
                    "quantity": 56,
                    "cart": 10,
                    "product": 11
                }
            ],
            "user": "user1",
            "products": [
                {
                    "id": 41,
                    "name": "laptop",
                    "description": "A high-performance laptop.",
                    "price": "1599.99",
                    "stock": 20,
                    "image": null,
                    "category": 5
                },
                {
                    "id": 10,
                    "name": "siirt pistachio",
                    "description": "An endemic nut grown in Siirt, Turkey.",
                    "price": "499.99",
                    "stock": 7500,
                    "image": "http://localhost:8000/media/products/2023/08/18/test.jpeg",
                    "category": 4
                },
                {
                    "id": 11,
                    "name": "çorum chickpeas(leblebi)",
                    "description": "Çorum's famous roasted chickpea is made from black peas.",
                    "price": "44.99",
                    "stock": 9200,
                    "image": "http://localhost:8000/media/products/2023/08/18/test_como3qo.jpeg",
                    "category": 4
                }
            ]
        }
    ]

### Create Cart

This endpoint creates a new cart.

**Request:**

### POST /carts/
Authorization: Token <your_token>
Content-Type: application/json

    {
        "user": <user_id>
    }

**Response Example:**

    {
        "id": 6,
        "user": "user1",
        "cart_items": []
    }

### Delete Cart

This endpoint deletes the cart.

**Request:**

### DELETE /carts/{cart_id}/
Authorization: Token <your_token>

**Response Example:**

Status Code: 204 No Content

## CartItems
### List CartItems

This endpoint lists the cart items belonging to a user.

**Request:**

### GET /cartitems/
Authorization: Token <your_token>

**Response Example:**

    {
        "id": 3,
        "quantity": 5,
        "cart": 10,
        "product": 41
    },
    {
        "id": 4,
        "quantity": 8,
        "cart": 10,
        "product": 10
    },
    // Other cart items

### Get CartItem

This endpoint retrieves a single cart item.

**Request:**

### GET /cartitems/{cartitem_id}
Authorization: Token <your_token>

**Response Example:**

    {
        "id": 4,
        "quantity": 8,
        "cart": 10,
        "product": 10
    }


## Orders
### List Orders

This endpoint retrieves the user's orders.

**Request:**

### GET /orders/
Authorization: Token <your_token>

**Response Example:**

    [
        {
            "id": 1,
            "user": "user1",
            "order_items": [
                {
                    "product": 1,
                    "quantity": 2
                },
                // Other products
            ],
            "total_price": "1199.98",
            "created_at": "2023-08-17T13:35:11.916924Z"
        },
        // Other orders
    ]
