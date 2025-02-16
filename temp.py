import uuid

# Generate a random UUID
generated_uuid = uuid.uuid4()

# Convert the UUID to an integer
uuid_int = generated_uuid.int

# Limit the UUID to 6 digits by taking modulo 10^6
uuid_int_6_digits = uuid_int % 1000000

# Print the 6-digit integer value of the UUID
print(uuid_int_6_digits)
