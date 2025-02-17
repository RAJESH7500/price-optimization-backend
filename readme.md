# Use the python version 3
# clone the repo a install the pakcage from requirements.txt

# steps
  1. Clone the repo using: git clone https://github.com/RAJESH7500/price-optimization-backend
  2. install the requirements.txt using:---> <b>pip3 install -r requirments.txt<b/>
  3. Once the packages installed run the server using:---> <b>gunicorn app:app<b/> 
  4. Now server will open on url [http://127.0.0.1:8000]
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
