# Use the python version 3
# clone the repo a install the pakcage from requirements.txt

# steps
  1. Clone the repo using: git clone https://github.com/RAJESH7500/price-optimization-backend
  2. install the requirements.txt using: pip3 install -r requirments.txt
  3. Once the packages installed run the server using: python3 run.py
  4. Once the server up and running you will see the output as
    <img width="1091" alt="image" src="https://github.com/user-attachments/assets/767a9af0-6c6c-49cd-abaa-50d9a3ca2b68" />
# End points

## Authentication 

### User Register Route
Method: POST
<br>
Endpoint: /api/auth/register
<br>
Body: {
  first_name,
  last_name,
  email,
  password,
  mobile_no,
  role //default to user
}

### User Login Route
Method: POST
<br>
Endpoint: /api/auth/login
<br>
Body: {
  email,
  password
}


## Product Routes
### Get list of all products
Method: GET
<br>
Endpoint: /api/products
<br>
Description: return the list of available products

### Get product
Method: GET
<br>
Endpoint: /api/products/:product_id
<br>
Description: return the product with given id


### Update product
Method: PUT
<br>
Endpoint: /api/products/:product_id
<br>
Description: update the existing product data


### Remove the product
Method: DELETE
<br>
Endpoint: /api/products/:poroduct_id
<br>
Description: Remove the product from the database


# Live URL
Link: [https://price-optimization-backend.onrender.com]

Note: All the routes protected by jwt token, in order to get the information need to login or register first
