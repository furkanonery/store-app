# store-app
Backend structure developed using Django REST Framework for an e-commerce application.

## Deploying the project on Docker

1. Build the Docker images using the following command:

    ```
    docker-compose build
    ```

2. Start the application and services with Docker Compose:

    ```
    docker-compose up
    ```

## Load sample data

1. Navigate to the core directory:
    ```
    cd core
    ```

2. Install the samples by entering the following command:
    ```
    python3 manage.py loaddata initial_data.json
    ```



## store-app API Documentation

This documentation outlines the usage and endpoints of the E-Commerce API. The API supports basic e-commerce functionalities such as product management, cart operations, and order processing.

- [x] Login
- [x] Logout
- [x] Register
- [x] Get user's profile information
- [x] Update user's profile information
- [x] List Products
- [x] List Products with query params
- [x] Search Products with Elasticsearch
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

### Register

This endpoint allows users to register in the system.
* The UserProfile model has been associated with the User model using signals.

**Request:**

### POST /register/
Content-Type: application/json

    {
        "first_name" : <your_firstname>,
        "last_name" : <your_lastname>,
        "username" : <your_username>,
        "email" : <your_email>,
        "password" : <your_password>,
        "password2" : <your_password>
    }

**Response Example:**

    {
        "username": <your_username>,
        "email": <your_email>,
        "first_name": <your_firstname>,
        "last_name": "<your_lastname>
    }

## User Profiles

### Get Profile

This endpoint retrieves the user's personal information.

**Request:**

### GET /api/userprofile/
Authorization: Token <your_token>

**Response Example:**

    {
        "id": 2,
        "bio": "Biographical information",
        "profile_picture": "File path of profile photo",
        "birth_date": "1999-01-01",
        "phone_number": "+90 000 000 00 00",
        "address": "İstanbul, Türkiye"
    }

### Update Profile

This endpoint allows the user to update their personal information.

**Request:**

### PATCH /api/userprofile/
Authorization: Token <your_token> <br>
Content-Type: application/json

    {
        "address": "Pendik, İstanbul, Türkiye"
    }

**Response Example:**

    {
        "id": 2,
        "bio": "Biographical information",
        "profile_picture": "File path of profile photo",
        "birth_date": "1999-01-01",
        "phone_number": "+90 000 000 00 00",
        "address": "Pendik, İstanbul, Türkiye"
    }

## Products

### List Products

This endpoint retrieves a list of available products.

**Request:**

### GET /api/products/


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

### GET /api/products?category=electronics


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

### Search Products with Elasticsearch

This endpoint performs analysis on the product names and descriptions based on the provided search parameters and returns the results.

**Request:**

### GET /api/search/?search=<search_value>

**Request Example:**

### GET /api/search/?search=wireless

**Response Example:**

    [
        {
            "description": "Premium wireless earbuds with noise cancellation.",
            "name": "Wireless Earbuds",
            "id": 2
        }
    ]

**Request Example:**

### GET /api/search/?search=premium

**Response Example:**

    [
        {
            "description": "Premium quality almonds for snacking.",
            "name": "Almonds",
            "id": 5
        },
        {
            "description": "Premium wireless earbuds with noise cancellation.",
            "name": "Wireless Earbuds",
            "id": 2
        }
    ]
    

### Add Product

This endpoint allows you to add a new product.

**Request:**

### POST /api/products/
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

### Detail Product

This endpoint retrieves the information of a single product.

**Request:**

### GET /api/products/{product_id}


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

### PATCH /api/products/{product_id}/
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

### DELETE /api/products/{products_id}

 **Response Example:**

Status Code: 204 No Content

## Carts
### List Cart

This endpoint retrieves the user's cart.

**Request:**

### GET /api/carts/
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

### POST /api/carts/
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

### DELETE /api/carts/{cart_id}/
Authorization: Token <your_token>

**Response Example:**

Status Code: 204 No Content

## CartItems
### List CartItems

This endpoint lists the cart items belonging to a user.

**Request:**

### GET /api/cartitems/
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

### GET /api/cartitems/{cartitem_id}
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

### POST /api/cartitems/
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

### PATCH /api/cartitems/{cartitems_id}
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

### DELETE /api/cartitems/{cartitems_id}

 **Response Example:**

Status Code: 204 No Content


## Orders
### List Orders

This endpoint retrieves the user's orders.

**Request:**

### GET /api/orders/
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

### POST /api/orders/
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

### GET /api/orders/order_id
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

Deletes the order based on the order's ID number.

**Request:**

### DELETE /api/orders/order_id
Authorization: Token <your_token>

**Response Example:**

Status Code: 204 No Content