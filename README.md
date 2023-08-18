# store-app
Backend structure developed using Django REST Framework for an e-commerce application.

# store-app API Documentation

This documentation outlines the usage and endpoints of the E-Commerce API. The API supports basic e-commerce functionalities such as product management, cart operations, and order processing.

## Products

### List Products [GET /products/]

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

### Add Product [POST /products/]

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

## Carts
### List Cart [GET /carts/]

This endpoint retrieves the user's cart.

**Request:**

### GET /carts/
Authorization: Token <your_token>

 **Response Example:**

    {
        "id": 5,
        "user": "user1",
        "cart_items": [
            {
                "product": 1,
                "quantity": 3
            },
            // Other products
        ]
    }

### Create Cart [POST /carts/]

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

### Update Cart [PUT /carts/{cart_id}/]

This endpoint updates the cart.

**Request:**

### PUT /carts/6/
Authorization: Token <your_token>
Content-Type: application/json

    {
        "user": "user1",
        "cart_items": [
            {
                "product": 1,
                "quantity": 2
            }
        ]
    }

**Response Example:**

    {
        "id": 6,
        "user": "user1",
        "cart_items": [
            {
                "product": 1,
                "quantity": 2
            }
        ]
    }

### Delete Cart [DELETE /carts/{cart_id}/]

This endpoint deletes the cart.

**Request:**

### DELETE /carts/6/
Authorization: Token <your_token>

**Response Example:**

Status Code: 204 No Content

## Orders
### List Orders [GET /orders/]

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