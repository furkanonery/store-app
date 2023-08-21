# store-app
Backend structure developed using Django REST Framework for an e-commerce application.

# store-app API Documentation

This documentation outlines the usage and endpoints of the E-Commerce API. The API supports basic e-commerce functionalities such as product management, cart operations, and order processing.

- [x] Login
- [x] Logout
- [x] List Products
- [x] List Products with query params
- [x] Add Product
- [x] Get Product With ID
- [x] Update Product
- [x] Delete Product With ID
- [x] Get the cart with cart_items
- [x] Create Cart
- [x] Delete Cart With ID
- [x] List CartItems
- [x] Get CartItem With ID
- [x] Create CartItem
- [x] Update CartItem
- [x] Delete CartItem With ID
- [x] Listing the orders with order_items
- [x] Create Order
- [x] Get Order With ID
- [x] Delete Order With ID


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

### List Products with query params

This endpoint retrieves a list of available products with query params.

**Request:**

### GET /products?&category=electronics


**Response Example:**

    [
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
            "id": 43,
            "name": "Mouse",
            "description": "A high quality mouse.",
            "price": "299.99",
            "stock": 50,
            "image": null,
            "category": 5
        }
    ]
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

### Delete Product With ID

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

**Response Example:**

    {
        "id": 31,
        "cart_items": [],
        "products": []
    }

### Delete Cart With ID

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

### Create CartItem

This endpoint retrieves a single cart item.

**Request:**

### POST /cartitems/
Authorization: Token <your_token> <br>
Content-Type: application/json

    {
        "quantity": 3,
        "product": 10
    }

**Response Example:**

    {
        "id": 46,
        "cart": 30,
        "quantity": 3,
        "product": 10
    }

### Update CartItem

This endpoint updates cart items.

**Request:**

### PATCH /cartitems/{cartitems_id}
Authorization: Token <your_token> <br>
Content-Type: application/json

    {
        "quantity": 34
    }

**Response Example:**

    {
        "id": 38,
        "cart": 30,
        "quantity": 34,
        "product": 11
    }

### Delete CartItem With ID

This endpoint is used to delete a Cart Item.

**Request:**

### DELETE /cartitems/{cartitems_id}

 **Response Example:**

Status Code: 204 No Content


## Orders
### List Orders

This endpoint retrieves the user's orders.

**Request:**

### GET /orders/
Authorization: Token <your_token>

**Response Example:**

    [
        {
            "id": 50,
            "order_items": [
                {
                    "id": 47,
                    "order": 50,
                    "quantity": 2,
                    "product": 10
                },
                {
                    "id": 48,
                    "order": 50,
                    "quantity": 3,
                    "product": 11
                }
            ],
            "products": [
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
            ],
            "total_price": 1134.95,
            "created_at": "2023-08-21T13:52:27.509025Z"
        },
        {
            "id": 52,
            "order_items": [
                {
                    "id": 52,
                    "order": 52,
                    "quantity": 2,
                    "product": 41
                }
            ],
            "products": [
                {
                    "id": 41,
                    "name": "laptop",
                    "description": "A high-performance laptop.",
                    "price": "1599.99",
                    "stock": 20,
                    "image": null,
                    "category": 5
                }
            ],
            "total_price": 3199.98,
            "created_at": "2023-08-21T14:00:03.064448Z"
        }
    ]

### Create Order

An order is being created based on the user's cart.

**Request:**

### POST /orders/
Authorization: Token <your_token>

**Response Example:**

    {
        "id": 52,
        "order_items": [
            {
                "id": 52,
                "order": 52,
                "quantity": 2,
                "product": 41
            }
        ],
        "products": [
            {
                "id": 41,
                "name": "laptop",
                "description": "A high-performance laptop.",
                "price": "1599.99",
                "stock": 20,
                "image": null,
                "category": 5
            }
        ],
        "total_price": 3199.98,
        "created_at": "2023-08-21T14:00:03.064448Z"
    }

### Get Order With ID

It returns order details based on the order's ID number.

**Request:**

### GET /orders/order_id
Authorization: Token <your_token>

**Response Example:**

    {
        "id": 50,
        "order_items": [
            {
                "id": 47,
                "order": 50,
                "quantity": 2,
                "product": 10
            },
            {
                "id": 48,
                "order": 50,
                "quantity": 3,
                "product": 11
            }
        ],
        "products": [
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
        ],
        "total_price": 1134.95,
        "created_at": "2023-08-21T13:52:27.509025Z"
    }

### Delete Order With ID

It returns order details based on the order's ID number.

**Request:**

### DELETE /orders/order_id
Authorization: Token <your_token>

**Response Example:**

Status Code: 204 No Content